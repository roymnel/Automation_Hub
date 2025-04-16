# Monthly Budget Tracker
def track_budget():
    try:
        income = float(input("Enter total income for the month: $"))
        rent = float(input("Rent: $"))
        groceries = float(input("Groceries: $"))
        utilities = float(input("Utilities: $"))
        transport = float(input("Transport: $"))
        other = float(input("Other expenses: $"))

        expenses = rent + groceries + utilities + transport + other
        balance = income - expenses

        print("\n📊 Budget Summary:")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Remaining Balance: ${balance:.2f}")
        if balance < 0:
            print("❌ You're over budget!")
        else:
            print("✅ You're within budget.")
    except ValueError:
        print("❌ Invalid input. Please enter numbers.")

if __name__ == "__main__":
    track_budget()
