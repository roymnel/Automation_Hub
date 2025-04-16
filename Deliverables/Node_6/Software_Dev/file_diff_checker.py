# File Difference Checker
def diff_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        print("\n🔍 Differences:")
        for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
            if line1 != line2:
                print(f"Line {i}:\n  → {line1.strip()}\n  ≠ {line2.strip()}")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    f1 = input("Enter first file path: ").strip()
    f2 = input("Enter second file path: ").strip()
    diff_files(f1, f2)
