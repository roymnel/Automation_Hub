# BMI Calculator (Metric)
def calculate_bmi():
    try:
        height_cm = float(input("Enter your height in cm: "))
        weight_kg = float(input("Enter your weight in kg: "))
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        print(f"\n📏 Your BMI is {bmi:.2f}")
        if bmi < 18.5:
            print("⚠️ Underweight")
        elif 18.5 <= bmi < 25:
            print("✅ Normal weight")
        elif 25 <= bmi < 30:
            print("⚠️ Overweight")
        else:
            print("🚨 Obese")
    except ValueError:
        print("❌ Please enter valid numbers.")

if __name__ == "__main__":
    calculate_bmi()
