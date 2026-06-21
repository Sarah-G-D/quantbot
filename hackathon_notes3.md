Skip to main content
We have updated our Terms of Service. Learn more
incognito
Temporary chat
 Your conversation won’t be saved automatically
51,463 tokens

User 12:00 PM
ok I'm doing a hackathon. these are the rules AI Trading Competition Rules
Note: All dates and times in this document are in British Summer Time (BST).
Competition Positioning
This is an AI / Quant / Hybrid Trading Competition based on simulated funds, real market quotes, and a real liquidity environment. The goal of the competition is not to reward a single extreme bet, but to reward trading systems that can generate returns amid market volatility, manage risk, and possess reproducible logic.
Participants may use quantitative strategies, AI agents, human-assisted judgment, hybrid strategies, self-developed models, or third-party tools. The organizer will not evaluate the subjective intent of any trading strategy, and will rank, eliminate, and review participants solely on the basis of public, objective, and computable metrics.
Competition Account Rules
Item	Rule
Account type	Simulated trading account
Initial funds	1,000,000 USD
Maximum leverage	30x (1:30)
Stop-Out Level	30% — positions are force-liquidated when the margin level falls to 30%
Trading environment	Unified market data, order matching, and account conditions
Ranking basis	Account equity, return rate, maximum drawdown, Sharpe ratio, risk discipline
Principal risk	Zero risk to principal
All participants operate within the same market environment. The platform will not individually adjust price feeds based on the trading behavior of any single participant.
Competition Asset Scope
The competition covers the following tradable instruments across three categories: 8 forex pairs, 2 precious metals, and 5 cryptocurrencies (15 instruments in total).
Category	Instruments
Forex	AUD/USD, EUR/CHF, EUR/GBP, EUR/USD, GBP/USD, USD/CAD, USD/CHF, USD/JPY
Metals	XAG/USD, XAU/USD
Crypto	BAR/USD, BTC/USD, ETH/USD, SOL/USD, XRP/USD
4. Pre-Competition Preparation and Access Arrangements
15 Jun — Opening. That evening from 17:00 to 20:00, the competition portal and relevant materials will be made accessible to the public. All registered participants may access competition data, including historical data for backtesting, as well as the technical toolkits provided by participating sponsors. From their first login, all participants can view their trading account credentials (usernames and passwords) to familiarize themselves with the interface and operational workflows, though trading remains disabled during this stage.
18 Jun 22:00 — Second Registration Deadline. The official competition is scheduled to commence at 21 Jun 22:00.
All competition-related data, rules, platform permissions, and trading conditions will be fully and equitably accessible to all participants prior to the official launch.
Competition Schedule
Date	Phase	Details
15 Jun	Opening / Rules Announcement	17:00-20:00: Access to the competition portal, historical data, and sponsor toolkits opens; from first login, all participants can view their trading credentials to explore the interface (trading disabled).
18 Jun	Registration Deadline	22:00: Second registration deadline.
21 Jun	Official Launch	22:00: Competition begins; all trading accounts initialize with the same initial funds.
22 Jun	Round 1 Conclusion	22:00: Rankings recorded; number of qualifiers TBC; 22:00-23:00: Compliance review & verification.
23 Jun	Round 2 Conclusion	22:00: Rankings recorded; number of qualifiers TBC; 22:00-23:00: Compliance review & verification.
24 Jun	Round 3 Conclusion	22:00: Rankings recorded; number of qualifiers TBC; 22:00-23:00: Compliance review & verification.
24-26 Jun	Final Phase	24 Jun 22:00 - 26 Jun 22:00: Top 100 compete in the Finals.
26 Jun	Post-Finals Audit / Results Audit	22:00-23:00: Anomaly detection, confirmation of final rankings, and review of trading logs and anomalies.
27 Jun	Results Announcement & Awards	Final rankings, official competition highlights, and award ceremony.
Data and Platform Access Rules
The organizer provides all participants with historical market data for strategy backtesting, model training, parameter tuning, and execution logic preparation.
The platform is not guaranteed to feature a complete, built-in backtesting engine. Participants may utilize the provided data to conduct independent backtesting and model evaluation within their own environments.
For participants deploying the platform's native AI Agents, basic strategy evaluation and backtesting assistance may be available, though with less flexibility than a bespoke/self-built framework. This option is primarily tailored for participants with limited trading experience.
Pricing and Execution Mechanism
Platform quotes aggregate liquidity from multiple brokers and sources, integrated with risk-pricing logic, to establish the final tradable prices.
The organizer will not skew or adjust quotes based on the trading behavior of any individual participant. The bid/ask quotes seen by all participants at the same moment remain consistent.
Trades execute within a simulated environment engineered to replicate real-market liquidity, depth, spreads, and impact cost as closely as possible. Consequently, both market orders and pending orders are subject to market depth, available volume, partial fills, slippage, and market impact.
Transparency & Compliance Mechanism
During the elimination phase (21 Jun – 24 Jun), participants have access to near-real-time leaderboards, peer trading logs, current positions, account performance, and risk metrics, subject to a 5-minute latency.
Following the conclusion of each round (between 22:00 and 23:00), the system freezes snapshots for ranking records, compiles trade/risk metrics, and runs anomalous trading detection to review potential compliance violations. Should any anomalies be flagged, the organizer will publicly disclose the anomaly type, the determination criteria, relevant Trade/Order IDs, and the resulting impact on qualification via the official Discord community.
During the final phase, peer trading logs, positions, and the live leaderboard will be blinded. Participants retain full visibility only over their own account equity, active positions, open orders, risk metrics, and available margin.
Upon competition closure on 27 Jun, the organizer will publish the final standings, key performance metrics, verified historical logs, necessary Trade/Order IDs, and official rulings on any penalties or disputes. To ensure regulatory compliance and privacy, all Personally Identifiable Information (PII) will remain strictly protected and undisclosed.
Technology Usage & Prize Eligibility
To be eligible for the competition's technology prize, participants are expected to share the technical details of their projects. Following the Round 3 elimination on 24 Jun, eligible participants should provide:
A link to the GitHub repository containing their project code;
An overview of the partner technologies utilized, along with a brief description of their application;
Details regarding their data usage; and
A demonstration showcasing how the project works.
Intellectual Property: Participants retain full ownership and intellectual property rights of their respective projects. Access to a project is requested solely to ensure the fairness and integrity of the judging process, and for no other purpose.
A submission form will be made available on the platform. Further details and instructions will be announced separately.
Core Ranking Logic
Final standings are determined by a formula-based composite score: PnL-driven, risk-adjusted, and strictly bound by red-line rules for absolute veto.
No subjective penalties or discretionary deductions shall be applied. Standard rankings are determined strictly via algorithmic formulas; high-risk behaviors are cataloged under Risk Discipline and penalized against explicit quantitative thresholds; critical violations result in direct disqualification or immediate elimination; ambiguous gray-area disputes trigger compliance reviews without resulting in arbitrary point deductions.
Scoring is purely formulaic. Disqualification is binary and rules-driven. Discretionary penalties are strictly zero.
Final Score Formula
To eliminate any ambiguity, the composite score is calculated as follows:
F
i
n
a
l
S
c
o
r
e
70
%
×
R
e
t
u
r
n
R
a
n
k
+
15
%
×
D
r
a
w
d
o
w
n
R
a
n
k
+
10
%
×
S
h
a
r
p
e
R
a
n
k
+
5
%
×
R
i
s
k
D
i
s
c
i
p
l
i
n
e
Final Score=70%×Return Rank+15%×Drawdown Rank+10%×Sharpe Rank+5%×Risk Discipline
(Note: "Rank" refers to the percentile or absolute ranking of the specific metric among all active participants.)
Metric Calculation Formulas
Return
The absolute return for participant
i
i within the given round is defined as:
R
e
t
u
r
n
i
E
q
u
i
t
y
f
i
n
a
l
,
i
−
E
q
u
i
t
y
i
n
i
t
i
a
l
E
q
u
i
t
y
i
n
i
t
i
a
l
Return
i
​
Equity
initial
​
Equity
final,i
​
−Equity
initial
​
​
Variable Definitions:
E
q
u
i
t
y
f
i
n
a
l
,
i
Equity
final,i
​
: Total account equity of participant
i
i at the conclusion of the round.
E
q
u
i
t
y
i
n
i
t
i
a
l
Equity
initial
​
: Initial account capital, fixed at
1
,
000
,
000
USD
1,000,000 USD.
R
e
t
u
r
n
i
Return
i
​
: The net return rate for participant
i
i.
2. Return Rank
The raw return is converted into a normalized rank score scaled from 0 to 100:
R
e
t
u
r
n
R
a
n
k
i
100
×
N
−
R
a
n
k
i
N
−
1
Return Rank
i
​
=100×
N−1
N−Rank
i
​
​
Ranking Logic: All active, non-eliminated participants are ranked by
R
e
t
u
r
n
i
Return
i
​
in descending order. The resulting rank (
R
a
n
k
i
Rank
i
​
) is then normalized.
Boundary Condition: In the event that only a single active participant remains (
N
1
N=1),
R
e
t
u
r
n
R
a
n
k
Return Rank defaults to 100.
3. Maximum Drawdown (MaxDD)
The maximum peak-to-trough decline in account equity during the round is monitored continuously:
M
a
x
D
D
i
max
⁡
t
(
P
e
a
k
E
q
u
i
t
y
i
,
t
−
E
q
u
i
t
y
i
,
t
P
e
a
k
E
q
u
i
t
y
i
,
t
)
MaxDD
i
​
=max
t
​
(
PeakEquity
i,t
​
PeakEquity
i,t
​
−Equity
i,t
​
​
)
Variable Definitions:
E
q
u
i
t
y
i
,
t
Equity
i,t
​
: Total account equity of participant
i
i at time
t
t.
P
e
a
k
E
q
u
i
t
y
i
,
t
PeakEquity
i,t
​
: The historical peak equity achieved by participant
i
i from the inception of the round up to time
t
t.
M
a
x
D
D
i
MaxDD
i
​
: The maximum drawdown recorded for the current round.
4. Drawdown Rank
The maximum drawdown is converted into a normalized rank score scaled from 0 to 100:
D
r
a
w
d
o
w
n
R
a
n
k
i
100
×
N
−
R
a
n
k
D
D
i
N
−
1
Drawdown Rank
i
​
=100×
N−1
N−RankDD
i
​
​
Ranking Logic: All participants are sorted by
M
a
x
D
D
i
MaxDD
i
​
in ascending order (lower drawdown yields a higher score), where
R
a
n
k
D
D
i
RankDD
i
​
represents the participant's absolute position.
5. Sharpe Ratio
This competition utilizes a non-annualized Sharpe Ratio, computed directly from 15-minute account equity returns.
The 15-minute interval return (
r
i
,
t
r
i,t
​
) is calculated as:
r
i
,
t
E
q
u
i
t
y
i
,
t
−
E
q
u
i
t
y
i
,
t
−
1
E
q
u
i
t
y
i
,
t
−
1
r
i,t
​
Equity
i,t−1
​
Equity
i,t
​
−Equity
i,t−1
​
​
The Sharpe Ratio for participant
i
i is defined as:
S
h
a
r
p
e
i
Mean
(
r
i
,
t
)
Std
(
r
i
,
t
)
Sharpe
i
​
Std(r
i,t
​
)
Mean(r
i,t
​
)
​
Variable Definitions:
r
i
,
t
r
i,t
​
: The return achieved by participant
i
i during the
t
t-th 15-minute interval.
Mean
(
r
i
,
t
)
Mean(r
i,t
​
): The arithmetic mean of the 15-minute interval returns.
Std
(
r
i
,
t
)
Std(r
i,t
​
): The standard deviation of the 15-minute interval returns.
S
h
a
r
p
e
i
Sharpe
i
​
: The non-annualized Sharpe Ratio.
Boundary Constraints:
If
Std
(
r
i
,
t
)
0
Std(r
i,t
​
)=0,
S
h
a
r
p
e
i
Sharpe
i
​
is defined as 0.
To prevent statistical anomalies from sparse data, if an account contains fewer than 8 valid 15-minute return observations, its final
S
h
a
r
p
e
R
a
n
k
Sharpe Rank shall be capped at a maximum of 50 points.
6. Sharpe Rank
The Sharpe Ratio is converted into a normalized rank score scaled from 0 to 100:
S
h
a
r
p
e
R
a
n
k
i
100
×
N
−
R
a
n
k
S
h
a
r
p
e
i
N
−
1
Sharpe Rank
i
​
=100×
N−1
N−RankSharpe
i
​
​
Ranking Logic: All active participants are ranked by
S
h
a
r
p
e
i
Sharpe
i
​
in descending order, where
R
a
n
k
S
h
a
r
p
e
i
RankSharpe
i
​
represents the participant's absolute position.
13. Risk Discipline Rules
Each participant starts each round with a baseline Risk Discipline score of 100 points, subject to deductions for verified risk violations, down to a floor of 0. The Risk Discipline score is calculated independently per round and resets automatically at each round's inception.
Critical red-line violations bypass the reset protocol. Actions including forced liquidation, exploitation of system vulnerabilities, API abuse, multi-account participation, or manipulation of competition fairness will, once confirmed, lead directly to disqualification.
Margin Usage
The margin utilization rate for participant
i
i is defined as:
M
a
r
g
i
n
U
s
a
g
e
i
U
s
e
d
M
a
r
g
i
n
i
E
q
u
i
t
y
i
Margin Usage
i
​
Equity
i
​
Used Margin
i
​
​
Violation Criteria	Risk Discipline Penalty
M
a
r
g
i
n
U
s
a
g
e
i
90
%
Margin Usage
i
​
90% persisting for a continuous duration of
≥
30
minutes
≥30 minutes	-20 points
M
a
r
g
i
n
U
s
a
g
e
i
95
%
Margin Usage
i
​
95% persisting for a continuous duration of
≥
15
minutes
≥15 minutes	-30 points
M
a
r
g
i
n
U
s
a
g
e
i
98
%
Margin Usage
i
​
98% persisting for a continuous duration of
≥
10
minutes
≥10 minutes	Triggers Compliance Review
Leverage Usage
The effective leverage ratio for participant
i
i is calculated as:
L
e
v
e
r
a
g
e
i
G
r
o
s
s
N
o
t
i
o
n
a
l
E
x
p
o
s
u
r
e
i
E
q
u
i
t
y
i
Leverage
i
​
Equity
i
​
Gross Notional Exposure
i
​
​
Violation Criteria	Risk Discipline Penalty
L
e
v
e
r
a
g
e
i
28
x
Leverage
i
​
28x persisting for a continuous duration of
≥
30
minutes
≥30 minutes	-20 points
L
e
v
e
r
a
g
e
i
29
x
Leverage
i
​
29x persisting for a continuous duration of
≥
15
minutes
≥15 minutes	-30 points
L
e
v
e
r
a
g
e
i
Leverage
i
​
approaching
30
x
30x for a continuous duration of
≥
10
minutes
≥10 minutes	Triggers Compliance Review
Exposure Concentration
Asset and direction concentration metrics are defined via the following allocation ratios:
S
i
n
g
l
e
I
n
s
t
r
u
m
e
n
t
E
x
p
o
s
u
r
e
i
N
o
t
i
o
n
a
l
E
x
p
o
s
u
r
e
s
i
n
g
l
e
G
r
o
s
s
N
o
t
i
o
n
a
l
E
x
p
o
s
u
r
e
i
Single Instrument Exposure
i
​
Gross Notional Exposure
i
​
Notional Exposure
single
​
​
Violation Criteria	Risk Discipline Penalty
Single-instrument exposure
90
%
90% persisting for a continuous duration of
≥
30
minutes
≥30 minutes	-10 points
Net Directional Exposure
95
%
95% persisting for a continuous duration of
≥
30
minutes
≥30 minutes	-10 points
(Note: Directional trading is permitted. What the rules restrict is the prolonged, extremely concentrated, near-full-leverage use of risk.)
Red-Line Rules
Forced Liquidation: Triggers immediate elimination from the competition, with no advancement to the next round.
Exploitation of System Vulnerabilities: Results in immediate disqualification. This includes exploiting system vulnerabilities, erroneous quotes, latency loopholes, matching-engine anomalies, settlement anomalies, or circumventing system limits.
API Abuse: Results in immediate disqualification. This includes maliciously flooding API endpoints, bypassing API rate limits, attacking or interfering with platform services, unauthorized access to systems or data, and high-frequency requests that cause system anomalies.
Safe Harbor Threshold: High-frequency requests within a normal range are not deemed abnormal; for example, requests at or below 500 per second will not be automatically classified as abnormal behavior. However, if request behavior causes system anomalies, circumvents limits, or affects the fairness for other participants, the organizer reserves the right to review.
Multi-Account Participation by the Same User: Results in immediate disqualification. Each participant may use only one account to compete.
Unauthorized Collaboration or Collusion to Manipulate Rankings: Manipulating rankings through multiple accounts, external (out-of-team) collaboration, mutual transfer of risk, pre-arranged trading, or any other means is prohibited.
Elimination and Qualification Rules
At the conclusion of each round, the qualification and elimination protocol executes via the following sequential workflow:
22:00 — Data Snapshot: The system freezes and logs all account equity, active positions, historical trading logs, and risk metrics for the current round.
22:00 - 23:00 — Compliance & Audit Window:
Anomaly Detection: Run automated screening for traffic and trading anomalies.
Red-Line Verification: Cross-check trading logs against the defined red-line rules.
Account Purge: Disqualify and remove any accounts that triggered violations or suffered forced liquidation (account wipeout).
Score Calculation & Ranking: Compute individual performance metrics, generate the Final Score for all remaining active accounts, and sort participants in descending order.
Roster Finalization & Public Disclosure: Finalize the official qualification roster for the next round. Any flagged anomalies and compliance rulings will be publicly disclosed within the official Discord community.
Qualification Schedule
Round	Trading Cutoff	Audit & Review Window	Qualified Status
Round 1	22 Jun 22:00	22:00 - 23:00	Qualifiers TBC
Round 2	23 Jun 22:00	22:00 - 23:00	Qualifiers TBC
Round 3	24 Jun 22:00	22:00 - 23:00	Qualifiers TBC
Finals	26 Jun 22:00	22:00 - 23:00	Final Ranking
16. Tie-Breaking Protocols
In the event that multiple participants conclude a round with identical Final Scores, deadlocks will be systematically resolved based on the following strict hierarchy of performance metrics:
Primary: Higher
R
e
t
u
r
n
i
Return
i
​
(descending order).
Secondary: Lower
M
a
x
D
D
i
MaxDD
i
​
(ascending order).
Tertiary: Higher
S
h
a
r
p
e
i
Sharpe
i
​
(descending order).
Quaternary: Higher Risk Discipline score (descending order).
Quinary: More reasonable trading activity.
Fallback: If a tie persists after applying all the above quantitative layers, the organizer will conduct a review and publish the basis for its decision.
Best Sharpe Ratio Award
Prize: $10,000 — awarded to the eligible participant with the highest Sharpe Ratio.
Eligibility. To qualify, a participant must:
reach the Finals;
finish within the Top 50 of the final overall ranking;
have no red-line violations;
have executed at least 30 trades.
Sharpe Ratio Formula. The Sharpe Ratio is computed from 15-minute account-equity returns and is not annualized. Returns are sampled at 15-minute intervals throughout the entire competition period.
r
i
,
t
E
q
u
i
t
y
i
,
t
−
E
q
u
i
t
y
i
,
t
−
1
E
q
u
i
t
y
i
,
t
−
1
r
i,t
​
Equity
i,t−1
​
Equity
i,t
​
−Equity
i,t−1
​
​
S
h
a
r
p
e
i
Mean
(
r
i
,
t
)
Std
(
r
i
,
t
)
Sharpe
i
​
Std(r
i,t
​
)
Mean(r
i,t
​
)
​
Variable Definitions:
E
q
u
i
t
y
i
,
t
Equity
i,t
​
: Account equity of participant
i
i at the close of the
t
t-th 15-minute interval.
E
q
u
i
t
y
i
,
t
−
1
Equity
i,t−1
​
: Account equity of participant
i
i at the close of the previous 15-minute interval.
r
i
,
t
r
i,t
​
: The 15-minute account return of participant
i
i.
Mean
(
r
i
,
t
)
Mean(r
i,t
​
): The arithmetic mean of the 15-minute interval returns.
Std
(
r
i
,
t
)
Std(r
i,t
​
): The standard deviation of the 15-minute interval returns.
S
h
a
r
p
e
i
Sharpe
i
​
: The non-annualized Sharpe Ratio of participant
i
i.
Winner Selection. Among all eligible participants, the participant with the highest Sharpe Ratio shall be declared the winner. In the event of a tie:
The participant with the higher Final Return shall be ranked higher;
If the tie persists, the participant with the lower Maximum Drawdown shall be ranked higher.
18. Appeals and Dispute Resolution
Participants may file reasonable appeals during or after the competition. The organizer will keep feedback and appeal channels open.
For ambiguous gray-area disputes or those difficult to adjudicate objectively, the organizer may disclose the relevant facts, redact personal sensitive information, publish the Trade IDs / Order IDs, organize community discussion, and, where necessary, put the matter to a participant vote.
Scope of Authority Statement: The organizer's role is not to judge the intent behind participants' strategies, but to safeguard the order, fairness, and integrity of the competition.
Principle of Public Disclosure of Penalties
For any penalty, elimination, or disqualification decision, the organizer will disclose to all participants:
The reason for the penalty.
The basis for the determination.
The relevant Trade IDs / Order IDs.
The impact on rankings.
For privacy protection, the organizer will not disclose real names, email addresses, phone numbers, identity information, or other personal sensitive information.
Organizer's Reserved Rights
The organizer reserves the right to suspend, adjust, review, or modify the competition arrangements in the event of:
System failures.
Market-data anomalies or quote anomalies.
Matching anomalies or settlement anomalies.
API-service anomalies.
Large-scale force majeure or technical issues that clearly affect fairness.
In any such case, the organizer will publish the reasons, scope of impact, and resolution as transparently as possible. I have set up 5 bots with 5 different strategies who vote and then this is compiled by the apha agent and executed by the main agent. I have a remote desktop with Amazon lightsail. On my main desktop I ahve python on visual coder. This then feeds into github and then into the remote desktop. And into metatrader 5 which then will connect to symphonix for the trading. I also want to set up market signals for the data. I have access to Northflank $100 credits, doublewood for more efficient IQ per follar, pydantic $50 credit and logfire, and then nvidia nemotro 3 nano and anthropic $50 credits in claude console. I want to set up a market watch to assess for news impact on the assets I am trading. THe credits need to last the whole competiion and I need to put the restults of the market data into asyinc batch with strucutred outputs from unstructures information. Would it be helpful if I pasted in the existing pyhton code here and then step by step we can set up the market watch.
Model 12:00 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
User 12:05 PM
ok These are the code. Also feel free to suggest improvements. These were tested on the backtesting data we got given. 1. bot1.py:
strategies/bot1.py
class Bot1:
"""
Bot 1: Order Book Imbalance (OBI).
Detects structural supply and demand imbalances in the order book depth.
"""
def init(self, threshold: float = 0.45):
# Default optimized to 0.45 based on Fold 2 cross-validation
self.threshold = threshold
code
Code
def evaluate(self, row) -> str:
    # Fast path: Use pre-calculated column
    if 'book_imbalance' in row:
        try:
            imbalance = float(row['book_imbalance'])
            if imbalance > self.threshold:
                return "BUY"
            elif imbalance < -self.threshold:
                return "SELL"
        except (ValueError, TypeError):
            pass
    
    # Fallback path: Calculate directly from raw lists if present
    try:
        total_bids = sum(row.get('bidsizes', []))
        total_asks = sum(row.get('asksizes', []))
        if (total_bids + total_asks) > 0:
            imbalance = (total_bids - total_asks) / (total_bids + total_asks)
            if imbalance > self.threshold:
                return "BUY"
            elif imbalance < -self.threshold:
                return "SELL"
    except Exception:
        pass
        
    return "HOLD"
bot2.py:
strategies/bot2.py
import numpy as np
class Bot2:
"""
Bot 2: Volatility-Filtered EMA Momentum.
EMA crossovers are executed only when volatility is expanding.
"""
def init(self, fast: int = 5, slow: int = 15, vol_window: int = 20):
self.fast = fast
self.slow = slow
self.vol_window = vol_window
code
Code
def evaluate(self, price_history: list) -> str:
    if len(price_history) < self.vol_window:
        return "HOLD"
    
    # Convert only the slice we need to a numpy array to save CPU cycles
    prices = np.array(price_history[-self.vol_window:])
    
    fast_ma = np.mean(prices[-self.fast:])
    slow_ma = np.mean(prices[-self.slow:])
    
    recent_std = np.std(prices)
    
    # Safe lookup for previous standard deviation
    if len(price_history) > self.vol_window:
        prev_prices = np.array(price_history[-self.vol_window-1:-1])
        prev_std = np.std(prev_prices)
    else:
        prev_std = recent_std
    
    # Only signal a trade if standard deviation is expanding
    if recent_std > prev_std:
        if fast_ma > slow_ma:
            return "BUY"
        elif fast_ma < slow_ma:
            return "SELL"
            
    return "HOLD"
bot3.py:
strategies/bot3.py
import numpy as np
class Bot3:
"""
Bot 3: Statistical Mean Reversion (Z-Score).
Sells overbought extremes and buys oversold extremes.
"""
def init(self, window: int = 30, z_threshold: float = 2.5):
# Default optimized to 2.5 based on Fold 2 cross-validation
self.window = window
self.z_threshold = z_threshold
code
Code
def evaluate(self, mid_price: float, price_history: list) -> str:
    if len(price_history) < self.window:
        return "HOLD"
        
    window_prices = np.array(price_history[-self.window:])
    mean_val = np.mean(window_prices)
    std_val = np.std(window_prices)
    
    if std_val < 1e-8:
        return "HOLD"
        
    z_score = (mid_price - mean_val) / std_val
    
    if z_score < -self.z_threshold:
        return "BUY"
    elif z_score > self.z_threshold:
        return "SELL"
        
    return "HOLD"
4.bot4.py:
strategies/bot4.py
import numpy as np
class Bot4:
"""
Bot 4: Medium-Term Structural Trend Follower.
Keeps the council aligned with the broader market direction.
"""
def init(self, fast: int = 10, slow: int = 30):
self.fast = fast
self.slow = slow
code
Code
def evaluate(self, price_history: list) -> str:
    if len(price_history) < self.slow:
        return "HOLD"
        
    prices = np.array(price_history[-self.slow:])
    fast_ma = np.mean(prices[-self.fast:])
    slow_ma = np.mean(prices)
    
    if fast_ma > slow_ma:
        return "BUY"
    elif fast_ma < slow_ma:
        return "SELL"
        
    return "HOLD"
5.bot5.py:
strategies/bot5.py
class Bot5:
"""
Bot 5: Lead-Lag Cross-Asset Correlation.
Identifies momentum shifts in leading assets to predict lagging targets.
"""
def init(self, threshold_pct: float = 0.0005):
self.threshold_pct = threshold_pct
# Correlation mapping: {lagging_asset: leading_asset}
self.lead_lag_map = {
"GBPUSD": "EURUSD",
"XAGUSD": "XAUUSD",
"ETHUSD": "BTCUSD",
"SOLUSD": "BTCUSD",
"XRPUSD": "BTCUSD"
}
code
Code
def evaluate(self, symbol: str, current_prices: dict, price_histories: dict) -> str:
    leader = self.lead_lag_map.get(symbol)
    if not leader:
        return "HOLD"
        
    leader_history = price_histories.get(leader, [])
    if len(leader_history) < 2:
        return "HOLD"
        
    # Compare the last two recorded mid prices
    leader_prev = leader_history[-2]
    leader_curr = leader_history[-1]
    
    if leader_prev <= 0:
        return "HOLD"
        
    leader_return = (leader_curr - leader_prev) / leader_prev
    
    if leader_return > self.threshold_pct:
        return "BUY"
    elif leader_return < -self.threshold_pct:
        return "SELL"
        
    return "HOLD"
risk_agent.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
from pydantic import BaseModel, Field
def calculate_standalone_sharpe(equity_list) -> float:
if len(equity_list) < 8:
return 0.0
returns = []
for i in range(1, len(equity_list)):
prev = equity_list[i-1]
curr = equity_list[i]
if prev <= 0:
returns.append(0.0)
else:
returns.append((curr - prev) / prev)
std_dev = np.std(returns)
if std_dev == 0:
return 0.0
return float(np.mean(returns) / std_dev)
class AccountState(BaseModel):
equity: float
used_margin: float = 0.0
gross_exposure: float = 0.0
asset_exposures: dict[str, float] = Field(default_factory=dict)
class AssetRiskGuard:
def init(self):
self.MAX_LEVERAGE_GLOBAL = 30.0
self.STOP_OUT_LEVEL = 0.30
self.HARD_DRAWDOWN_LIMIT = 0.14
self.margin_rates = {"FOREX": 0.0333, "METALS": 0.0500, "CRYPTO": 0.2000}
code
Code
self.max_leverage_limits = {
        "BTCUSD": 2.0, "ETHUSD": 2.0, "SOLUSD": 2.0, "XRPUSD": 2.0, "BARUSD": 2.0,
        "XAUUSD": 5.0, "XAGUSD": 5.0, "FOREX": 5.0
    }
    
    self.peak_equity = 1000000.0
    self.max_drawdown = 0.0
    self.risk_discipline_score = 100.0
    
    self.margin_90_start = None
    self.margin_95_start = None
    self.margin_98_start = None
    
    self.leverage_28_start = None
    self.leverage_29_start = None
    self.leverage_30_start = None
    
    self.concentration_90_start = None
    self.deductions_applied = set()
    
    self.equity_history_15m = []
    self.last_sharpe_time = None
    self.total_completed_trades = 0
    self.REQUIRED_TRADES_FOR_PRIZE = 30
    self.MAX_RPS = 450.0  
    self.request_timestamps = []

def check_rate_limit(self) -> bool:
    now = time.time()
    self.request_timestamps = [t for t in self.request_timestamps if now - t < 1.0]
    if len(self.request_timestamps) >= self.MAX_RPS:
        return False
    self.request_timestamps.append(now)
    return True

def is_session_liquid(self, symbol: str, current_time) -> bool:
    if any(crypto in symbol for crypto in ["BTC", "ETH", "SOL", "XRP", "BAR"]):
        return True
    hour = current_time.hour
    if 21 <= hour < 23:
        return False
    return True

def calculate_metrics(self, account: AccountState, current_time):
    if account.equity > self.peak_equity:
        self.peak_equity = account.equity
        
    current_dd = (self.peak_equity - account.equity) / self.peak_equity if self.peak_equity > 0 else 0.0
    if current_dd > self.max_drawdown:
        self.max_drawdown = current_dd
        
    leverage = account.gross_exposure / account.equity if account.equity > 0 else 0.0
    margin_usage = account.used_margin / account.equity if account.equity > 0 else 0.0
    
    if self.last_sharpe_time is None or (current_time - self.last_sharpe_time) >= timedelta(minutes=15):
        self.equity_history_15m.append(account.equity)
        self.last_sharpe_time = current_time
        
    return current_dd, leverage, margin_usage

def evaluate_compliance_violations(self, account: AccountState, current_time):
    drawdown, leverage, margin_usage = self.calculate_metrics(account, current_time)
    
    max_asset = None
    max_asset_exposure = 0.0
    if account.gross_exposure > 0:
        for asset, exp in account.asset_exposures.items():
            if exp > max_asset_exposure:
                max_asset_exposure = exp
                max_asset = asset
        max_concentration = max_asset_exposure / account.gross_exposure
    else:
        max_concentration = 0.0

    # --- Margin Violations --- [1]
    if margin_usage > 0.90:
        if self.margin_90_start is None: self.margin_90_start = current_time
        elapsed = (current_time - self.margin_90_start).total_seconds() / 60.0
        if elapsed >= 30.0 and "margin_90" not in self.deductions_applied:
            self.risk_discipline_score = max(0.0, self.risk_discipline_score - 20)
            self.deductions_applied.add("margin_90")
    else:
        self.margin_90_start = None
        self.deductions_applied.discard("margin_90")

    if margin_usage > 0.95:
        if self.margin_95_start is None: self.margin_95_start = current_time
        elapsed = (current_time - self.margin_95_start).total_seconds() / 60.0
        if elapsed >= 15.0 and "margin_95" not in self.deductions_applied:
            self.risk_discipline_score = max(0.0, self.risk_discipline_score - 30)
            self.deductions_applied.add("margin_95")
    else:
        self.margin_95_start = None
        self.deductions_applied.discard("margin_95")

    if margin_usage > 0.98:
        if self.margin_98_start is None: self.margin_98_start = current_time
        elapsed = (current_time - self.margin_98_start).total_seconds() / 60.0
        if elapsed >= 10.0 and "margin_98" not in self.deductions_applied:
            self.risk_discipline_score = max(0.0, self.risk_discipline_score - 50)
            self.deductions_applied.add("margin_98")
    else:
        self.margin_98_start = None
        self.deductions_applied.discard("margin_98")

    # --- Leverage Violations --- [1]
    if leverage > 28.0:
        if self.leverage_28_start is None: self.leverage_28_start = current_time
        elapsed = (current_time - self.leverage_28_start).total_seconds() / 60.0
        if elapsed >= 30.0 and "leverage_28" not in self.deductions_applied:
            self.risk_discipline_score = max(0.0, self.risk_discipline_score - 20)
            self.deductions_applied.add("leverage_28")
    else:
        self.leverage_28_start = None
        self.deductions_applied.discard("leverage_28")

    if leverage > 29.0:
        if self.leverage_29_start is None: self.leverage_29_start = current_time
        elapsed = (current_time - self.leverage_29_start).total_seconds() / 60.0
        if elapsed >= 15.0 and "leverage_29" not in self.deductions_applied:
            self.risk_discipline_score = max(0.0, self.risk_discipline_score - 30)
            self.deductions_applied.add("leverage_29")
    else:
        self.leverage_29_start = None
        self.deductions_applied.discard("leverage_29")

    # --- Concentration Violations --- [1]
    if max_concentration > 0.90 and leverage > 1.0:
        if self.concentration_90_start is None: self.concentration_90_start = current_time
        elapsed = (current_time - self.concentration_90_start).total_seconds() / 60.0
        if elapsed >= 30.0 and "concentration_90" not in self.deductions_applied:
            self.risk_discipline_score = max(0.0, self.risk_discipline_score - 10)
            self.deductions_applied.add("concentration_90")
    else:
        self.concentration_90_start = None
        self.deductions_applied.discard("concentration_90")

def validate_trade(self, account: AccountState, asset: str, trade_size: float, current_time) -> bool:
    if not self.check_rate_limit():
        return False
        
    if current_time.hour == 21 and current_time.minute >= 50:
        return False
        
    if not self.is_session_liquid(asset, current_time):
        return False

    drawdown, leverage, margin_usage = self.calculate_metrics(account, current_time)
    if drawdown >= self.HARD_DRAWDOWN_LIMIT:
        return False

    asset_clean = asset.replace("/", "").replace("_", "")
    is_crypto = any(c in asset_clean for c in ["BTC", "ETH", "SOL", "XRP", "BAR"])
    is_metal = any(m in asset_clean for m in ["XAU", "XAG"])
    asset_class = "CRYPTO" if is_crypto else ("METALS" if is_metal else "FOREX")

    current_asset_exposure = account.asset_exposures.get(asset_clean, 0.0)
    projected_asset_exposure = current_asset_exposure + trade_size
    projected_gross_exposure = account.gross_exposure + trade_size
    
    if account.equity <= 0:
        return False
        
    projected_leverage = projected_gross_exposure / account.equity
    projected_concentration = projected_asset_exposure / projected_gross_exposure if projected_gross_exposure > 0 else 0.0
    
    required_margin_rate = self.margin_rates.get(asset_class, 0.0333)
    projected_used_margin = account.used_margin + (trade_size * required_margin_rate)
    projected_margin_usage = projected_used_margin / account.equity
    
    if projected_margin_usage > 0:
        projected_margin_level = account.equity / projected_used_margin
        if projected_margin_level <= 0.40:  
            return False

    limit = self.max_leverage_limits.get(asset_clean, self.max_leverage_limits["FOREX"] if asset_class == "FOREX" else 1.0)
    if projected_leverage > limit:
        return False

    if projected_leverage >= 29.5 or projected_margin_usage >= 0.97:
        return False

    return True

def get_sharpe_ratio(self) -> float:
    return calculate_standalone_sharpe(self.equity_history_15m)
alpha_agent.py:
alpha_agent.py
import sys
import os
Ensure Python looks in the current directory for the strategies package
current_dir = os.path.dirname(os.path.abspath(file))
if current_dir not in sys.path:
sys.path.append(current_dir)
from strategies.bot1 import Bot1
from strategies.bot2 import Bot2
from strategies.bot3 import Bot3
from strategies.bot4 import Bot4
from strategies.bot5 import Bot5
class FiveBotAlphaCouncil:
def init(self):
self.price_histories = {} # {symbol: [list of historical prices]}
self.bot1 = Bot1()
self.bot2 = Bot2()
self.bot3 = Bot3()
self.bot4 = Bot4()
self.bot5 = Bot5()
code
Code
def update_price(self, symbol: str, mid_price: float):
    """Maintains price history records sequentially."""
    if symbol not in self.price_histories:
        self.price_histories[symbol] = []
    self.price_histories[symbol].append(mid_price)
    
    # Limit history length to 100 to prevent memory leaks [1]
    if len(self.price_histories[symbol]) > 100:
        self.price_histories[symbol].pop(0)

def evaluate_market(self, row, symbol: str) -> dict:
    mid_price = (float(row['bid']) + float(row['ask'])) / 2.0
    history = self.price_histories.get(symbol, [])
    
    # Gather votes from individual bot classes
    v1 = self.bot1.evaluate(row)
    v2 = self.bot2.evaluate(history)
    v3 = self.bot3.evaluate(mid_price, history)
    v4 = self.bot4.evaluate(history)
    
    # Compile latest mid prices for the lead-lag calculations [1]
    current_prices = {}
    for sym, hist in self.price_histories.items():
        if hist:
            current_prices[sym] = hist[-1]
            
    v5 = self.bot5.evaluate(symbol, current_prices, self.price_histories)
    
    votes = {"Bot1": v1, "Bot2": v2, "Bot3": v3, "Bot4": v4, "Bot5": v5}
    vote_values = list(votes.values())
    buy_count = vote_values.count("BUY")
    sell_count = vote_values.count("SELL")
    
    final_signal = "HOLD"
    vote_strength = 0
    
    # Consensus gate: requires a majority of 3+ agreement [1]
    if buy_count >= 3 and buy_count > sell_count:
        final_signal = "BUY"
        vote_strength = buy_count
    elif sell_count >= 3 and sell_count > buy_count:
        final_signal = "SELL"
        vote_strength = sell_count
        
    return {
        "signal": final_signal,
        "vote_strength": vote_strength,
        "votes": votes
    }
main.py:
import os
import glob
import pandas as pd
import numpy as np
import logfire
from alpha_agent import FiveBotAlphaCouncil
from risk_agent import AssetRiskGuard, AccountState
==============================================================================
PERFORMANCE CONFIGURATION
Set to 10 for high resolution. Increase to 50 or 100 if your computer runs out of RAM.
==============================================================================
DOWNSAMPLE_STEP = 100
Configure Logfire
logfire.configure(
token="pylf_v1_eu_zwcrVr8W6Lq9FYfGFLcbP1kr3VmcL6kyJdTqpbZNNhMp",
console=logfire.ConsoleOptions(min_log_level="notice")
)
logfire.instrument_pydantic()
ALLOWED_ASSETS = [
"AUDUSD", "EURCHF", "EURGBP", "EURUSD", "GBPUSD", "USDCAD", "USDCHF", "USDJPY",
"XAGUSD", "XAUUSD",
"BARUSD", "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
]
def load_and_preprocess_file(file_path: str, asset_name: str, downsample_step: int, params: dict = None) -> pd.DataFrame:
"""
Optimized loader: Filters provider and downsamples IMMEDIATELY.
Calculates technical features vectorized across the series before looping.
"""
try:
raw_df = pd.read_parquet(file_path, engine='pyarrow')
except Exception:
return None
if raw_df.empty:
return None
code
Code
df_cleaned = raw_df[raw_df['provider'] == 'XSMM01CH01'].copy()
if df_cleaned.empty:
    return None
    
# Downsample immediately to reduce raw row processing load
df_down = df_cleaned.iloc[::downsample_step].copy()

# Process 5-tier level arrays
for i in range(5):
    try:
        df_down[f'bid_price_lvl_{i+1}'] = df_down['bidprices'].str[i].astype(float)
        df_down[f'bid_size_lvl_{i+1}']  = df_down['bidsizes'].str[i].astype(float)
        df_down[f'ask_price_lvl_{i+1}'] = df_down['askprices'].str[i].astype(float)
        df_down[f'ask_size_lvl_{i+1}']  = df_down['asksizes'].str[i].astype(float)
    except Exception:
        # Fallback values if level values are missing
        df_down[f'bid_price_lvl_{i+1}'] = np.nan
        df_down[f'bid_size_lvl_{i+1}']  = 0.0
        df_down[f'ask_price_lvl_{i+1}'] = np.nan
        df_down[f'ask_size_lvl_{i+1}']  = 0.0
        
total_bid_depth = df_down[[f'bid_size_lvl_{j}' for j in range(1, 6)]].sum(axis=1)
total_ask_depth = df_down[[f'ask_size_lvl_{j}' for j in range(1, 6)]].sum(axis=1)
df_down['book_imbalance'] = (total_bid_depth - total_ask_depth) / (total_bid_depth + total_ask_depth + 1e-8)

df_down['assigned_symbol'] = asset_name
df_down['mid_price'] = (df_down['bid'].astype(float) + df_down['ask'].astype(float)) / 2.0

# Extract operational parameter overrides
bot1_thresh = params.get("bot1_threshold", 0.35) if params else 0.35
bot3_thresh = params.get("bot3_z_threshold", 2.5) if params else 2.5

# Pre-calculate Bot 1 Signals
df_down['bot1_vote'] = 'HOLD'
df_down.loc[df_down['book_imbalance'] > bot1_thresh, 'bot1_vote'] = 'BUY'
df_down.loc[df_down['book_imbalance'] < -bot1_thresh, 'bot1_vote'] = 'SELL'

# Pre-calculate Bot 2 Signals
fast_ma_2 = df_down['mid_price'].rolling(5, min_periods=5).mean()
slow_ma_2 = df_down['mid_price'].rolling(15, min_periods=15).mean()
recent_std_2 = df_down['mid_price'].rolling(20, min_periods=20).std().fillna(0)
prev_std_2 = recent_std_2.shift(1).fillna(0)

df_down['bot2_vote'] = 'HOLD'
vol_expansion = recent_std_2 > prev_std_2
df_down.loc[vol_expansion & (fast_ma_2 > slow_ma_2), 'bot2_vote'] = 'BUY'
df_down.loc[vol_expansion & (fast_ma_2 < slow_ma_2), 'bot2_vote'] = 'SELL'

# Pre-calculate Bot 3 Signals
mean_30 = df_down['mid_price'].rolling(30, min_periods=30).mean()
std_30 = df_down['mid_price'].rolling(30, min_periods=30).std().fillna(0)
std_30_safe = std_30.replace(0, 1e-8)
z_score = (df_down['mid_price'] - mean_30) / std_30_safe

df_down['bot3_vote'] = 'HOLD'
df_down.loc[z_score < -bot3_thresh, 'bot3_vote'] = 'BUY'
df_down.loc[z_score > bot3_thresh, 'bot3_vote'] = 'SELL'

# Pre-calculate Bot 4 Signals
fast_ma_4 = df_down['mid_price'].rolling(10, min_periods=10).mean()
slow_ma_4 = df_down['mid_price'].rolling(30, min_periods=30).mean()

df_down['bot4_vote'] = 'HOLD'
df_down.loc[fast_ma_4 > slow_ma_4, 'bot4_vote'] = 'BUY'
df_down.loc[fast_ma_4 < slow_ma_4, 'bot4_vote'] = 'SELL'

return df_down
def get_sorted_trading_days(data_dir: str) -> list:
all_files = glob.glob(os.path.join(data_dir, "*.parquet"))
unique_dates = set()
for f in all_files:
base = os.path.basename(f)
# Fixes split pattern typo from previous script
parts = base.replace(".parquet", "").split("")
if len(parts) >= 4:
date_str = f"{parts[-3]}{parts[-2]}_{parts[-1]}"
unique_dates.add(date_str)
return sorted(list(unique_dates))
==========================================
3. BACKTEST RUNNER (COMPOSITE METRIC ENGINE)
==========================================
def run_backtest_on_days(target_days: list, data_dir: str, council_params: dict = None) -> dict:
council = FiveBotAlphaCouncil()
guard = AssetRiskGuard()
my_account = AccountState(equity=1000000.0, used_margin=0.0, gross_exposure=0.0)
initial_equity = my_account.equity
code
Code
portfolio_positions = {asset: None for asset in ALLOWED_ASSETS}
trade_size_cash = 1000000.0
all_files = sorted(glob.glob(os.path.join(data_dir, "*.parquet")))

for target_day in target_days:
    print(f"     Processing market data for day: {target_day}...", flush=True)
    day_files = [f for f in all_files if target_day in f]
    day_dfs = []
    
    for file_path in day_files:
        file_name = os.path.basename(file_path)
        asset_name = next((a for a in ALLOWED_ASSETS if a in file_name.replace("_", "")), None)
        if not asset_name:
            continue
        
        df_clean = load_and_preprocess_file(file_path, asset_name, DOWNSAMPLE_STEP, council_params)
        if df_clean is not None and not df_clean.empty:
            day_dfs.append(df_clean)

    if not day_dfs:
        continue
        
    master_day_stream = pd.concat(day_dfs, axis=0, ignore_index=True)
    master_day_stream['time'] = pd.to_datetime(master_day_stream['time'])
    master_day_stream = master_day_stream.sort_values(by='time').reset_index(drop=True)
    
    # Fast streaming loop
    for _, row in master_day_stream.iterrows():
        symbol = row['assigned_symbol']
        mid_price = row['mid_price']
        
        # Maintain real-time price state for lead-lag checks
        council.update_price(symbol, mid_price)
        
        # Continuously monitor compliance and drawdown metrics [1]
        guard.evaluate_compliance_violations(my_account, row['time'])
        
        active_trade = portfolio_positions[symbol]
        
        # --- EVALUATE EXITS ---
        if active_trade is not None:
            current_pnl = active_trade['pos_size'] * (mid_price - active_trade['entry_price'])
            my_account.equity = initial_equity + current_pnl
            
            direction_mult = 1 if active_trade['direction'] == "BUY" else -1
            current_return = direction_mult * (mid_price - active_trade['entry_price']) / active_trade['entry_price']
            
            if current_return >= 0.002 or current_return <= -0.001:
                initial_equity += current_pnl
                my_account.equity = initial_equity
                my_account.gross_exposure -= trade_size_cash
                portfolio_positions[symbol] = None
                continue

        # --- EVALUATE ENTRIES ---
        if portfolio_positions[symbol] is None:
            if not guard.is_session_liquid(symbol, row['time']):
                continue
                
            analysis = council.evaluate_market(row, symbol)
            signal = analysis.get("signal")
            
            if signal in ["BUY", "SELL"]:
                is_safe = guard.validate_trade(my_account, symbol, trade_size_cash, row['time'])
                if is_safe:
                    pos_size = (trade_size_cash / mid_price) if signal == "BUY" else -(trade_size_cash / mid_price)
                    portfolio_positions[symbol] = {
                        'entry_price': mid_price,
                        'pos_size': pos_size,
                        'direction': signal
                    }
                    my_account.gross_exposure += trade_size_cash
                    
total_return = (my_account.equity - 1000000.0) / 1000000.0
sharpe = guard.get_sharpe_ratio()

return {
    "total_return": total_return,
    "max_drawdown": guard.max_drawdown,
    "sharpe_ratio": sharpe,
    "risk_discipline": guard.risk_discipline_score
}
==========================================
4. SURROGATE SCORING FUNCTION
==========================================
def calculate_surrogate_score(metrics: dict) -> float:
ret = metrics["total_return"]
dd = metrics["max_drawdown"]
sharpe = metrics["sharpe_ratio"]
risk = metrics["risk_discipline"]
code
Code
s_return = min(100.0, max(0.0, (ret / 0.05) * 100.0))
s_drawdown = max(0.0, 100.0 - (dd / 0.14) * 100.0) 
s_sharpe = min(100.0, max(0.0, (sharpe / 1.5) * 100.0))
s_risk = risk 

composite_score = (0.70 * s_return) + (0.15 * s_drawdown) + (0.10 * s_sharpe) + (0.05 * s_risk)
return composite_score
==========================================
5. CROSS-VALIDATION ORCHESTRATION
==========================================
def run_cross_validation(data_dir: str):
trading_days = get_sorted_trading_days(data_dir)
num_days = len(trading_days)
code
Code
if num_days < 15:
    print("Error: Insufficient trading data to run walk-forward validation.")
    return
    
print(f"Parsed {num_days} unique trading days.")

fold1_train = trading_days[0:14]
fold1_test = trading_days[14:21]

fold2_train = trading_days[0:21]
fold2_test = trading_days[21:]

param_grid = [
    {"bot1_threshold": 0.35, "bot3_z_threshold": 2.0},
    {"bot1_threshold": 0.45, "bot3_z_threshold": 2.5}
]

oos_results = []

# --- FOLD 1 ---
print("\n--- Running Fold 1 Training (Composite Score Search) ---")
best_f1_params = None
best_f1_score = -999.0

for params in param_grid:
    metrics = run_backtest_on_days(fold1_train, data_dir, council_params=params)
    score = calculate_surrogate_score(metrics)
    print(f"Params: {params} | OOS Surrogate Score: {score:.2f} | (Ret: {metrics['total_return']*100:.2f}%, DD: {metrics['max_drawdown']*100:.2f}%, Sharpe: {metrics['sharpe_ratio']:.3f}, Risk: {metrics['risk_discipline']})")
    if score > best_f1_score:
        best_f1_score = score
        best_f1_params = params
        
print(f"Fold 1 Optimal Params: {best_f1_params}")
f1_test_res = run_backtest_on_days(fold1_test, data_dir, council_params=best_f1_params)
f1_test_score = calculate_surrogate_score(f1_test_res)
oos_results.append(f1_test_res)
print(f"Fold 1 OOS Result -> Surrogate Score: {f1_test_score:.2f} | Return: {f1_test_res['total_return']*100:.2f}% | MaxDD: {f1_test_res['max_drawdown']*100:.2f}%")

# --- FOLD 2 ---
print("\n--- Running Fold 2 Training (Composite Score Search) ---")
best_f2_params = None
best_f2_score = -999.0

for params in param_grid:
    metrics = run_backtest_on_days(fold2_train, data_dir, council_params=params)
    score = calculate_surrogate_score(metrics)
    print(f"Params: {params} | OOS Surrogate Score: {score:.2f} | (Ret: {metrics['total_return']*100:.2f}%, DD: {metrics['max_drawdown']*100:.2f}%, Sharpe: {metrics['sharpe_ratio']:.3f}, Risk: {metrics['risk_discipline']})")
    if score > best_f2_score:
        best_f2_score = score
        best_f2_params = params
        
print(f"Fold 2 Optimal Params: {best_f2_params}")
f2_test_res = run_backtest_on_days(fold2_test, data_dir, council_params=best_f2_params)
f2_test_score = calculate_surrogate_score(f2_test_res)
oos_results.append(f2_test_res)
print(f"Fold 2 OOS Result -> Surrogate Score: {f2_test_score:.2f} | Return: {f2_test_res['total_return']*100:.2f}% | MaxDD: {f2_test_res['max_drawdown']*100:.2f}%")

# --- AGGREGATE EVALUATION ---
avg_oos_return = np.mean([r['total_return'] for r in oos_results])
avg_oos_drawdown = np.mean([r['max_drawdown'] for r in oos_results])
avg_oos_sharpe = np.mean([r['sharpe_ratio'] for r in oos_results])
avg_oos_risk = np.mean([r['risk_discipline'] for r in oos_results])

final_aggregate_metrics = {
    "total_return": avg_oos_return,
    "max_drawdown": avg_oos_drawdown,
    "sharpe_ratio": avg_oos_sharpe,
    "risk_discipline": avg_oos_risk
}
final_aggregate_score = calculate_surrogate_score(final_aggregate_metrics)

print("\n==============================================")
print("      WALK-FORWARD COMPOSITE OOS SUMMARY      ")
print("==============================================")
print(f"Overall Walk-Forward Score: {final_aggregate_score:.2f} / 100.00")
print(f"Average Out-of-Sample Return: {avg_oos_return*100:.2f}%")
print(f"Average Out-of-Sample Max Drawdown: {avg_oos_drawdown*100:.2f}%")
print(f"Average Out-of-Sample Sharpe Ratio: {avg_oos_sharpe:.4f}")
print(f"Average Out-of-Sample Risk Score: {avg_oos_risk:.1f} / 100")
print("==============================================")
if name == "main":
DATA_DIRECTORY = "pricer-output-2026-05-11_2026-06-10"
run_cross_validation(DATA_DIRECTORY)
9.main_live.py
import time
import json
import os
import pandas as pd  # <--- ADD THIS LINE HERE
import MetaTrader5 as mt5
import logfire
from alpha_agent import FiveBotAlphaCouncil
from risk_agent import AssetRiskGuard, AccountState
Configure Logfire for live monitoring [1]
logfire.configure(
token="pylf_v1_eu_zwcrVr8W6Lq9FYfGFLcbP1kr3VmcL6kyJdTqpbZNNhMp",
console=logfire.ConsoleOptions(min_log_level="notice")
)
logfire.instrument_pydantic()
ALLOWED_ASSETS = [
"AUDUSD", "EURCHF", "EURGBP", "EURUSD", "GBPUSD", "USDCAD", "USDCHF", "USDJPY",
"XAGUSD", "XAUUSD",
"BARUSD", "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
]
SENTIMENT_FILE = "sentiment_regime.json"
def load_sentiment_bias() -> str:
"""Reads the background sentiment file generated by your Northflank cron job [1]."""
if os.path.exists(SENTIMENT_FILE):
try:
with open(SENTIMENT_FILE, "r") as f:
data = json.load(f)
return data.get("bias", "NEUTRAL")
except Exception:
pass
return "NEUTRAL"
def execute_mt5_order(symbol: str, action: str, volume: float, price: float, comment: str = ""):
"""Submits a market execution order directly to the MetaTrader 5 terminal [1]."""
# Map actions to MT5 action types
order_type = mt5.ORDER_TYPE_BUY if action == "BUY" else mt5.ORDER_TYPE_SELL
code
Code
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": volume,
    "type": order_type,
    "price": price,
    "deviation": 20, # Max slippage allowed in points [1]
    "magic": 123456, # Unique identifier for your bot council [1]
    "comment": comment,
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC, # Immediate-or-Cancel to prevent partial fills [1]
}

# Send transaction
result = mt5.order_send(request)
if result.retcode != mt5.TRADE_RETCODE_DONE:
    logfire.error("MT5 Order Failed", symbol=symbol, action=action, error=result.comment, retcode=result.retcode)
    print(f"❌ MT5 Order Failed for {symbol}: {result.comment}")
else:
    logfire.notice("MT5 Order Executed Successfully", symbol=symbol, action=action, price=result.price, volume=volume)
    print(f"🎯 Successful {action} order executed on {symbol} at {result.price}")
return result
def live_trading_loop():
print("==================================================")
print("      QUANTBOT METATRADER 5 LIVE ORCHESTRATOR     ")
print("==================================================")
code
Code
# 1. Initialize connection to MT5 terminal
if not mt5.initialize():
    print(f"❌ MT5 Initialization failed: {mt5.last_error()}")
    return
    
print("✅ Successfully linked to MetaTrader 5 terminal.")

council = FiveBotAlphaCouncil()
guard = AssetRiskGuard()

# Keep track of active positions locally to avoid redundant API calls
local_positions = {asset: None for asset in ALLOWED_ASSETS}

try:
    while True:
        # Read global macro sentiment to dynamically skew decision parameters [1]
        sentiment_bias = load_sentiment_bias()
        
        # Apply sentiment skew to Alpha Council thresholds
        if sentiment_bias == "BULLISH":
            # Loosen the threshold to buy, tighten to sell
            council.bot1_threshold = 0.25 
        elif sentiment_bias == "BEARISH":
            council.bot1_threshold = 0.45 
        else:
            council.bot1_threshold = 0.35 # Default
        
        # 2. Sync account balance metrics live with the terminal
        acct = mt5.account_info()
        if acct is None:
            print("⚠️ Failed to fetch live account details from MT5.")
            time.sleep(1)
            continue
            
        # Populate our standard AccountState object
        current_state = AccountState(
            equity=acct.equity,
            used_margin=acct.margin,
            gross_exposure=acct.margin_initial # Proxy or sum of asset exposures
        )
        
        # 3. Process each instrument chronologically
        for symbol in ALLOWED_ASSETS:
            # Fetch tick data live from Symphonix gateway [1]
            tick = mt5.symbol_info_tick(symbol)
            if tick is None:
                continue
                
            mid_price = (tick.bid + tick.ask) / 2.0
            council.update_price(symbol, mid_price)
            
            # Check current open positions in MT5 for this asset
            positions = mt5.positions_get(symbol=symbol)
            
            # --- EXIT EVALUATION ---
            if positions:
                pos = positions[0] # Assume one position per asset for simplicity
                entry_price = pos.price_open
                direction = "BUY" if pos.type == mt5.POSITION_TYPE_BUY else "SELL"
                
                # Calculate percentage return
                if direction == "BUY":
                    current_return = (mid_price - entry_price) / entry_price
                else:
                    current_return = (entry_price - mid_price) / entry_price
                    
                # Rule-based Profit Target (+0.2%) or Stop Loss (-0.1%) [1]
                if current_return >= 0.002 or current_return <= -0.001:
                    close_action = "SELL" if direction == "BUY" else "BUY"
                    print(f"🛑 [Exit Signal] Closing {symbol} position...")
                    execute_mt5_order(symbol, close_action, pos.volume, mid_price, comment="Exit Bracket")
                    
            # --- ENTRY EVALUATION ---
            else:
                # Construct a mock row dictionary to mimic raw data format for your bots
                mock_row = {
                    'bid': tick.bid,
                    'ask': tick.ask,
                    'book_imbalance': 0.0, # We can replace with live book depth if available [1]
                    'bot1_vote': 'HOLD',
                    'bot2_vote': 'HOLD',
                    'bot3_vote': 'HOLD',
                    'bot4_vote': 'HOLD'
                }
                
                # Since we are live, we compute indicators online or use a fast tick window
                # Evaluating the Alpha Council decision
                analysis = council.evaluate_market(mock_row, symbol)
                signal = analysis.get("signal")
                
                if signal in ["BUY", "SELL"]:
                    trade_size_cash = 1000000.0 # Standard size from backtest [1]
                    
                    # Verify safe parameters with the Risk Agent before execution
                    current_time = pd.Timestamp.now()
                    is_safe = guard.validate_trade(current_state, symbol, trade_size_cash, current_time)
                    
                    if is_safe:
                        trade_volume = trade_size_cash / mid_price
                        # Normalize volume to MT5 contract sizes (lot sizes) if needed [1]
                        # For standard Forex, $1,000,000 exposure is roughly 10 standard lots [1]
                        mt5_lot_size = round(trade_volume / 100000, 2) 
                        
                        if mt5_lot_size > 0:
                            print(f"🚀 [Entry Signal] Executing {signal} for {symbol}...")
                            execute_mt5_order(symbol, signal, mt5_lot_size, mid_price, comment="Alpha Council Consensus")
        
        # Control loop frequency to limit processing overhead [1]
        time.sleep(1) 
        
except KeyboardInterrupt:
    print("\nStopping Live Execution Bridge...")
finally:
    mt5.shutdown()
    print("MetaTrader 5 connection closed.")
if name == "main":
live_trading_loop()
Model 12:05 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
Your existing code is well-structured for a backtesting-to-live pipeline. However, before setting up the Market Watch system, we should address a few critical issues in the code that would prevent your live trading system from behaving as intended.
Part 1: Critical Code Review & Improvements
1. The bot1_threshold Linkage Bug
In main_live.py, you adjust the threshold based on sentiment like this:
code
Python
if sentiment_bias == "BULLISH":
    council.bot1_threshold = 0.25
However, in alpha_agent.py, FiveBotAlphaCouncil initializes self.bot1 = Bot1(). The Bot1 class reads self.threshold during execution. Modifying council.bot1_threshold creates a new unused attribute on the council object; it does not update the actual bot threshold.
Fix: Update FiveBotAlphaCouncil to forward this threshold, or change main_live.py to target the bot directly:
code
Python
council.bot1.threshold = 0.25 if sentiment_bias == "BULLISH" else ...
2. Live Order Book Imbalance (Bot 1)
In main_live.py, you pass mock_row with a hardcoded 'book_imbalance': 0.0.
Because Bot 1 checks if imbalance > threshold (where threshold is 0.25 to 0.45), an imbalance of 0.0 means Bot 1 will always vote "HOLD" in live trading.
Fix: If MT5 order book depth is available, you can calculate live imbalance. If not, Bot 1 should gracefully fall back or be bypassed in the live council if order book data is missing.
3. Vectorized Pre-calculations vs. Sequential State in Backtesting
In main.py, you pre-calculate technical features across the entire dataframe before running the chronological loop. This is excellent for backtesting speed, but it means council.evaluate_market in main.py is called with historical indicators already populated in the row. In main_live.py, those pre-calculated columns do not exist on your mock_row.
Ensure that FiveBotAlphaCouncil relies purely on self.price_histories (which is updated sequentially) or live-calculated metrics so that the live behavior matches the backtest.
Part 2: Async Market Watch System Architecture
To ensure your 
50
A
n
t
h
r
o
p
i
c
c
r
e
d
i
t
∗
∗
a
n
d
∗
∗
50Anthropiccredit∗∗and∗∗
50 Pydantic/Logfire credit last the entire competition while processing news for 15 assets, we will design a Two-Tier Triage Pipeline:
code
Code
[News Ingestion: RSS/APIs] 
       │
       ▼ (Async Queue)
[Tier 1: Triage (Nvidia Nemotron 3 Nano)]  <-- Extremely cheap / high speed
       │ (Filters out noise. Only proceeds if high-impact & targets our 15 assets)
       ▼
[Tier 2: Deep Analysis (Anthropic Claude)] <-- Higher reasoning / structured output
       │ (Extracts exact Pydantic schema: Sentiment, Impact Score, Justification)
       ▼
[JSON State: sentiment_regime.json] + [Logfire Trace Spans]
We will implement this as a standalone background worker (market_watch.py) that you can deploy on Northflank using your $100 credit. It will output to sentiment_regime.json (or a shared volume/API endpoint) which main_live.py will read.
Part 3: Step-by-Step Implementation
First, let's create the Pydantic structures and the async orchestrator.
Step 1: Define the Pydantic Schema (schemas.py)
This ensures our unstructured data is transformed into structured, predictable data using pydantic and logfire.
code
Python
# schemas.py
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from datetime import datetime

class AssetSentiment(BaseModel):
    asset: Literal[
        "AUDUSD", "EURCHF", "EURGBP", "EURUSD", "GBPUSD", "USDCAD", "USDCHF", "USDJPY",
        "XAGUSD", "XAUUSD", "BARUSD", "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
    ] = Field(..., description="The specific standard trading asset impacted by the news.")
    sentiment: Literal["BULLISH", "BEARISH", "NEUTRAL"] = Field(
        ..., description="The directional sentiment classification for this asset."
    )
    impact_score: float = Field(
        ..., ge=0.0, le=1.0, description="The quantitative impact weight where 1.0 is extreme volatility."
    )
    justification: str = Field(
        ..., description="Brief 1-sentence reasoning linking the news directly to the asset."
    )

class MarketWatchPayload(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    primary_bias: Literal["BULLISH", "BEARISH", "NEUTRAL"] = Field(
        ..., description="Overall market consensus derived from this batch of news."
    )
    impacted_assets: List[AssetSentiment] = Field(
        default_factory=list, description="A list of specific assets with clear, direct directional impact."
    )
Step 2: Implement the Async Market Watch (market_watch.py)
This script uses aiohttp to fetch news, uses the cheap LLM for triage, uses Anthropic Claude for high-value structured extractions, and logs everything to Logfire.
code
Python
# market_watch.py
import asyncio
import aiohttp
import xml.etree.ElementTree as ET
import json
import os
from datetime import datetime
import logfire
from openai import AsyncOpenAI  # For Nvidia/Doublewood endpoints
from anthropic import AsyncAnthropic
from schemas import MarketWatchPayload

# Configure Logfire using your credentials
logfire.configure(
    token="pylf_v1_eu_zwcrVr8W6Lq9FYfGFLcbP1kr3VmcL6kyJdTqpbZNNhMp",
    console=logfire.ConsoleOptions(min_log_level="notice")
)

# API Clients Configuration
# Doublewood / Nvidia Nemotron 3 Nano configuration (using OpenAI-compatible SDK)
TRIAGE_CLIENT = AsyncOpenAI(
    base_url="https://api.nvidia.com/v1", # Replace with your Doublewood/Nvidia base URL
    api_key=os.environ.get("NVIDIA_API_KEY", "your-nvidia-key")
)

ANTHROPIC_CLIENT = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY", "your-claude-key")
)

# Target assets to filter
TARGET_ASSETS = [
    "AUDUSD", "EURCHF", "EURGBP", "EURUSD", "GBPUSD", "USDCAD", "USDCHF", "USDJPY",
    "XAGUSD", "XAUUSD", "BARUSD", "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
]

# RSS News Feeds to Watch
FEEDS = [
    "https://www.forexlive.com/Feed",
    "https://feed.cryptopanic.com/posts/?key=YOUR_FREE_API_KEY", # If using Cryptopanic
    "https://news.google.com/rss/search?q=forex+crypto+gold&hl=en-US&gl=US&ceid=US:en"
]

SENTIMENT_FILE = "sentiment_regime.json"

async def fetch_rss_feed(session: aiohttp.ClientSession, url: str) -> list[dict]:
    """Asynchronously fetches and parses RSS feed items."""
    try:
        async with session.get(url, timeout=10) as response:
            if response.status != 200:
                return []
            xml_data = await response.text()
            root = ET.fromstring(xml_data)
            
            articles = []
            for item in root.findall(".//item"):
                title = item.find("title")
                description = item.find("description")
                link = item.find("link")
                
                articles.append({
                    "title": title.text if title is not None else "",
                    "description": description.text if description is not None else "",
                    "link": link.text if link is not None else ""
                })
            return articles
    except Exception as e:
        logfire.warn("Failed to fetch RSS feed", url=url, error=str(e))
        return []

async def check_triage_relevance(article: dict) -> bool:
    """
    Tier 1 Triage using Nvidia Nemotron 3 Nano.
    Filters out noise cheaply. Returns True if highly relevant to our 15 assets.
    """
    text_content = f"Title: {article['title']}\nDescription: {article['description']}"
    
    prompt = f"""
    Analyze this financial news story. Determine if it has high-impact, immediate trading relevance to any of the following assets:
    {', '.join(TARGET_ASSETS)}
    
    Respond with exactly 'YES' if it directly affects their prices or represents structural macroeconomic shifts (e.g., central bank rates, major technical breaches, geopolitical shock).
    Respond with 'NO' if it is minor, educational, general commentary, or unrelated.
    
    Content:
    {text_content}
    
    Decision:
    """
    try:
        response = await TRIAGE_CLIENT.chat.completions.create(
            model="nvidia/nemotron-3-8b-nano", # Adjust based on precise partner model name
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
            temperature=0.0
        )
        decision = response.choices[0].message.content.strip().upper()
        return "YES" in decision
    except Exception as e:
        logfire.error("Triage classification failed, passing to Tier 2 by default", error=str(e))
        return True # Default to safe-harbor processing

async def extract_structured_sentiment(relevant_articles: list[dict]) -> Optional[MarketWatchPayload]:
    """
    Tier 2 Deep Analysis using Anthropic Claude.
    Extracts structured directional data.
    """
    if not relevant_articles:
        return None
        
    combined_content = "\n\n".join([
        f"Article {i+1}:\nTitle: {a['title']}\nDesc: {a['description']}" 
        for i, a in enumerate(relevant_articles)
    ])
    
    prompt = f"""
    You are a professional quantitative macro research assistant. 
    Analyze this batch of highly-curated financial news stories:
    
    {combined_content}
    
    Identify which specific assets from {TARGET_ASSETS} are directly impacted and specify the direction (BULLISH, BEARISH, NEUTRAL), impact score (0.0 to 1.0), and a brief justification.
    Provide an overall primary market bias (BULLISH, BEARISH, or NEUTRAL) for the entire trading desk.
    """
    
    try:
        # Use Anthropic's tool use / structured output framework
        with logfire.span("Anthropic Structured Extraction"):
            response = await ANTHROPIC_CLIENT.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                temperature=0.0,
                system="You extract highly-accurate structured economic signals for a quant portfolio.",
                messages=[{"role": "user", "content": prompt}],
                tools=[{
                    "name": "submit_market_analysis",
                    "description": "Submit structured sentiment outputs.",
                    "input_schema": MarketWatchPayload.model_json_schema()
                }],
                tool_choice={"type": "tool", "name": "submit_market_analysis"}
            )
            
            # Extract JSON tool input
            tool_input = response.content[0].input if hasattr(response.content[0], 'input') else response.content[1].input
            parsed_payload = MarketWatchPayload(**tool_input)
            return parsed_payload
    except Exception as e:
        logfire.error("Claude structured sentiment extraction failed", error=str(e))
        return None

async def run_market_watch_cycle():
    """Main execution loop for one watch interval."""
    async with aiohttp.ClientSession() as session:
        # Fetch news from all sources in parallel
        tasks = [fetch_rss_feed(session, url) for url in FEEDS]
        results = await asyncio.gather(*tasks)
        
        # Flatten articles list
        all_articles = [article for feed_res in results for article in feed_res]
        if not all_articles:
            return
            
        # Run Tier 1 Triage in parallel
        triage_tasks = [check_triage_relevance(art) for art in all_articles]
        triage_results = await asyncio.gather(*triage_tasks)
        
        relevant_articles = [
            art for art, is_relevant in zip(all_articles, triage_results) if is_relevant
        ]
        
        logfire.notice(
            "Triage complete", 
            total_fetched=len(all_articles), 
            total_relevant=len(relevant_articles)
        )
        
        # Run Tier 2 Structured Extraction on verified articles only
        if relevant_articles:
            # We can batch them in chunks of 5 to protect context windows and control latency
            analysis = await extract_structured_sentiment(relevant_articles[:5])
            if analysis:
                # Write results to share state with live execution bridge
                with open(SENTIMENT_FILE, "w") as f:
                    json.dump({
                        "bias": analysis.primary_bias,
                        "timestamp": analysis.timestamp.isoformat(),
                        "assets": [a.model_dump() for a in analysis.impacted_assets]
                    }, f, indent=4)
                
                logfire.notice(
                    "Global sentiment bias state updated", 
                    bias=analysis.primary_bias, 
                    impacted_assets_count=len(analysis.impacted_assets)
                )

async def main_loop():
    print("📢 Starting Market Watch Background Process...")
    while True:
        try:
            await run_market_watch_cycle()
        except Exception as e:
            logfire.error("Error in Market Watch loop iteration", error=str(e))
        
        # Check every 5 minutes to remain highly responsive while keeping API costs low
        await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.run(main_loop())
Part 4: Adjusting Your Live Trading Bridge
Now we can implement the fixes directly into your main_live.py to securely read the updated sentiment_regime.json and cleanly skew the thresholds of Bot 1 and others.
Updated Live Orchestrator Snippet (main_live.py)
code
Python
# Read global macro sentiment to dynamically skew decision parameters [1]
            sentiment_bias = load_sentiment_bias()
            
            # FIXED: Target the actual bot instance attributes directly, not the council object
            if sentiment_bias == "BULLISH":
                # Loosen the threshold to buy, tighten to sell
                council.bot1.threshold = 0.25 
                council.bot3.z_threshold = 2.8  # Harder to trigger a mean-reverting sell
            elif sentiment_bias == "BEARISH":
                council.bot1.threshold = 0.45 
                council.bot3.z_threshold = 2.2  # Easier to trigger a mean-reverting sell
            else:
                council.bot1.threshold = 0.35 # Default
                council.bot3.z_threshold = 2.5 # Default
Key Structural Improvements Made:
Budget Protection: The Triage Phase uses the cheap, ultra-low-cost Nemotron 3 Nano model to strip out non-consequential noise. Only macro-critical, high-impact asset news reaches your Claude 3.5 Sonnet limit. This will easily allow your $50 credentials to last the 5 days of competition.
Pydantic Validation: The extraction process relies directly on Pydantic's JSON schema rendering features, ensuring structured output execution without formatting syntax errors.
Trace Monitoring: Wrapped crucial execution boundaries with logfire.span to trace any failure points transparently.
Model 12:09 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
Model 12:10 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
Yes, you absolutely want to keep main.py for testing historical data and main_live.py for live trading.
This division of labor is standard practice in quantitative trading:
main.py (Backtesting Framework): Operates on static parquet files, allows you to optimize parameters across different folds, and acts as your sandbox. Keeping it unchanged ensures you always have a baseline to measure if strategy updates improve or harm performance.
main_live.py (Live Production Bridge): Interfaces directly with MetaTrader 5, handles real-time network states, manages rate limits dynamically via the AssetRiskGuard, and handles live trade routing.
Below is the step-by-step plan to update your live environment files to resolve the critical bugs (including the inactive sentiment skew and the inactive Order Book Imbalance bot).
Step 1: Update alpha_agent.py
We will keep your underlying core strategy logic intact (so your backtests remain valid), but we will add a small refinement to the FiveBotAlphaCouncil class to make sure its internal bot properties are easily modifiable by main_live.py.
Open alpha_agent.py and replace its contents with the code below:
code
Python
# alpha_agent.py
import sys
import os

# Ensure Python looks in the current directory for the strategies package
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from strategies.bot1 import Bot1
from strategies.bot2 import Bot2
from strategies.bot3 import Bot3
from strategies.bot4 import Bot4
from strategies.bot5 import Bot5

class FiveBotAlphaCouncil:
    def __init__(self):
        self.price_histories = {}  # {symbol: [list of historical prices]}
        self.bot1 = Bot1()
        self.bot2 = Bot2()
        self.bot3 = Bot3()
        self.bot4 = Bot4()
        self.bot5 = Bot5()

    def update_price(self, symbol: str, mid_price: float):
        """Maintains price history records sequentially."""
        if symbol not in self.price_histories:
            self.price_histories[symbol] = []
        self.price_histories[symbol].append(mid_price)
        
        # Limit history length to 100 to prevent memory leaks
        if len(self.price_histories[symbol]) > 100:
            self.price_histories[symbol].pop(0)

    def evaluate_market(self, row, symbol: str) -> dict:
        mid_price = (float(row['bid']) + float(row['ask'])) / 2.0
        history = self.price_histories.get(symbol, [])
        
        # Gather votes from individual bot classes
        v1 = self.bot1.evaluate(row)
        v2 = self.bot2.evaluate(history)
        v3 = self.bot3.evaluate(mid_price, history)
        v4 = self.bot4.evaluate(history)
        
        # Compile latest mid prices for the lead-lag calculations
        current_prices = {}
        for sym, hist in self.price_histories.items():
            if hist:
                current_prices[sym] = hist[-1]
                
        v5 = self.bot5.evaluate(symbol, current_prices, self.price_histories)
        
        votes = {"Bot1": v1, "Bot2": v2, "Bot3": v3, "Bot4": v4, "Bot5": v5}
        vote_values = list(votes.values())
        buy_count = vote_values.count("BUY")
        sell_count = vote_values.count("SELL")
        
        final_signal = "HOLD"
        vote_strength = 0
        
        # Consensus gate: requires a majority of 3+ agreement
        if buy_count >= 3 and buy_count > sell_count:
            final_signal = "BUY"
            vote_strength = buy_count
        elif sell_count >= 3 and sell_count > buy_count:
            final_signal = "SELL"
            vote_strength = sell_count
            
        return {
            "signal": final_signal,
            "vote_strength": vote_strength,
            "votes": votes
        }
Step 2: Update main_live.py
We are making three primary updates to your live execution engine:
Fixing the threshold updating bug: Direct updates now target council.bot1.threshold and council.bot3.z_threshold directly.
Live Order Book Subscription: We use mt5.market_book_add to subscribe to depth-of-market for allowed assets, calculate real-time imbalances, and pass them to Bot 1.
Warm-up Price History on Startup: Instead of booting up with empty arrays (which would force the bots to wait 30 seconds to begin trading), the script will query the last 100 historical 1-minute candles from the MT5 server directly when initializing, ensuring the bots are immediately active and structurally aligned with the backtest's timescales.
Open main_live.py and replace its contents with the code below:
code
Python
# main_live.py
import time
import json
import os
import pandas as pd
import MetaTrader5 as mt5
import logfire
from alpha_agent import FiveBotAlphaCouncil
from risk_agent import AssetRiskGuard, AccountState

# Configure Logfire for live monitoring
logfire.configure(
    token="pylf_v1_eu_zwcrVr8W6Lq9FYfGFLcbP1kr3VmcL6kyJdTqpbZNNhMp",
    console=logfire.ConsoleOptions(min_log_level="notice")
)
logfire.instrument_pydantic()

ALLOWED_ASSETS = [
    "AUDUSD", "EURCHF", "EURGBP", "EURUSD", "GBPUSD", "USDCAD", "USDCHF", "USDJPY",
    "XAGUSD", "XAUUSD",
    "BARUSD", "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
]

SENTIMENT_FILE = "sentiment_regime.json"

def load_sentiment_bias() -> str:
    """Reads the background sentiment file generated by your Northflank job."""
    if os.path.exists(SENTIMENT_FILE):
        try:
            with open(SENTIMENT_FILE, "r") as f:
                data = json.load(f)
                return data.get("bias", "NEUTRAL")
        except Exception:
            pass
    return "NEUTRAL"

def get_live_book_imbalance(symbol: str) -> float:
    """Fetches Depth of Market from MT5 to compute a live order book imbalance."""
    items = mt5.market_book_get(symbol)
    if not items or len(items) == 0:
        return 0.0
    
    total_bids = 0.0
    total_asks = 0.0
    
    for item in items:
        # Check order types: 1=Buy, 2=Sell (or MT5 specific constants)
        if item.type in [mt5.BOOK_TYPE_BUY, mt5.BOOK_TYPE_BUY_LIMIT]:
            total_bids += item.volume_dbl if hasattr(item, 'volume_dbl') else item.volume
        elif item.type in [mt5.BOOK_TYPE_SELL, mt5.BOOK_TYPE_SELL_LIMIT]:
            total_asks += item.volume_dbl if hasattr(item, 'volume_dbl') else item.volume
            
    if (total_bids + total_asks) > 0:
        return (total_bids - total_asks) / (total_bids + total_asks)
    return 0.0

def warmup_council_histories(council: FiveBotAlphaCouncil):
    """Fills history with the latest M1 close bars to avoid waiting for initial warmups."""
    print("⏳ Warming up asset price histories using MT5 M1 bars...")
    for symbol in ALLOWED_ASSETS:
        # Fetch last 100 1-minute close prices
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 100)
        if rates is not None and len(rates) > 0:
            prices = [float(candle['close']) for candle in rates]
            council.price_histories[symbol] = prices
            print(f"   Warmup complete for {symbol}: Loaded {len(prices)} bars.")
        else:
            print(f"   ⚠️ Warmup skipped/failed for {symbol}. Will accumulate live ticks.")

def execute_mt5_order(symbol: str, action: str, volume: float, price: float, comment: str = ""):
    """Submits a market execution order directly to the MetaTrader 5 terminal."""
    order_type = mt5.ORDER_TYPE_BUY if action == "BUY" else mt5.ORDER_TYPE_SELL
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "deviation": 20, # Max slippage in points
        "magic": 123456, # Council unique identifier
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC, # Immediate-or-Cancel
    }
    
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logfire.error("MT5 Order Failed", symbol=symbol, action=action, error=result.comment, retcode=result.retcode)
        print(f"❌ MT5 Order Failed for {symbol}: {result.comment}")
    else:
        logfire.notice("MT5 Order Executed Successfully", symbol=symbol, action=action, price=result.price, volume=volume)
        print(f"🎯 Successful {action} order executed on {symbol} at {result.price}")
    return result

def live_trading_loop():
    print("==================================================")
    print("      QUANTBOT METATRADER 5 LIVE ORCHESTRATOR     ")
    print("==================================================")
    
    # 1. Initialize connection to MT5 terminal
    if not mt5.initialize():
        print(f"❌ MT5 Initialization failed: {mt5.last_error()}")
        return
        
    print("✅ Successfully linked to MetaTrader 5 terminal.")
    
    council = FiveBotAlphaCouncil()
    guard = AssetRiskGuard()
    
    # Warm up council price buffers
    warmup_council_histories(council)
    
    # Subscribe to Depth of Market books
    for symbol in ALLOWED_ASSETS:
        if mt5.market_book_add(symbol):
            print(f"✅ Subscribed to order book depth for {symbol}")
        else:
            print(f"⚠️ Failed to subscribe to order book depth for {symbol}: {mt5.last_error()}")
    
    try:
        while True:
            # Read global macro sentiment to dynamically skew decision parameters
            sentiment_bias = load_sentiment_bias()
            
            # Apply sentiment skew directly to strategy instances inside the council
            if sentiment_bias == "BULLISH":
                council.bot1.threshold = 0.25 
                council.bot3.z_threshold = 2.8 # Less sensitive to mean-reverting sells
            elif sentiment_bias == "BEARISH":
                council.bot1.threshold = 0.45 
                council.bot3.z_threshold = 2.2 # More sensitive to mean-reverting sells
            else:
                council.bot1.threshold = 0.35 # Default
                council.bot3.z_threshold = 2.5 # Default
            
            # 2. Sync account balance metrics live with the terminal
            acct = mt5.account_info()
            if acct is None:
                print("⚠️ Failed to fetch live account details from MT5.")
                time.sleep(1)
                continue
                
            current_state = AccountState(
                equity=acct.equity,
                used_margin=acct.margin,
                gross_exposure=acct.margin_initial # Margin initialized can serve as proxy exposure
            )
            
            # 3. Process each instrument
            for symbol in ALLOWED_ASSETS:
                tick = mt5.symbol_info_tick(symbol)
                if tick is None:
                    continue
                    
                mid_price = (tick.bid + tick.ask) / 2.0
                council.update_price(symbol, mid_price)
                
                # Check current open positions in MT5 for this asset
                positions = mt5.positions_get(symbol=symbol)
                
                # --- EXIT EVALUATION ---
                if positions:
                    pos = positions[0] # Evaluate the first position
                    entry_price = pos.price_open
                    direction = "BUY" if pos.type == mt5.POSITION_TYPE_BUY else "SELL"
                    
                    if direction == "BUY":
                        current_return = (mid_price - entry_price) / entry_price
                    else:
                        current_return = (entry_price - mid_price) / entry_price
                        
                    # Target (+0.2%) or Stop Loss (-0.1%)
                    if current_return >= 0.002 or current_return <= -0.001:
                        close_action = "SELL" if direction == "BUY" else "BUY"
                        print(f"🛑 [Exit Signal] Closing {symbol} position...")
                        execute_mt5_order(symbol, close_action, pos.volume, mid_price, comment="Exit Bracket")
                        
                # --- ENTRY EVALUATION ---
                else:
                    # Get live order book imbalance
                    live_imbalance = get_live_book_imbalance(symbol)
                    
                    # Construct structural mock row to send to your bots
                    mock_row = {
                        'bid': tick.bid,
                        'ask': tick.ask,
                        'book_imbalance': live_imbalance,
                    }
                    
                    analysis = council.evaluate_market(mock_row, symbol)
                    signal = analysis.get("signal")
                    
                    if signal in ["BUY", "SELL"]:
                        trade_size_cash = 1000000.0 # Standard size from backtest
                        
                        current_time = pd.Timestamp.now()
                        is_safe = guard.validate_trade(current_state, symbol, trade_size_cash, current_time)
                        
                        if is_safe:
                            trade_volume = trade_size_cash / mid_price
                            # Standard Forex conversion: $100k exposure equals roughly 1 lot
                            mt5_lot_size = round(trade_volume / 100000.0, 2) 
                            
                            if mt5_lot_size > 0:
                                print(f"🚀 [Entry Signal] Executing {signal} for {symbol} with lots {mt5_lot_size}...")
                                execute_mt5_order(symbol, signal, mt5_lot_size, mid_price, comment="Council Consensus")
            
            # Rest 1 second between polls
            time.sleep(1) 
            
    except KeyboardInterrupt:
        print("\nStopping Live Execution Bridge...")
    finally:
        # Release Book Subscriptions safely
        for symbol in ALLOWED_ASSETS:
            mt5.market_book_release(symbol)
        mt5.shutdown()
        print("MetaTrader 5 connection closed.")

if __name__ == "__main__":
    live_trading_loop()
Step 3: Action Required
Keep main.py as is: This allows you to continue benchmarking model strategies with standard historical data.
Apply updates to your local environment: Replace alpha_agent.py and main_live.py with the codes above.
Run a quick test: Run main_live.py once to confirm that your connection establishes, and check if it successfully downloads historical 1-minute candles from your MT5 terminal.
Once you have verified that the connection establishes and the warm-up cycle completes without errors, let me know and we will proceed to create the Async Market Watch script to deploy on Northflank!
User 12:12 PM
main_live.py : The term 'main_live.py' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
ok updated all of them. This is the error:
main_live.py
code
Code
+ CategoryInfo          : ObjectNotFound: (main_live.py:String) [], CommandNotFoundException
  + FullyQualifiedErrorId : CommandNotFoundException
Suggestion [3,General]: The command main_live.py was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\main_live.py". See "get-help about_Command_Precedence" for more details.
Model 12:12 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
In Windows PowerShell, you cannot execute a Python script by typing just the filename because PowerShell does not load commands from the current working directory by default for security reasons.
To run your live script, execute it using your Python interpreter in the terminal:
code
Powershell
python main_live.py
If your machine uses the Python launcher (py), you can use:
code
Powershell
py main_live.py
Or, if you want PowerShell to trigger Python automatically via file associations, you must add the path prefix as PowerShell suggested:
code
Powershell
.\main_live.py
Try running python main_live.py and check if it connects to MetaTrader 5 and completes the 1-minute historical warm-up sequence.
Model 12:12 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
Yes, you are in the correct place. The integrated terminal inside Visual Studio Code is exactly where you want to be.
That terminal is running Windows PowerShell behind the scenes inside your editor. The error you saw earlier was not because of VS Code, but simply because PowerShell requires you to explicitly state how to run the file.
In that same VS Code terminal, simply type:
code
Powershell
python main_live.py
and press Enter. This tells the terminal to use Python to execute the script in your current directory.
Model 12:13 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
User 12:14 PM
yes let's do it setting up market wathc. I have this draft sentiment_engine.py import os
import xml.etree.ElementTree as ET
import json
import requests
import anthropic
Configure your API credentials (to be set in Northflank Environment Variables) [1]
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "your_anthropic_key_here")
DOUBLEWORD_KEY = os.getenv("DOUBLEWORD_API_KEY", "your_doubleword_key_here")
Feeds targeting primary asset drivers in the competition [1]
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
code
Code
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
code
Code
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
code
Code
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
if name == "main":
run_sentiment_pipeline()
Model 12:14 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
The Northflank to Lightsail Architecture Challenge
Since your sentiment_engine.py will run on Northflank, and your main_live.py will run on Amazon Lightsail, they cannot easily share a local sentiment_regime.json file.
To bridge this gap cleanly and cheaply:
We will turn sentiment_engine.py on Northflank into a lightweight FastAPI web server.
An async background task will run every 5 minutes to fetch RSS feeds, process them using Doubleword (Nvidia Nemotron), analyze them using Anthropic, and store the resulting bias in memory.
The FastAPI app will expose a public GET endpoint: /sentiment.
Your main_live.py on Lightsail will make a fast async or synchronous HTTP GET request to your Northflank endpoint instead of reading a local file.
Step 1: Create sentiment_engine.py (For Northflank)
Create a new file in your repository named sentiment_engine.py. This code uses aiohttp for non-blocking HTTP requests, FastAPI to expose the endpoint, and AsyncAnthropic to preserve your thread limits.
code
Python
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
Step 2: Create requirements.txt (For Northflank)
Create a requirements.txt file in your root folder. This instructs Northflank's builder on what dependencies to install automatically.
code
Text
fastapi==0.110.0
uvicorn==0.28.0
aiohttp==3.9.3
pydantic==2.6.4
anthropic==0.21.3
logfire==0.32.0
Step 3: Update main_live.py (On Lightsail)
We need to update main_live.py to point to your new Northflank API deployment. Replace the local load_sentiment_bias() logic with an HTTP call.
Locate load_sentiment_bias() inside main_live.py and replace it with this version:
code
Python
# Updated function in main_live.py
import requests

# Set your Northflank deployment address here once you build the service
NORTHFLANK_URL = os.getenv("SENTIMENT_API_URL", "https://your-app-name.code.northflank.com/sentiment")

def load_sentiment_bias() -> str:
    """Fetches real-time market sentiment bias from your Northflank web service."""
    try:
        response = requests.get(NORTHFLANK_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("bias", "NEUTRAL")
    except Exception as e:
        # Fallback to local file if the server is offline or not yet deployed
        if os.path.exists("sentiment_regime.json"):
            try:
                with open("sentiment_regime.json", "r") as f:
                    data = json.load(f)
                    return data.get("bias", "NEUTRAL")
            except Exception:
                pass
    return "NEUTRAL"
Verify Local Testing
Before deploying to Northflank, you can run the sentiment engine locally to verify that it functions correctly:
In your VS Code terminal, start the local server:
code
Powershell
python -m uvicorn sentiment_engine:app --reload
Open your web browser and go to http://127.0.0.1:8000/sentiment. You should see the default JSON payload. Within a few seconds, the background task will fetch the live RSS feeds and update the bias.
Keep the server running and try running python main_live.py in a separate terminal. It will query your local server, retrieve the bias, adjust your bot parameters, and execute the MT5 warm-up phase.
Model 12:21 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
Here is the complete code for main_live.py with the new load_sentiment_bias() function fully integrated. You can copy and paste this entire block directly into your main_live.py file.
Complete Updated main_live.py
code
Python
# main_live.py
import time
import json
import os
import requests
import pandas as pd
import MetaTrader5 as mt5
import logfire
from alpha_agent import FiveBotAlphaCouncil
from risk_agent import AssetRiskGuard, AccountState

# Configure Logfire for live monitoring
logfire.configure(
    token="pylf_v1_eu_zwcrVr8W6Lq9FYfGFLcbP1kr3VmcL6kyJdTqpbZNNhMp",
    console=logfire.ConsoleOptions(min_log_level="notice")
)
logfire.instrument_pydantic()

ALLOWED_ASSETS = [
    "AUDUSD", "EURCHF", "EURGBP", "EURUSD", "GBPUSD", "USDCAD", "USDCHF", "USDJPY",
    "XAGUSD", "XAUUSD",
    "BARUSD", "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
]

# ---------------------------------------------------------------------------
# NORTHFLANK CONFIGURATION
# ---------------------------------------------------------------------------
# If you are running both locally, this defaults to 'http://127.0.0.1:8000/sentiment'.
# Once you deploy to Northflank, change this URL to your Northflank web service address.
NORTHFLANK_URL = os.getenv("SENTIMENT_API_URL", "http://127.0.0.1:8000/sentiment")
SENTIMENT_FILE = "sentiment_regime.json"

def load_sentiment_bias() -> str:
    """Fetches real-time market sentiment bias from your Northflank web service,

    with fallbacks to a local file and a safe default ('NEUTRAL').
    """
    try:
        response = requests.get(NORTHFLANK_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("bias", "NEUTRAL")
    except Exception:
        # If the API server is offline or not yet deployed, fallback to local JSON file
        if os.path.exists(SENTIMENT_FILE):
            try:
                with open(SENTIMENT_FILE, "r") as f:
                    data = json.load(f)
                    return data.get("bias", "NEUTRAL")
            except Exception:
                pass
    return "NEUTRAL"
# ---------------------------------------------------------------------------

def get_live_book_imbalance(symbol: str) -> float:
    """Fetches Depth of Market from MT5 to compute a live order book imbalance."""
    items = mt5.market_book_get(symbol)
    if not items or len(items) == 0:
        return 0.0
    
    total_bids = 0.0
    total_asks = 0.0
    
    for item in items:
        if item.type in [mt5.BOOK_TYPE_BUY, mt5.BOOK_TYPE_BUY_LIMIT]:
            total_bids += item.volume_dbl if hasattr(item, 'volume_dbl') else item.volume
        elif item.type in [mt5.BOOK_TYPE_SELL, mt5.BOOK_TYPE_SELL_LIMIT]:
            total_asks += item.volume_dbl if hasattr(item, 'volume_dbl') else item.volume
            
    if (total_bids + total_asks) > 0:
        return (total_bids - total_asks) / (total_bids + total_asks)
    return 0.0

def warmup_council_histories(council: FiveBotAlphaCouncil):
    """Fills history with the latest M1 close bars to avoid waiting for initial warmups."""
    print("⏳ Warming up asset price histories using MT5 M1 bars...")
    for symbol in ALLOWED_ASSETS:
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 100)
        if rates is not None and len(rates) > 0:
            prices = [float(candle['close']) for candle in rates]
            council.price_histories[symbol] = prices
            print(f"   Warmup complete for {symbol}: Loaded {len(prices)} bars.")
        else:
            print(f"   ⚠️ Warmup skipped/failed for {symbol}. Will accumulate live ticks.")

def execute_mt5_order(symbol: str, action: str, volume: float, price: float, comment: str = ""):
    """Submits a market execution order directly to the MetaTrader 5 terminal."""
    order_type = mt5.ORDER_TYPE_BUY if action == "BUY" else mt5.ORDER_TYPE_SELL
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "deviation": 20, 
        "magic": 123456, 
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC, 
    }
    
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logfire.error("MT5 Order Failed", symbol=symbol, action=action, error=result.comment, retcode=result.retcode)
        print(f"❌ MT5 Order Failed for {symbol}: {result.comment}")
    else:
        logfire.notice("MT5 Order Executed Successfully", symbol=symbol, action=action, price=result.price, volume=volume)
        print(f"🎯 Successful {action} order executed on {symbol} at {result.price}")
    return result

def live_trading_loop():
    print("==================================================")
    print("      QUANTBOT METATRADER 5 LIVE ORCHESTRATOR     ")
    print("==================================================")
    
    if not mt5.initialize():
        print(f"❌ MT5 Initialization failed: {mt5.last_error()}")
        return
        
    print("✅ Successfully linked to MetaTrader 5 terminal.")
    
    council = FiveBotAlphaCouncil()
    guard = AssetRiskGuard()
    
    warmup_council_histories(council)
    
    for symbol in ALLOWED_ASSETS:
        if mt5.market_book_add(symbol):
            print(f"✅ Subscribed to order book depth for {symbol}")
        else:
            print(f"⚠️ Failed to subscribe to order book depth for {symbol}: {mt5.last_error()}")
    
    try:
        while True:
            # Read global macro sentiment live from your API or local file
            sentiment_bias = load_sentiment_bias()
            
            if sentiment_bias == "BULLISH":
                council.bot1.threshold = 0.25 
                council.bot3.z_threshold = 2.8 
            elif sentiment_bias == "BEARISH":
                council.bot1.threshold = 0.45 
                council.bot3.z_threshold = 2.2 
            else:
                council.bot1.threshold = 0.35 
                council.bot3.z_threshold = 2.5 
            
            acct = mt5.account_info()
            if acct is None:
                print("⚠️ Failed to fetch live account details from MT5.")
                time.sleep(1)
                continue
                
            current_state = AccountState(
                equity=acct.equity,
                used_margin=acct.margin,
                gross_exposure=acct.margin_initial 
            )
            
            for symbol in ALLOWED_ASSETS:
                tick = mt5.symbol_info_tick(symbol)
                if tick is None:
                    continue
                    
                mid_price = (tick.bid + tick.ask) / 2.0
                council.update_price(symbol, mid_price)
                
                positions = mt5.positions_get(symbol=symbol)
                
                # --- EXIT EVALUATION ---
                if positions:
                    pos = positions[0] 
                    entry_price = pos.price_open
                    direction = "BUY" if pos.type == mt5.POSITION_TYPE_BUY else "SELL"
                    
                    if direction == "BUY":
                        current_return = (mid_price - entry_price) / entry_price
                    else:
                        current_return = (entry_price - mid_price) / entry_price
                        
                    if current_return >= 0.002 or current_return <= -0.001:
                        close_action = "SELL" if direction == "BUY" else "BUY"
                        print(f"🛑 [Exit Signal] Closing {symbol} position...")
                        execute_mt5_order(symbol, close_action, pos.volume, mid_price, comment="Exit Bracket")
                        
                # --- ENTRY EVALUATION ---
                else:
                    live_imbalance = get_live_book_imbalance(symbol)
                    
                    mock_row = {
                        'bid': tick.bid,
                        'ask': tick.ask,
                        'book_imbalance': live_imbalance,
                    }
                    
                    analysis = council.evaluate_market(mock_row, symbol)
                    signal = analysis.get("signal")
                    
                    if signal in ["BUY", "SELL"]:
                        trade_size_cash = 1000000.0 
                        
                        current_time = pd.Timestamp.now()
                        is_safe = guard.validate_trade(current_state, symbol, trade_size_cash, current_time)
                        
                        if is_safe:
                            trade_volume = trade_size_cash / mid_price
                            mt5_lot_size = round(trade_volume / 100000.0, 2) 
                            
                            if mt5_lot_size > 0:
                                print(f"🚀 [Entry Signal] Executing {signal} for {symbol} with lots {mt5_lot_size}...")
                                execute_mt5_order(symbol, signal, mt5_lot_size, mid_price, comment="Council Consensus")
            
            time.sleep(1) 
            
    except KeyboardInterrupt:
        print("\nStopping Live Execution Bridge...")
    finally:
        for symbol in ALLOWED_ASSETS:
            mt5.market_book_release(symbol)
        mt5.shutdown()
        print("MetaTrader 5 connection closed.")

if __name__ == "__main__":
    live_trading_loop()
Understanding the Northflank Deployment URL
What is a "Northflank deployment address"?
When you write code on your computer, it runs locally on your machine, accessible at http://127.0.0.1 (which is standard computer terminology for "myself").
When you upload your code to Northflank, Northflank takes your code and runs it on a computer in their cloud. Because it is on the internet, Northflank generates a public web address (a URL) for your app, such as:
https://sentiment-engine-xxxx.code.northflank.com
This allows your local computer (running main_live.py inside VS Code) to send requests over the internet to retrieve the sentiment data.
Step-by-Step Guide: Deploying to Northflank for the First Time
Since you already have a GitHub account linked to VS Code, the easiest way to deploy to Northflank is via your GitHub repository.
Step 1: Push Your Code to GitHub
Ensure your repository has these files in the root folder:
sentiment_engine.py
requirements.txt
Commit and push them to your GitHub repository using VS Code.
Step 2: Create a Service on Northflank
Log in to your Northflank Dashboard.
Click Create New (top right) and select Service.
Choose Combined Service (this builds your code from GitHub and hosts it instantly).
Step 3: Link Your GitHub Repository
Select Repository as your source.
Link your GitHub account if you haven't done so.
Select your repository name and the branch (usually main or master).
Step 4: Configure the Build Settings
For Build Source, select Buildpack (Northflank will detect that your project uses Python because of your requirements.txt and configure it automatically).
For Environment Variables (under advanced settings or setup options), add your secret API keys so your code can read them:
Key: ANTHROPIC_API_KEY | Value: Your Anthropic Claude API Key
Key: DOUBLEWORD_API_KEY | Value: Your Doubleword API Key
Step 5: Deploy and Copy Your URL
Click Create Service at the bottom.
Northflank will build your image and spin up the container. This usually takes 2–3 minutes.
Once running, look at the top of your service dashboard on Northflank. You will see a unique link next to "Ports" or under your service name (ending in .code.northflank.com).
Copy that URL. It should look like this:
https://[your-service-subdomain].code.northflank.com
Step 6: Link It to main_live.py
Open main_live.py in VS Code and change the URL string to match your Northflank address (remembering to add /sentiment at the end):
code
Python
NORTHFLANK_URL = "https://[your-service-subdomain].code.northflank.com/sentiment"
Save the file. Your live trading system is now configured to retrieve macro-sentiments directly from your deployed cloud service.
Model 12:26 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
Model 12:32 PM
ThinkingThoughts
Expand to view model thoughts

chevron_right
You should choose Buildpack.
Because this is your first time deploying a service like this, a Buildpack is much simpler and safer than writing a custom Dockerfile.
Here is why, and exactly how to configure it in Northflank:
Why Buildpack is Better for Your Setup
Zero Configuration Files: With a Dockerfile, you have to write a custom text file instructing the system on exactly which version of Linux to download, how to copy files, and how to configure system privileges. It is very easy to make syntax errors.
Automatic Detection: A Buildpack will look at your GitHub repository, see your requirements.txt file, automatically figure out that you are using Python, download the correct runtime, and install all your libraries (like fastapi, uvicorn, anthropic, and aiohttp) automatically.
How to Configure the Buildpack in Northflank
When creating your service, after you choose Buildpack, you just need to fill in two key settings to make sure your FastAPI web server starts and can be reached by your computer:
1. The Run Command (CMD Override)
You need to tell the buildpack exactly how to start your FastAPI app. Look for a setting called Docker CMD override (usually under "Advanced options" or "Run settings") and type this command:
code
Text
uvicorn sentiment_engine:app --host 0.0.0.0 --port 8000
Why 0.0.0.0 is important: By default, servers only listen to "localhost" (themselves). Binding to 0.0.0.0 tells the server to listen to requests coming from outside (like your MetaTrader script on your Lightsail server over the internet).
2. The Port Settings (Networking)
Under the Networking or Ports section of the service setup, add the port your application is running on so Northflank can route traffic to it:
Port Number: 8000 (this must match the --port 8000 in your Run Command above).
Protocol: HTTP or HTTP/1.1.
Access: Set this to Public (so your local machine can access it).
Once you click Create Service, Northflank will build and deploy your code. When it finishes, it will generate the public URL (ending in .code.northflank.com or similar) that you will use in main_live.py.
info
Google AI models may make mistakes, so double-check outputs.
Use Arrow Up and Arrow Down to select a turn, Enter to jump to it, and Escape to return to the chat.
Start typing a prompt to see what our models can do

google
Grounding with Google Search


Response ready.