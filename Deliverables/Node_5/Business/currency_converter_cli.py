# Currency Converter CLI (Static Rates)
def convert_currency():
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 151.3,
        "ZAR": 18.9
    }
    print("💱 Supported currencies:", ', '.join(rates.keys()))
    try:
        from_curr = input("From currency (e.g., USD): ").strip().upper()
        to_curr = input("To currency (e.g., EUR): ").strip().upper()
        amount = float(input("Amount: "))
        if from_curr not in rates or to_curr not in rates:
            print("❌ Unsupported currency.")
            return
        converted = amount * (rates[to_curr] / rates[from_curr])
        print(f"\n💰 {amount:.2f} {from_curr} = {converted:.2f} {to_curr}")
    except ValueError:
        print("❌ Please enter a valid amount.")

if __name__ == "__main__":
    convert_currency()
