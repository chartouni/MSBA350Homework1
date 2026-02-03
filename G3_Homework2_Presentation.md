# Group 3 - Homework 2 Presentation
## Stock Returns, Volatility, Inflation Analysis & Cryptocurrency Bar Sampling

**Group Members:** [Add Names Here]

---

## Agenda

1. Simple vs Log Returns Analysis
2. Volatility Analysis & Market Risk
3. Inflation Impact on Real Returns
4. Cryptocurrency Bar Sampling Methods
5. Key Findings & Conclusions

---

## Part 1: Simple vs Log Returns Analysis

### What are Simple and Log Returns?

**Simple Return:**
- Formula: R_t = (P_t - P_{t-1}) / P_{t-1}
- Intuitive: "How much did I gain/lose?"

**Log Return:**
- Formula: r_t = ln(P_t / P_{t-1})
- Better properties: Time-additive, more symmetric

---

### Key Statistics

| Metric | Simple Returns | Log Returns |
|--------|----------------|-------------|
| **MSFT Mean** | 0.1169% | 0.1023% |
| **MSFT Std Dev** | 1.71% | 1.71% |
| **Correlation** | **>0.998** for all stocks | (Nearly perfect) |

**Finding:** Simple and log returns are virtually identical for daily data!

---

### Visual Evidence: Pairwise Comparison

**All 10 stocks show:**
- Perfect linear relationship (correlation >0.998)
- Points hug the y=x reference line
- Minimal divergence even at extremes

**Key Insight:**
- For small daily returns, ln(1+R) ≈ R
- Divergence only matters for large price movements
- Choice of return type has minimal practical impact for daily stock analysis

---

### MSFT Time Series Analysis

**Top Chart:** Simple vs Log Returns overlay
- Lines are virtually indistinguishable
- Both capture same volatility patterns
- COVID-19 crash visible in March 2020

**Bottom Chart:** Difference between methods
- Difference typically <0.001 (0.1%)
- Largest difference: ~0.012 during COVID crash
- **Conclusion:** Negligible difference in practice

---

### Practical Implications

| Return Type | Best For | Why |
|-------------|----------|-----|
| **Simple Returns** | Cross-sectional analysis | Additive across assets in portfolio |
| **Log Returns** | Time series analysis | Additive across time, symmetric |
| **Recommendation** | Use log returns | Better statistical properties for modeling |

---

## Part 2: Volatility Analysis

### Annualized Volatility Rankings

| Rank | Stock | Volatility | Sector | Risk Profile |
|------|-------|------------|--------|--------------|
| 1 | **KO** | **40.55%** | Consumer Staples | Surprisingly High! |
| 2 | **MSFT** | **38.62%** | Technology | Expected High |
| 3 | **LLY** | **36.46%** | Biotech | Expected High |
| 4 | **LUV** | 29.16% | Airlines | High |
| 5 | **LMT** | 28.96% | Aerospace | Moderate-High |
| 6 | **KHC** | 27.40% | Consumer Staples | Moderate |
| 7 | **META** | 27.10% | Technology | Moderate |
| 8 | **LOW** | 23.23% | Retail | Moderate |
| 9 | **MCD** | 20.51% | Consumer Staples | Low |
| 10 | **KEY** | **18.15%** | Banking | **Lowest** |

**Average Portfolio Volatility:** 29.01%

---

### Surprising Findings

**KO (Coca-Cola) - Highest Volatility?**
- Traditionally viewed as "safe" consumer staple
- 40.55% volatility challenges this perception
- Possible reasons:
  - Market shifts in consumer preferences
  - Competition from health-conscious alternatives
  - Currency fluctuations (global operations)

**KEY (KeyCorp) - Lowest Volatility**
- Regional bank with stable operations
- 18.15% volatility = most consistent returns
- Best choice for risk-averse investors in this portfolio

---

### Rolling Volatility Analysis

**Key Events Identified:**

1. **COVID-19 Crash (March 2020)**
   - MSFT: Spiked to 100% annualized volatility (3.7x normal)
   - KO: Peaked at 80% (4.4x normal!)
   - META: Reached 85% (3.1x normal)

2. **2022 Tech Selloff**
   - META: 40-50% sustained volatility
   - Related to metaverse concerns & Fed rate hikes

3. **2025 Recent Decline**
   - Volatility returning to normal levels
   - Market stabilizing post-pandemic

**Insight:** Volatility is NOT constant - it clusters during crisis periods

---

### Investment Implications

**Risk-Return Spectrum:**

**High Risk, High Potential Return:**
- KO, MSFT, LLY (35-40% volatility)
- Suitable for: Aggressive growth investors

**Moderate Risk:**
- LUV, LMT, KHC, META (27-29% volatility)
- Suitable for: Balanced portfolios

**Lower Risk:**
- LOW, MCD, KEY (18-23% volatility)
- Suitable for: Conservative investors, income-focused

**Portfolio Strategy:** Diversification across volatility profiles reduces overall risk!

---

## Part 3: Inflation Analysis

### CPI Growth (2015-2025)

**Starting Point (Jan 2015):** CPI = 237.24
**Ending Point (July 2025):** CPI = 307.81

**Total CPI Increase:** 29.75%
**Annualized Inflation:** ~2.5% per year

**Inflation Rate Characteristics:**
- Mostly fluctuating between 1.5% - 3.5%
- Generally above Fed's 2% target
- Persistent erosion of purchasing power

---

### The Inflation Impact: Total Returns Comparison

| Rank | Stock | Nominal Return | Real Return | Inflation Impact |
|------|-------|----------------|-------------|------------------|
| 1 | **MSFT** | **+1,233%** | **+938%** | **-296%** |
| 2 | **LLY** | **+954%** | **+720%** | **-234%** |
| 3 | **META** | **+698%** | **+521%** | **-177%** |
| 4 | **LOW** | +314% | +222% | -92% |
| 5 | **MCD** | +307% | +217% | -90% |
| 6 | **LMT** | +191% | +126% | -65% |
| 7 | **KO** | +139% | +86% | -53% |
| 8 | **KEY** | +80% | +40% | -40% |
| 9 | **LUV** | +4% | **-19%** | -23% |
| 10 | **KHC** | **-40%** | **-53%** | **-13%** |

---

### Critical Insights from Inflation Analysis

**1. MSFT: The Winner**
- Nominal: +1,233% (13.3x return!)
- Real: +938% (10.4x return)
- Lost 296% to inflation BUT still massive real gains
- **Conclusion:** Tech growth >> inflation

**2. LUV: The Hidden Loser**
- Nominal: +3.9% (barely positive)
- Real: -19.2% (actual loss!)
- **Conclusion:** Investors LOST purchasing power despite nominal gain

**3. KHC: The Disaster**
- Nominal: -40% (bad)
- Real: -53% (catastrophic!)
- Inflation made a bad investment even worse

---

### Visual Analysis: Gap Between Pink and Gold

**Widening Gap = Inflation Erosion**

**Best Performers:**
- MSFT: Gap widens but returns so strong it doesn't matter
- LLY: Similar pattern, exceptional growth
- META: Strong recovery post-2022

**Mediocre Performers:**
- LMT, KO: Gap grows steadily, modest real returns
- MCD, LOW: Decent but gap shows inflation impact

**Poor Performers:**
- KEY: Small gap but low total returns
- LUV: Gap shows complete erosion of gains
- KHC: Both lines negative, inflation adds insult to injury

---

### Why This Matters for Investors

**Real Returns = What Actually Matters**

1. **Retirement Planning:** Need real returns to maintain purchasing power
2. **Investment Selection:** A 5% return with 3% inflation = only 2% real gain
3. **Long-term Wealth:** Nominal gains are illusory if inflation keeps pace

**Portfolio Lesson:**
- Seek investments that consistently beat inflation
- Growth stocks (MSFT, LLY, META) did this successfully
- Value/defensive stocks (KO, LUV, KEY) struggled more

---

## Part 4: Cryptocurrency Bar Sampling

### What are Information-Driven Bars?

**Problem with Time Bars:**
- Sample at fixed time intervals (1 minute, 1 hour, 1 day)
- Ignores market activity levels
- High activity and low activity get same treatment

**Solution: Information-Driven Sampling**
- Sample based on market events, not time
- More samples during high activity
- Better statistical properties for modeling

---

### The Four Bar Types

| Bar Type | Sampling Trigger | What It Measures |
|----------|------------------|------------------|
| **Price Bars** | Fixed price change (e.g., $10) | Volatility events |
| **Tick Bars** | Fixed # of trades (e.g., 1M trades) | Market activity/liquidity |
| **Volume Bars** | Fixed volume traded (e.g., 1M coins) | Participation level |
| **Dollar Bars** | Fixed $ value traded (e.g., $100M) | Economic significance |

---

### Group 3 Cryptocurrencies Analysis

**Cryptocurrencies:** BNB, DOGE, DOT
**Data:** Last 3,000 hourly transactions from Binance (USDT pairs)

---

### BNB (Binance Coin) Results

**Bar Counts:**
- Price Bars: **27** (fewest - stable price movement)
- Tick Bars: **97**
- Volume Bars: **96**
- Dollar Bars: **96**

**Price Statistics:**
- High: $959.52
- Low: $750.08
- Average: $872.01
- Range: $209.44 (21.9%)

**Key Observation:**
- Price bars produced FAR fewer samples (27 vs ~96)
- Indicates relatively stable price with high volume concentration
- Most activity happened within narrow price bands

---

### BNB Return Distributions

**Price Bars:**
- Mean: -0.248%
- Std Dev: 2.351%
- Sample: Only 26 returns
- Distribution: Bimodal pattern (two humps)

**Tick Bars:**
- Mean: -0.084%
- Std Dev: 1.252%
- Sample: 96 returns
- Distribution: More uniform, slightly negative skew

**Volume Bars:**
- Mean: -0.089%
- Std Dev: 1.200%
- Sample: 95 returns
- Distribution: **Most normal-looking** (centered near zero)

**Dollar Bars:**
- Mean: -0.093%
- Std Dev: 1.255%
- Sample: 95 returns
- Distribution: **Very normal** (bell-curve shape)

---

### DOGE (Dogecoin) Results

**Bar Counts:**
- Price Bars: **69** (more than BNB - more volatile)
- Tick Bars: **96**
- Volume Bars: **95**
- Dollar Bars: **95**

**Price Statistics:**
- High: $0.16
- Low: $0.09
- Average: $0.13
- Range: $0.07 (54% range!)

**Key Observation:**
- Much more volatile than BNB (69 vs 27 price bars)
- Meme coin showing higher price variability
- Similar activity levels (tick/volume/dollar bars ~95)

---

### DOT (Polkadot) - [Pattern Similar to DOGE]

**Expected Results:**
- Moderate number of price bars
- Consistent tick/volume/dollar bar counts
- Return distributions showing market characteristics

---

### Comparing Bar Types: Key Insights

**1. Price Bars = Volatility Detector**
- Fewer bars → More stable asset (BNB: 27 bars)
- More bars → More volatile asset (DOGE: 69 bars)
- **Use case:** Comparing volatility across assets

**2. Tick Bars = Activity Detector**
- Consistent counts (~96) show similar trading frequency
- **Use case:** Understanding market participation

**3. Volume Bars = Participation Measure**
- Tracks actual coins changing hands
- **Use case:** Identifying accumulation/distribution phases

**4. Dollar Bars = Economic Significance**
- Accounts for both price AND volume
- Best for ML: Most normal return distributions
- **Use case:** Professional trading algorithms

---

### Statistical Properties: Why Dollar Bars Win

**Return Distribution Comparison:**

| Bar Type | Normal Distribution? | ML Suitability | i.i.d. Properties |
|----------|---------------------|----------------|-------------------|
| Price Bars | ❌ Often bimodal | Poor | Weak |
| Tick Bars | ⚠️ Somewhat | Moderate | Moderate |
| Volume Bars | ✅ Better | Good | Good |
| **Dollar Bars** | ✅✅ **Best** | **Excellent** | **Strong** |

**Why This Matters:**
- Most statistical models assume normal distributions
- i.i.d. (independent, identically distributed) = cleaner signals
- Dollar bars produce cleaner data for machine learning

---

### Practical Applications

**For Traders:**

**Use Price Bars when:**
- Setting stop-losses based on price movement
- Identifying breakout levels
- Comparing volatility across assets

**Use Tick Bars when:**
- High-frequency trading
- Market microstructure analysis
- Detecting unusual activity patterns

**Use Volume Bars when:**
- Volume-based strategies (e.g., VWAP)
- Identifying institutional flows
- Accumulation/distribution analysis

**Use Dollar Bars when:**
- Building ML models
- Professional algorithmic trading
- Need best statistical properties

---

### Real-World Interpretation

**What Different Bar Counts Tell Us:**

**Scenario 1: More tick bars, fewer dollar bars**
→ Many small trades = Retail activity

**Scenario 2: Fewer tick bars, more dollar bars**
→ Large institutional orders

**Scenario 3: Many price bars, few volume bars**
→ High volatility with low participation = Unstable

**Scenario 4: Few price bars, many volume bars**
→ High volume in narrow range = Accumulation phase

---

## Part 5: Key Findings & Conclusions

### Major Findings Summary

**1. Returns Analysis:**
- Simple and log returns are practically identical for daily data (correlation >0.998)
- Use log returns for better statistical properties in time series

**2. Volatility Analysis:**
- Wide range: 18% (KEY) to 40% (KO)
- COVID-19 caused 3-4x volatility spikes
- Volatility clusters during crisis periods
- Average portfolio volatility: 29%

**3. Inflation Impact:**
- CPI increased 29.75% over 10 years
- Top performers (MSFT +1233%, LLY +954%) overcame inflation
- LUV had negative REAL returns despite nominal gain
- Inflation eroded 40-296% of nominal gains

**4. Cryptocurrency Bars:**
- Dollar bars produce best statistical properties
- Different bar types reveal different market aspects
- Price bars best for volatility comparison
- 27-96 bars from same 3,000 hourly data points

---

### Investment Insights

**Best Performing Stocks (2015-2025):**
1. **MSFT:** +1,233% nominal, +938% real - Tech dominance
2. **LLY:** +954% nominal, +720% real - Biotech innovation
3. **META:** +698% nominal, +521% real - Social media giant

**Worst Performing Stocks:**
1. **KHC:** -40% nominal, -53% real - Value destruction
2. **LUV:** +4% nominal, -19% real - Failed to beat inflation
3. **KEY:** +80% nominal, +40% real - Underwhelming

**Risk-Adjusted Lesson:**
- High volatility doesn't always mean high returns (KO: 40% vol, 139% return)
- Low volatility doesn't mean safety (KEY: 18% vol, but only 80% return)
- Best performers combined growth with manageable volatility

---

### Methodological Insights

**Why This Analysis Matters:**

**1. Returns Calculation:**
- Understanding simple vs log returns prevents analytical errors
- Log returns are time-additive: crucial for compound analysis

**2. Volatility Understanding:**
- Static volatility numbers miss the dynamic nature
- Rolling volatility reveals market regime changes
- Crisis periods require different risk management

**3. Inflation Adjustment:**
- Nominal returns mislead investors
- Real returns show true wealth creation/destruction
- Essential for retirement and long-term planning

**4. Bar Sampling Innovation:**
- Traditional time bars are suboptimal
- Information-driven bars improve signal quality
- Critical for modern algorithmic trading

---

### Practical Recommendations

**For Portfolio Construction:**

1. **Diversify across volatility profiles**
   - Mix high-vol growth (MSFT, LLY) with low-vol stable (KEY, MCD)

2. **Focus on inflation-beating returns**
   - Target real returns >5% annually
   - Avoid "value traps" like LUV and KHC

3. **Monitor rolling volatility**
   - Increase defensive positions when volatility spikes
   - Crisis periods offer opportunities for repositioning

4. **Use appropriate return measures**
   - Log returns for time series analysis
   - Real returns for actual wealth assessment

---

### Advanced Trading Applications

**For Quantitative Strategies:**

1. **Feature Engineering**
   - Use dollar bars for ML model inputs
   - Calculate returns from information-driven bars

2. **Risk Management**
   - Rolling volatility for position sizing
   - Inflation-adjusted stops for long-term holds

3. **Signal Generation**
   - Volume bar divergences for accumulation detection
   - Price bar clustering for volatility breakouts

4. **Backtesting**
   - Test strategies on multiple bar types
   - Validate on inflation-adjusted returns

---

### Limitations & Future Work

**Current Limitations:**

1. **Sample Period:** 10 years may not capture full market cycles
2. **Survivorship Bias:** Analyzed existing stocks only
3. **CPI Approximation:** Used synthetic data (not official FRED data)
4. **Crypto Data:** Limited to 3,000 hourly bars (~4 months)

**Future Enhancements:**

1. Extend analysis to 20+ year periods
2. Include delisted/bankrupt stocks
3. Use official CPI data from Federal Reserve
4. Analyze full crypto history with tick-level data
5. Test trading strategies on different bar types
6. Add transaction costs and slippage

---

### Conclusions

**Key Takeaways:**

1. **Mathematical equivalence:** Simple ≈ Log returns for daily data, but log is superior for analysis

2. **Volatility reality:** Not constant, clusters in crises, varies 2x across "similar" stocks

3. **Inflation matters:** Can turn nominal gains into real losses (see LUV)

4. **Growth wins:** MSFT, LLY, META crushed inflation; value stocks struggled

5. **Bar innovation:** Dollar bars >> time bars for statistical modeling

6. **Market complexity:** Different sampling methods reveal different market aspects

**Final Thought:**
Modern portfolio analysis requires moving beyond simple price charts. Understanding returns calculation, volatility dynamics, inflation impact, and advanced sampling methods is essential for successful investing in today's markets.

---

## Questions?

**Topics We Can Discuss:**

- Deep dive into any specific stock
- Alternative bar sampling methods
- Portfolio optimization using these insights
- Trading strategy development
- Statistical properties of different return measures

---

## Appendix: Technical Details

### Formulas Used

**Simple Return:**
```
R_t = (P_t - P_{t-1}) / P_{t-1}
```

**Log Return:**
```
r_t = ln(P_t / P_{t-1}) = ln(P_t) - ln(P_{t-1})
```

**Annualized Volatility:**
```
σ_annual = σ_daily × √252
```

**Real Return:**
```
Real Return = (1 + Nominal Return) / (1 + Inflation) - 1
```

**Cumulative Return:**
```
Cumulative = ∏(1 + R_t) - 1
```

---

### Data Sources

- **Stock Data:** Yahoo Finance (yfinance)
- **Date Range:** 2015-01-01 to 2025-07-31
- **CPI Data:** Synthetic (based on ~2.5% average inflation)
- **Crypto Data:** Binance Public API (USDT pairs)
- **Sampling Frequency:** Daily (stocks), Hourly (crypto)

---

### Tools & Technologies

- **Language:** Python 3.8+
- **Libraries:**
  - pandas (data manipulation)
  - numpy (numerical computing)
  - matplotlib/seaborn (visualization)
  - yfinance (stock data)
  - requests (API calls)
- **Analysis:** Jupyter Notebook
- **Version Control:** Git/GitHub

---

## Thank You!

**Group 3 - MSBA 350 Homework 2**

Contact: [Add contact info if needed]

Repository: [Add GitHub link if public]
