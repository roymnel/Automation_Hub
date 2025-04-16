# Profit and Loss Calculator CLI
def calculate_profit_or_loss():
    try:
        revenue = float(input("Enter total revenue ($): "))
        expenses = float(input("Enter total expenses ($): "))
        profit = revenue - expenses
        if profit > 0:
            print(f"✅ Profit: ${profit:.2f}")
        elif profit < 0:
            print(f"❌ Loss: ${abs(profit):.2f}")
        else:
            print("⚖️ Break-even: No profit, no loss.")
    except ValueError:
        print("❌ Please enter valid numbers.")

if __name__ == "__main__":
    calculate_profit_or_loss()
