# Sales Tax Calculator
def calculate_tax():
    try:
        amount = float(input("Enter sale amount ($): "))
        tax_rate = float(input("Enter tax rate (%): "))
        tax = amount * (tax_rate / 100)
        total = amount + tax
        print(f"\n💵 Base: ${amount:.2f}")
        print(f"📈 Tax: ${tax:.2f}")
        print(f"💰 Total: ${total:.2f}")
    except ValueError:
        print("❌ Please enter valid numeric values.")

if __name__ == "__main__":
    calculate_tax()
