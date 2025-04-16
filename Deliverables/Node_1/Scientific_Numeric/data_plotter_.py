# Line Chart Plotter
import pandas as pd
import matplotlib.pyplot as plt

def plot(csv):
    df = pd.read_csv(csv)
    numeric = df.select_dtypes(include='number')
    if numeric.empty:
        print("No numeric columns found.")
        return
    numeric.plot(title="Line Chart from CSV")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot(input("CSV file path: "))
