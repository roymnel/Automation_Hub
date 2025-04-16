# Circle Area & Circumference Calculator
import math

def calculate_circle_metrics():
    try:
        radius = float(input("Enter radius (cm): "))
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print(f"\n🟢 Radius: {radius:.2f} cm")
        print(f"📏 Area: {area:.2f} cm²")
        print(f"📐 Circumference: {circumference:.2f} cm")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    calculate_circle_metrics()
