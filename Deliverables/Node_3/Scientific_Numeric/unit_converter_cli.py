# Unit Converter - Meters to Feet and Kilograms to Pounds
def convert_units():
    try:
        m = float(input("Enter meters: "))
        kg = float(input("Enter kilograms: "))
        feet = m * 3.28084
        pounds = kg * 2.20462
        print(f"\n📏 {m} meters = {feet:.2f} feet")
        print(f"⚖️ {kg} kilograms = {pounds:.2f} pounds")
    except ValueError:
        print("❌ Please enter valid numeric values.")

if __name__ == "__main__":
    convert_units()
