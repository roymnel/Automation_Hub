# Temperature Converter (Celsius ↔ Fahrenheit)
def convert_temp():
    try:
        scale = input("Convert from (C/F): ").strip().upper()
        temp = float(input("Enter temperature: "))
        if scale == "C":
            result = (temp * 9/5) + 32
            print(f"{temp:.1f}°C = {result:.1f}°F")
        elif scale == "F":
            result = (temp - 32) * 5/9
            print(f"{temp:.1f}°F = {result:.1f}°C")
        else:
            print("❌ Invalid scale. Use 'C' or 'F'.")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    convert_temp()
