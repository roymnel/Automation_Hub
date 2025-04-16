# ai_learning_tutor.py
# 📚 Adaptive Learning Tutor – Personalized Learning Curve Generator
# Requires: pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import random

def simulate_learning_sessions(num_days=30):
    data = {
        "Day": list(range(1, num_days + 1)),
        "Time_Spent_Min": [random.randint(20, 90) for _ in range(num_days)],
        "Quiz_Score_%": [round(random.uniform(55, 100), 1) for _ in range(num_days)],
        "Focus_Level_10": [random.randint(5, 10) for _ in range(num_days)]
    }
    return pd.DataFrame(data)

def evaluate_learning(data):
    print("📊 Learning Report:")
    print(data.tail())

    avg_score = data["Quiz_Score_%"].mean()
    avg_focus = data["Focus_Level_10"].mean()
    avg_time = data["Time_Spent_Min"].mean()

    print(f"\n📚 Avg Quiz Score: {avg_score:.1f}%")
    print(f"🧠 Avg Focus Level: {avg_focus:.1f}/10")
    print(f"⏱️ Avg Study Time: {avg_time:.1f} min/session")

    if avg_score >= 85:
        print("🎉 Performance is excellent. Keep the current pace.")
    elif avg_score >= 70:
        print("⚠️ Consider increasing focus or session time.")
    else:
        print("🔁 Try smaller daily goals or alternate formats (video, flashcards).")

def plot_learning_progress(data):
    data.set_index("Day")[["Quiz_Score_%", "Focus_Level_10"]].plot(
        figsize=(10, 5), title="📈 Learning Progress Over Time", grid=True
    )
    plt.ylabel("Score / Focus Level")
    plt.xlabel("Day")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("🧑‍🏫 Simulating AI learning journey...")
    df = simulate_learning_sessions()
    evaluate_learning(df)
    plot_learning_progress(df)

