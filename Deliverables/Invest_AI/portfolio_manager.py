# portfolio_manager.py
# 💼 AI Investment Portfolio Manager (Simulation Engine)
# Requires: pip install pandas matplotlib

import pandas as pd
import random
import matplotlib.pyplot as plt

def generate_fake_portfolio():
    assets = ["AAPL", "GOOGL", "TSLA", "AMZN", "MSFT", "NVDA"]
    weights = [random.uniform(0.05, 0.4) for _ in assets]
    total = sum(weights)
    weights = [round(w / total, 2) for w in weights]

    portfolio = pd.DataFrame({
        "Ticker": assets,
        "Weight": weights,
        "Annual_Return_%": [round(random.uniform(5, 20), 2) for _ in assets],
        "Volatility_%": [round(random.uniform(10, 35), 2) for _ in assets]
    })

    return portfolio

def analyze_portfolio(portfolio):
    print("📊 Portfolio Overview:")
    print(portfolio)

    expected_return = sum(portfolio["Weight"] * portfolio["Annual_Return_%"])
    volatility = sum(portfolio["Weight"] * portfolio["Volatility_%"])

    print(f"\n📈 Expected Annual Return: {expected_return:.2f}%")
    print(f"📉 Portfolio Volatility: {volatility:.2f}%")

    if expected_return > 12 and volatility < 20:
        print("✅ Portfolio is well-optimized for growth and stability.")
    elif expected_return < 8:
        print("⚠️ Consider reallocating into higher-return assets.")
    else:
        print("🧠 Portfolio is moderately aggressive. Review allocation.")

def plot_portfolio(portfolio):
    portfolio.set_index("Ticker")["Weight"].plot.pie(
        autopct='%1.1f%%', title="💰 Portfolio Allocation", figsize=(6, 6)
    )
    plt.ylabel("")
    plt.show()

if __name__ == "__main__":
    print("💼 Simulating AI-optimized portfolio...")
    df = generate_fake_portfolio()
    analyze_portfolio(df)
    plot_portfolio(df)

