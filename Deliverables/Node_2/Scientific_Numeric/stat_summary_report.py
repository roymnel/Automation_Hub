# Statistical Summary Report for CSV Data
import pandas as pd

def summarize(csv_path):
    try:
        df = pd.read_csv(csv_path)
        numeric = df.select_dtypes(include='number')
        if numeric.empty:
            print("No numeric data found.")
            return
        summary = numeric.describe()
        print("\nStatistical Summary:\n")
        print(summary)
        summary.to_csv("stat_summary.csv")
        print("\n✅ Summary saved as stat_summary.csv")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    path = input("Enter CSV file path: ").strip()
    summarize(path)
