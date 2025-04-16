# CSV Column Checker - Lists all column headers
import pandas as pd

def list_csv_columns(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\n📊 Columns found:")
        for col in df.columns:
            print(" -", col)
    except Exception as e:
        print("❌ Error reading CSV:", e)

if __name__ == "__main__":
    path = input("Enter path to CSV file: ").strip()
    list_csv_columns(path)
