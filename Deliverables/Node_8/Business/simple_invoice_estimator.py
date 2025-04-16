# Simple Invoice Estimator
def estimate_invoice():
    try:
        num_items = int(input("Number of items/services: "))
        total = 0
        for i in range(1, num_items + 1):
            desc = input(f"Item {i} description: ")
            price = float(input(f"Item {i} price ($): "))
            total += price
        tax_rate = float(input("Tax rate (%): "))
        tax = total * (tax_rate / 100)
        grand_total = total + tax
        print(f"\n📋 Subtotal: ${total:.2f}")
        print(f"📈 Tax: ${tax:.2f}")
        print(f"💰 Grand Total: ${grand_total:.2f}")
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    estimate_invoice()
