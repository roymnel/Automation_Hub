# Invoice Splitter - Divide a total invoice among clients
def split_invoice():
    try:
        total = float(input("Enter total invoice amount ($): "))
        clients = int(input("Enter number of clients to split across: "))
        if clients <= 0:
            print("❌ Client count must be positive.")
            return
        share = total / clients
        print(f"Each client owes: ${share:.2f}")
    except ValueError:
        print("❌ Please enter valid numeric values.")

if __name__ == "__main__":
    split_invoice()
