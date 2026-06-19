import os
import xml.etree.ElementTree as ET
import json
import requests
import anthropic

# Configure your API credentials (to be set in Northflank Environment Variables) [1]
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "your_anthropic_key_here")
DOUBLEWORD_KEY = os.getenv("DOUBLEWORD_API_KEY", "your_doubleword_key_here")

# Feeds targeting primary asset drivers in the competition [1]
NEWS_FEEDS = {
    "FOREX": "https://finance.yahoo.com/news/rss",
    "GOLD": "https://finance.yahoo.com/quote/GC=F/news",
    "CRYPTO": "https://finance.yahoo.com/quote/BTC-USD/news"
}

def fetch_rss_headlines(feed_url: str) -> list:
    """Fetches the latest 10 headlines from a target RSS feed."""
    headlines = []
    try:
        response = requests.get(feed_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            for item in root.findall(".//item")[:10]:
                title = item.find("title")
                if title is not None:
                    headlines.append(title.text)
    except Exception as e:
        print(f"⚠️ Failed to parse RSS feed {feed_url}: {e}")
    return headlines

def analyze_batch_with_nemotron(headlines: list) -> float:
    """
    Passes messy headlines to NVIDIA Nemotron-3 Nano (via Doubleword) [1].
    Nemotron acts as a cheap, low-latency filter, returning a structured score.
    """
    if not headlines:
        return 0.0
        
    combined_text = "\n".join(f"- {h}" for h in headlines)
    
    # Target Doubleword API URL structure (or configure to OpenAI-compatible endpoint) [1]
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
        "model": "nvidia/nemotron-3-8b", # Or your exact sponsor model path [1]
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=15)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content'].strip()
            # Extract only the float value
            return float(content)
    except Exception as e:
        print(f"⚠️ Doubleword / Nemotron call failed: {e}")
    return 0.0 # Return neutral if error [1]

def evaluate_macro_bias(forex_score: float, metal_score: float, crypto_score: float) -> str:
    """
    Utilizes Anthropic Claude for high-level macro reasoning [1].
    Claude interprets the aggregate scores to determine the overarching regime.
    """
    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    
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
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022", # Or your available Claude model [1]
            max_tokens=10,
            temperature=0.0,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text.strip().upper()
    except Exception as e:
        print(f"⚠️ Claude API call failed: {e}")
    return "NEUTRAL"

def run_sentiment_pipeline():
    print("📰 Fetching global market headlines...")
    
    forex_headlines = fetch_rss_headlines(NEWS_FEEDS["FOREX"])
    metal_headlines = fetch_rss_headlines(NEWS_FEEDS["GOLD"])
    crypto_headlines = fetch_rss_headlines(NEWS_FEEDS["CRYPTO"])
    
    print("🤖 Parsing news sentiment with NVIDIA Nemotron via Doubleword...")
    s_forex = analyze_batch_with_nemotron(forex_headlines)
    s_metal = analyze_batch_with_nemotron(metal_headlines)
    s_crypto = analyze_batch_with_nemotron(crypto_headlines)
    
    print(f"📊 Scores -> Forex: {s_forex:.2f} | Metals: {s_metal:.2f} | Crypto: {s_crypto:.2f}")
    
    print("🧠 Consulting Claude Managed Agent for macro evaluation...")
    bias = evaluate_macro_bias(s_forex, s_metal, s_crypto)
    print(f"🎯 Global Macro Bias set to: {bias}")
    
    # Save bias to local state file
    output_data = {
        "bias": bias,
        "scores": {
            "forex": s_forex,
            "metals": s_metal,
            "crypto": s_crypto
        }
    }
    
    with open("sentiment_regime.json", "w") as f:
        json.dump(output_data, f, indent=4)
    print("💾 Sentiment bias successfully written to 'sentiment_regime.json'.")

if __name__ == "__main__":
    run_sentiment_pipeline()