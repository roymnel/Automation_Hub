# health_assistant.py
# 💡 AI Health Assistant – Personalized Metrics Simulator
# Requires: pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import random
import datetime

def generate_fake_health_data(days=30):
    data = {
        "date": [datetime.date.today() - datetime.timedelta(days=i) for i in range(days)],
        "resting_heart_rate": [random.randint(60, 75) for _ in range(days)],
        "sleep_hours": [round(random.uniform(6.0, 9.0), 1) for _ in range(days)],
        "steps": [random.randint(4000, 12000) for _ in range(days)],
        "stress_level": [random.randint(1, 10) for _ in range(days)]
    }
    return pd.DataFrame(data)

def analyze_health(data):
    print("📊 Health Summary:")
    print(data.describe())
    
    high_stress_days = data[data["stress_level"] > 7]
    avg_sleep = data["sleep_hours"].mean()
    avg_heart_rate = data["resting_heart_rate"].mean()

    print(f"\n🧠 Days with high stress (>7): {len(high_stress_days)}")
    print(f"😴 Average sleep: {avg_sleep:.2f} hrs")
    print(f"❤️ Average resting heart rate: {avg_heart_rate:.1f} bpm")

    if avg_sleep < 7:
        print("⚠️ Recommendation: Increase nightly sleep to at least 7.5 hrs.")
    if avg_heart_rate > 72:
        print("⚠️ Consider light cardio to improve heart efficiency.")
    if len(high_stress_days) > 5:
        print("⚠️ Try meditation or deep breathing exercises.")

def plot_health(data):
    data.set_index("date").sort_index().plot(
        subplots=True, figsize=(10, 8), title="📈 30-Day Health Trends"
    )
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("🩺 Generating personalized health report...")
    df = generate_fake_health_data()
    analyze_health(df)
    plot_health(df)

