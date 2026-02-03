from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

def add_title_slide(title, subtitle=""):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title_shape = slide.shapes.title
    subtitle_shape = slide.placeholders[1]

    title_shape.text = title
    if subtitle:
        subtitle_shape.text = subtitle
    return slide

def add_content_slide(title, content_list):
    """Add a content slide with bullet points"""
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title_shape = slide.shapes.title
    body_shape = slide.placeholders[1]

    title_shape.text = title
    tf = body_shape.text_frame
    tf.clear()

    for item in content_list:
        if isinstance(item, dict):
            p = tf.add_paragraph()
            p.text = item['text']
            p.level = item.get('level', 0)
            p.font.size = Pt(item.get('size', 18))
        else:
            p = tf.add_paragraph()
            p.text = item
            p.level = 0
            p.font.size = Pt(18)

    return slide

def add_table_slide(title, headers, rows):
    """Add a slide with a table"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    title_shape = slide.shapes.title
    title_shape.text = title

    # Add table
    rows_count = len(rows) + 1
    cols_count = len(headers)
    left = Inches(0.5)
    top = Inches(2.0)
    width = Inches(9.0)
    height = Inches(4.5)

    table = slide.shapes.add_table(rows_count, cols_count, left, top, width, height).table

    # Set headers
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.text_frame.paragraphs[0].font.bold = True
        cell.text_frame.paragraphs[0].font.size = Pt(14)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(68, 114, 196)
        cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

    # Set data
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.text = str(value)
            cell.text_frame.paragraphs[0].font.size = Pt(12)

    return slide

# Slide 1: Title
add_title_slide(
    "Group 3 - Homework 2",
    "Stock Returns, Volatility, Inflation Analysis & Cryptocurrency Bar Sampling"
)

# Slide 2: Agenda
add_content_slide("Agenda", [
    "1. Simple vs Log Returns Analysis",
    "2. Volatility Analysis & Market Risk",
    "3. Inflation Impact on Real Returns",
    "4. Cryptocurrency Bar Sampling Methods",
    "5. Key Findings & Conclusions"
])

# PART 1: RETURNS ANALYSIS

# Slide 3: Returns Introduction
add_content_slide("Part 1: Simple vs Log Returns", [
    "What are Simple and Log Returns?",
    {"text": "Simple Return: R_t = (P_t - P_{t-1}) / P_{t-1}", "level": 1},
    {"text": "Intuitive: How much did I gain/lose?", "level": 2},
    {"text": "Log Return: r_t = ln(P_t / P_{t-1})", "level": 1},
    {"text": "Better properties: Time-additive, more symmetric", "level": 2},
    "",
    "Key Question: Does the choice matter for daily stock data?"
])

# Slide 4: Returns Statistics
add_table_slide(
    "Returns Statistics - Key Stocks",
    ["Metric", "MSFT Simple", "MSFT Log", "LLY Simple", "LLY Log"],
    [
        ["Mean", "0.1169%", "0.1023%", "0.1098%", "0.0930%"],
        ["Std Dev", "1.71%", "1.71%", "1.84%", "1.82%"],
        ["Min", "-14.74%", "-15.95%", "-11.66%", "-12.40%"],
        ["Max", "14.22%", "13.29%", "15.68%", "14.57%"],
        ["Correlation", "0.9996", "", "0.9995", ""]
    ]
)

# Slide 5: Key Finding - Perfect Correlation
add_content_slide("Key Finding: Nearly Perfect Correlation", [
    "All 10 stocks show correlation > 0.998",
    "",
    "Why are they so similar?",
    {"text": "For small returns: ln(1+R) ≈ R", "level": 1},
    {"text": "Daily returns are typically small", "level": 1},
    {"text": "Divergence only at extreme movements", "level": 1},
    "",
    "Practical Implication:",
    {"text": "Choice matters less for daily data", "level": 1},
    {"text": "Log returns preferred for statistical properties", "level": 1}
])

# Slide 6: When to Use Each
add_table_slide(
    "Practical Implications",
    ["Return Type", "Best For", "Why"],
    [
        ["Simple Returns", "Cross-sectional analysis", "Additive across assets in portfolio"],
        ["Log Returns", "Time series analysis", "Additive across time, symmetric"],
        ["Recommendation", "Use log returns", "Better statistical properties"]
    ]
)

# PART 2: VOLATILITY ANALYSIS

# Slide 7: Volatility Introduction
add_content_slide("Part 2: Volatility Analysis", [
    "Annualized Volatility Formula:",
    {"text": "σ_annual = σ_daily × √252", "level": 1},
    {"text": "252 = trading days per year", "level": 2},
    "",
    "Key Findings:",
    {"text": "Wide range: 18% to 40%", "level": 1},
    {"text": "COVID-19 caused 3-4x spikes", "level": 1},
    {"text": "Average portfolio: 29%", "level": 1}
])

# Slide 8: Volatility Rankings
add_table_slide(
    "Annualized Volatility Rankings",
    ["Rank", "Stock", "Volatility", "Sector"],
    [
        ["1", "KO", "40.55%", "Consumer Staples"],
        ["2", "MSFT", "38.62%", "Technology"],
        ["3", "LLY", "36.46%", "Biotech"],
        ["4", "LUV", "29.16%", "Airlines"],
        ["5", "LMT", "28.96%", "Aerospace"],
        ["6", "KHC", "27.40%", "Consumer Staples"],
        ["7", "META", "27.10%", "Technology"],
        ["8", "LOW", "23.23%", "Retail"],
        ["9", "MCD", "20.51%", "Consumer Staples"],
        ["10", "KEY", "18.15%", "Banking"]
    ]
)

# Slide 9: Surprising Finding
add_content_slide("Surprising Finding: KO Highest Volatility?", [
    "Coca-Cola (KO) - 40.55% volatility",
    {"text": "Traditionally viewed as 'safe' consumer staple", "level": 1},
    {"text": "Challenges common perception", "level": 1},
    "",
    "Possible Reasons:",
    {"text": "Market shifts in consumer preferences", "level": 1},
    {"text": "Health-conscious alternatives competition", "level": 1},
    {"text": "Currency fluctuations (global operations)", "level": 1},
    "",
    "KEY (KeyCorp) - Lowest at 18.15%",
    {"text": "Regional bank with stable operations", "level": 1}
])

# Slide 10: COVID Impact
add_content_slide("Rolling Volatility: COVID-19 Impact", [
    "March 2020 Volatility Spikes:",
    {"text": "MSFT: 100% annualized (3.7x normal)", "level": 1},
    {"text": "KO: 80% annualized (4.4x normal)", "level": 1},
    {"text": "META: 85% annualized (3.1x normal)", "level": 1},
    "",
    "2022 Tech Selloff:",
    {"text": "META: 40-50% sustained volatility", "level": 1},
    {"text": "Related to metaverse concerns & Fed rate hikes", "level": 1},
    "",
    "Key Insight: Volatility is NOT constant - it clusters!"
])

# Slide 11: Investment Implications
add_content_slide("Investment Implications by Risk Profile", [
    "High Risk, High Potential (35-40% volatility):",
    {"text": "KO, MSFT, LLY", "level": 1},
    {"text": "Suitable for: Aggressive growth investors", "level": 2},
    "",
    "Moderate Risk (27-29% volatility):",
    {"text": "LUV, LMT, KHC, META", "level": 1},
    {"text": "Suitable for: Balanced portfolios", "level": 2},
    "",
    "Lower Risk (18-23% volatility):",
    {"text": "LOW, MCD, KEY", "level": 1},
    {"text": "Suitable for: Conservative, income-focused", "level": 2}
])

# PART 3: INFLATION ANALYSIS

# Slide 12: Inflation Introduction
add_content_slide("Part 3: Inflation Impact Analysis", [
    "CPI Growth (2015-2025):",
    {"text": "Starting: CPI = 237.24", "level": 1},
    {"text": "Ending: CPI = 307.81", "level": 1},
    {"text": "Total Increase: 29.75%", "level": 1},
    {"text": "Annualized: ~2.5% per year", "level": 1},
    "",
    "Key Question:",
    "How much did inflation erode investment returns?"
])

# Slide 13: Total Returns Comparison
add_table_slide(
    "Total Returns: Nominal vs Real (2015-2025)",
    ["Rank", "Stock", "Nominal", "Real", "Inflation Impact"],
    [
        ["1", "MSFT", "+1,233%", "+938%", "-296%"],
        ["2", "LLY", "+954%", "+720%", "-234%"],
        ["3", "META", "+698%", "+521%", "-177%"],
        ["4", "LOW", "+314%", "+222%", "-92%"],
        ["5", "MCD", "+307%", "+217%", "-90%"],
        ["6", "LMT", "+191%", "+126%", "-65%"],
        ["7", "KO", "+139%", "+86%", "-53%"],
        ["8", "KEY", "+80%", "+40%", "-40%"],
        ["9", "LUV", "+4%", "-19%", "-23%"],
        ["10", "KHC", "-40%", "-53%", "-13%"]
    ]
)

# Slide 14: Critical Insights
add_content_slide("Critical Insights from Inflation Analysis", [
    "1. MSFT: The Winner",
    {"text": "Nominal: +1,233% | Real: +938%", "level": 1},
    {"text": "Tech growth >> inflation", "level": 1},
    "",
    "2. LUV: The Hidden Loser",
    {"text": "Nominal: +4% | Real: -19%", "level": 1},
    {"text": "Investors LOST purchasing power!", "level": 1},
    "",
    "3. KHC: The Disaster",
    {"text": "Nominal: -40% | Real: -53%", "level": 1},
    {"text": "Inflation made bad investment worse", "level": 1}
])

# Slide 15: Why It Matters
add_content_slide("Why Real Returns Matter", [
    "Real Returns = What Actually Matters",
    "",
    "1. Retirement Planning:",
    {"text": "Need real returns to maintain purchasing power", "level": 1},
    "",
    "2. Investment Selection:",
    {"text": "5% return with 3% inflation = only 2% real gain", "level": 1},
    "",
    "3. Long-term Wealth:",
    {"text": "Nominal gains are illusory if inflation keeps pace", "level": 1},
    "",
    "Portfolio Lesson:",
    {"text": "Growth stocks (MSFT, LLY, META) beat inflation", "level": 1},
    {"text": "Defensive stocks (KO, LUV, KEY) struggled", "level": 1}
])

# PART 4: CRYPTOCURRENCY ANALYSIS

# Slide 16: Crypto Introduction
add_content_slide("Part 4: Cryptocurrency Bar Sampling", [
    "Problem with Time Bars:",
    {"text": "Fixed time intervals (1 min, 1 hour, 1 day)", "level": 1},
    {"text": "Ignores market activity levels", "level": 1},
    "",
    "Solution: Information-Driven Sampling",
    {"text": "Sample based on market events, not time", "level": 1},
    {"text": "More samples during high activity", "level": 1},
    {"text": "Better statistical properties", "level": 1},
    "",
    "Group 3 Cryptocurrencies: BNB, DOGE, DOT"
])

# Slide 17: Four Bar Types
add_table_slide(
    "The Four Bar Sampling Methods",
    ["Bar Type", "Sampling Trigger", "What It Measures"],
    [
        ["Price Bars", "Fixed price change", "Volatility events"],
        ["Tick Bars", "Fixed # of trades", "Market activity/liquidity"],
        ["Volume Bars", "Fixed volume traded", "Participation level"],
        ["Dollar Bars", "Fixed $ value traded", "Economic significance"]
    ]
)

# Slide 18: Crypto Data Summary
add_table_slide(
    "Cryptocurrency Analysis Results",
    ["Crypto", "Avg Price", "Price Bars", "Tick Bars", "Volume Bars", "Dollar Bars"],
    [
        ["BNB", "$884.80", "27", "97", "96", "96"],
        ["DOT", "$1.97", "86", "96", "96", "95"],
        ["DOGE", "$0.13", "69", "96", "95", "95"]
    ]
)

# Slide 19: BNB Analysis
add_content_slide("BNB (Binance Coin) - Most Stable", [
    "Price Bars: 27 (fewest)",
    {"text": "Price Range: $750 - $960 (22%)", "level": 1},
    {"text": "Indicates: Very stable price movement", "level": 1},
    "",
    "Key Observation:",
    {"text": "27 vs ~96 for other bar types", "level": 1},
    {"text": "High volume within narrow price bands", "level": 1},
    {"text": "Large concentrated moves", "level": 1},
    "",
    "Investment Profile:",
    {"text": "Lower risk, institutional behavior", "level": 1},
    {"text": "Exchange token stability", "level": 1}
])

# Slide 20: DOGE Analysis
add_content_slide("DOGE (Dogecoin) - Most Volatile", [
    "Price Bars: 69 (2.5x more than BNB)",
    {"text": "Price Range: $0.09 - $0.16 (54%)", "level": 1},
    {"text": "Indicates: High volatility", "level": 1},
    "",
    "Key Observation:",
    {"text": "Meme coin showing frequent price swings", "level": 1},
    {"text": "Similar activity levels as others", "level": 1},
    {"text": "Retail-driven, sentiment-based", "level": 1},
    "",
    "Investment Profile:",
    {"text": "High risk, speculative", "level": 1},
    {"text": "Social media sensitive", "level": 1}
])

# Slide 21: DOT Analysis
add_content_slide("DOT (Polkadot) - Moderate Volatility", [
    "Price Bars: 86 (moderate)",
    {"text": "Price Range: $1.40 - $2.34 (48%)", "level": 1},
    {"text": "Indicates: Balanced volatility", "level": 1},
    "",
    "Key Observation:",
    {"text": "Middle ground between BNB and DOGE", "level": 1},
    {"text": "More stable than meme coins", "level": 1},
    {"text": "More volatile than exchange tokens", "level": 1},
    "",
    "Investment Profile:",
    {"text": "Medium risk", "level": 1},
    {"text": "Mix of retail and institutional", "level": 1},
    {"text": "Project fundamentals matter", "level": 1}
])

# Slide 22: Volatility Ranking
add_content_slide("Key Insight: Price Bars Reveal Volatility", [
    "Volatility Ranking (from 3,000 hourly bars):",
    "",
    {"text": "BNB: 27 price bars → MOST STABLE ✓", "level": 1, "size": 20},
    {"text": "DOGE: 69 price bars → MODERATE-HIGH", "level": 1, "size": 20},
    {"text": "DOT: 86 price bars → HIGHEST", "level": 1, "size": 20},
    "",
    "Surprising Finding:",
    {"text": "All had ~95 tick/volume/dollar bars", "level": 1},
    {"text": "Similar trading activity levels", "level": 1},
    {"text": "But vastly different price stability!", "level": 1},
    "",
    "Implication: 3x difference in bar counts = 3x difference in volatility"
])

# Slide 23: Return Distributions
add_content_slide("Return Distribution Analysis", [
    "All cryptos showed NEGATIVE returns:",
    {"text": "BNB: -0.09% to -0.25%", "level": 1},
    {"text": "DOGE: -0.22% to -0.31%", "level": 1},
    {"text": "DOT: -0.15% to -0.17%", "level": 1},
    "",
    "Market Context:",
    {"text": "Data: Last ~4 months", "level": 1},
    {"text": "Bearish crypto market period captured", "level": 1},
    "",
    "Distribution Quality:",
    {"text": "Dollar bars: Most normal distributions", "level": 1},
    {"text": "Best for statistical modeling", "level": 1}
])

# Slide 24: Why Dollar Bars Win
add_table_slide(
    "Bar Type Comparison: Statistical Properties",
    ["Bar Type", "Normal Distribution?", "ML Suitability", "i.i.d. Properties"],
    [
        ["Price Bars", "❌ Often bimodal", "Poor", "Weak"],
        ["Tick Bars", "⚠️ Somewhat", "Moderate", "Moderate"],
        ["Volume Bars", "✅ Better", "Good", "Good"],
        ["Dollar Bars", "✅✅ Best", "Excellent", "Strong"]
    ]
)

# Slide 25: Practical Applications
add_content_slide("Practical Applications for Trading", [
    "Use Price Bars when:",
    {"text": "Setting stop-losses based on price movement", "level": 1},
    {"text": "Comparing volatility across assets", "level": 1},
    "",
    "Use Tick Bars when:",
    {"text": "High-frequency trading", "level": 1},
    {"text": "Detecting unusual activity patterns", "level": 1},
    "",
    "Use Volume Bars when:",
    {"text": "Volume-based strategies (VWAP)", "level": 1},
    {"text": "Identifying institutional flows", "level": 1},
    "",
    "Use Dollar Bars when:",
    {"text": "Building ML models", "level": 1},
    {"text": "Professional algorithmic trading", "level": 1}
])

# PART 5: CONCLUSIONS

# Slide 26: Major Findings
add_content_slide("Major Findings Summary", [
    "1. Returns Analysis:",
    {"text": "Simple ≈ Log returns (correlation >0.998)", "level": 1},
    "",
    "2. Volatility Analysis:",
    {"text": "Range: 18% (KEY) to 40% (KO)", "level": 1},
    {"text": "COVID-19: 3-4x volatility spikes", "level": 1},
    "",
    "3. Inflation Impact:",
    {"text": "CPI +29.75% over 10 years", "level": 1},
    {"text": "Eroded 40-296% of nominal gains", "level": 1},
    "",
    "4. Cryptocurrency Bars:",
    {"text": "Price bars reveal volatility (27 vs 86)", "level": 1},
    {"text": "Dollar bars best for ML", "level": 1}
])

# Slide 27: Investment Insights
add_content_slide("Investment Insights: Winners & Losers", [
    "Best Performers (2015-2025):",
    {"text": "1. MSFT: +1,233% nominal, +938% real", "level": 1},
    {"text": "2. LLY: +954% nominal, +720% real", "level": 1},
    {"text": "3. META: +698% nominal, +521% real", "level": 1},
    "",
    "Worst Performers:",
    {"text": "1. KHC: -40% nominal, -53% real", "level": 1},
    {"text": "2. LUV: +4% nominal, -19% real (!))", "level": 1},
    {"text": "3. KEY: +80% nominal, +40% real", "level": 1},
    "",
    "Lesson: Growth stocks crushed inflation"
])

# Slide 28: Methodological Insights
add_content_slide("Why This Analysis Matters", [
    "1. Returns Calculation:",
    {"text": "Log returns are time-additive (crucial)", "level": 1},
    "",
    "2. Volatility Understanding:",
    {"text": "Rolling volatility reveals regime changes", "level": 1},
    {"text": "Crisis periods need different management", "level": 1},
    "",
    "3. Inflation Adjustment:",
    {"text": "Real returns show true wealth creation", "level": 1},
    {"text": "Essential for long-term planning", "level": 1},
    "",
    "4. Bar Sampling Innovation:",
    {"text": "Information-driven bars improve signal quality", "level": 1},
    {"text": "Critical for modern algorithmic trading", "level": 1}
])

# Slide 29: Recommendations
add_content_slide("Practical Recommendations", [
    "For Portfolio Construction:",
    {"text": "1. Diversify across volatility profiles", "level": 1},
    {"text": "2. Focus on inflation-beating returns (>5%)", "level": 1},
    {"text": "3. Monitor rolling volatility for timing", "level": 1},
    {"text": "4. Use log returns for time series", "level": 1},
    "",
    "For Quantitative Strategies:",
    {"text": "1. Use dollar bars for ML features", "level": 1},
    {"text": "2. Calculate returns from info-driven bars", "level": 1},
    {"text": "3. Test on multiple bar types", "level": 1},
    {"text": "4. Validate on inflation-adjusted returns", "level": 1}
])

# Slide 30: Key Takeaways
add_content_slide("Key Takeaways", [
    "1. Mathematical equivalence:",
    {"text": "Simple ≈ Log for daily, but log is superior", "level": 1},
    "",
    "2. Volatility reality:",
    {"text": "Not constant, clusters in crises", "level": 1},
    "",
    "3. Inflation matters:",
    {"text": "Can turn nominal gains into real losses", "level": 1},
    "",
    "4. Growth wins:",
    {"text": "MSFT, LLY, META crushed inflation", "level": 1},
    "",
    "5. Bar innovation:",
    {"text": "Dollar bars >> time bars for modeling", "level": 1}
])

# Slide 31: Final Thought
add_content_slide("Conclusions", [
    "Modern portfolio analysis requires moving",
    "beyond simple price charts.",
    "",
    "Understanding:",
    {"text": "• Returns calculation methods", "level": 1},
    {"text": "• Volatility dynamics", "level": 1},
    {"text": "• Inflation impact", "level": 1},
    {"text": "• Advanced sampling methods", "level": 1},
    "",
    "...is essential for successful investing",
    "in today's markets.",
    "",
    "Questions?"
])

# Save presentation
prs.save('/home/user/MSBA350Homework1/G3_Homework2_Presentation.pptx')
print("PowerPoint presentation created successfully!")
print("File: G3_Homework2_Presentation.pptx")
print(f"Total slides: {len(prs.slides)}")
