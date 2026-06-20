# sentiment_engine.py
import os
import asyncio
import xml.etree.ElementTree as ET
import json
import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel
import anthropic
import logfire

# Configure Logfire
logfire.configure(
    token="pylf_v1_eu_zwcrVr8W6Lq9FYfGFLcbP1kr3VmcL6kyJdTqpbZNNhMp",
    console=logfire.ConsoleOptions(min_log_level="notice")
)

# API Keys from Environment Variables
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "your_anthropic_key_here")
DOUBLEWORD_KEY = os.getenv("DOUBLEWORD_API_KEY", "your_doubleword_key_here")

# Robust Google News RSS feeds that reliably return clean XML
NEWS_FEEDS = {
    "FOREX": "https://news.google.com/rss/search?q=forex+currencies+market&hl=en-US",
    "GOLD": "https://news.google.com/rss/search?q=gold+silver+precious+metals+market&hl=en-US",
    "CRYPTO": "https://news.google.com/rss/search?q=bitcoin+ethereum+cryptocurrency+market&hl=en-US"
}

app = FastAPI(title="QuantBot Macro Sentiment Engine")

# Global in-memory state to serve requests instantly
CURRENT_SENTIMENT = {
    "bias": "NEUTRAL",
    "scores": {
        "forex": 0.0,
        "metals": 0.0,
        "crypto": 0.0
    }
}

async def fetch_rss_headlines(session: aiohttp.ClientSession, feed_url: str) -> list[str]:
    """Asynchronously fetches the latest 10 headlines from an RSS feed."""
    headlines = []
    try:
        async with session.get(feed_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10) as response:
            if response.status == 200:
                content = await response.read()
                root = ET.fromstring(content)
                for item in root.findall(".//item")[:10]:
                    title = item.find("title")
                    if title is not None and title.text:
                        headlines.append(title.text)
    except Exception as e:
        print(f"⚠️ Failed to parse RSS feed {feed_url}: {e}")
    return headlines

async def analyze_batch_with_nemotron(session: aiohttp.ClientSession, headlines: list[str]) -> float:
    """Passes headlines to NVIDIA Nemotron-3 (via Doubleword) asynchronously."""
    if not headlines:
        return 0.0
        
    combined_text = "\n".join(f"- {h}" for h in headlines)
    url = "https://api.doubleword.co/v1/chat/completions" 
    headers = {
        "Authorization": f"Bearer {DOUBLEWORD_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = (
        "Analyze the following financial headlines. "
        "Return exactly one decimal number between -1.0 (extremely bearish) and +1.0 (extremely bullish) "
        "representing the net sentiment. Do not include any other text:\n\n"
        f"{combined_text}"
    )
    
    data = {
        "model": "nvidia/nemotron-3-8b", # Sponsor path [1]
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    try:
        async with session.post(url, json=data, headers=headers, timeout=15) as response:
            if response.status == 200:
                res_data = await response.json()
                content = res_data['choices'][0]['message']['content'].strip()
                return float(content)
    except Exception as e:
        print(f"⚠️ Doubleword / Nemotron call failed: {e}")
    return 0.0

async def evaluate_macro_bias(forex_score: float, metal_score: float, crypto_score: float) -> str:
    """Utilizes Anthropic Claude for high-level macro reasoning [1] asynchronously."""
    client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_KEY)
    
    prompt = (
        f"You are a quantitative macro strategist. Here are raw sentiment scores "
        f"derived from global markets (-1.0 to +1.0):\n"
        f"- Forex Markets: {forex_score:.2f}\n"
        f"- Precious Metals: {metal_score:.2f}\n"
        f"- Cryptocurrency Markets: {crypto_score:.2f}\n\n"
        f"Determine the overarching global market bias to adjust our trade execution. "
        f"Choose exactly one of the following words:\n"
        f"- BULLISH\n"
        f"- BEARISH\n"
        f"- NEUTRAL\n\n"
        f"Respond with only that word."
    )
    
    try:
        message = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=10,
            temperature=0.0,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text.strip().upper()
    except Exception as e:
        print(f"⚠️ Claude API call failed: {e}")
    return "NEUTRAL"

async def sentiment_updater_task():
    """Background loop to periodically fetch and refresh global sentiment bias."""
    while True:
        try:
            print("📰 Fetching global market headlines...")
            async with aiohttp.ClientSession() as session:
                # Parallel feed fetching
                forex_task = fetch_rss_headlines(session, NEWS_FEEDS["FOREX"])
                metal_task = fetch_rss_headlines(session, NEWS_FEEDS["GOLD"])
                crypto_task = fetch_rss_headlines(session, NEWS_FEEDS["CRYPTO"])
                
                forex_hl, metal_hl, crypto_hl = await asyncio.gather(forex_task, metal_task, crypto_task)
                
                print("🤖 Parsing news sentiment with NVIDIA Nemotron via Doubleword...")
                f_task = analyze_batch_with_nemotron(session, forex_hl)
                m_task = analyze_batch_with_nemotron(session, metal_hl)
                c_task = analyze_batch_with_nemotron(session, crypto_hl)
                
                s_forex, s_metal, s_crypto = await asyncio.gather(f_task, m_task, c_task)
                
                print("🧠 Consulting Claude Managed Agent for macro evaluation...")
                bias = await evaluate_macro_bias(s_forex, s_metal, s_crypto)
                
                # Update global state safely
                CURRENT_SENTIMENT["bias"] = bias
                CURRENT_SENTIMENT["scores"] = {
                    "forex": s_forex,
                    "metals": s_metal,
                    "crypto": s_crypto
                }
                
                print(f"🎯 Global Macro Bias successfully updated to: {bias}")
                logfire.notice("Global Macro Bias Updated", bias=bias)
        except Exception as e:
            print(f"❌ Error in background sentiment loop: {e}")
            
        # Refresh every 5 minutes
        await asyncio.sleep(300)

@app.on_event("startup")
async def startup_event():
    # Run updater loop as a non-blocking background task on application startup
    asyncio.create_task(sentiment_updater_task())

@app.get("/sentiment")
async def get_sentiment():
    """Returns the latest compiled macro bias to the MT5 runner."""
    return CURRENT_SENTIMENT