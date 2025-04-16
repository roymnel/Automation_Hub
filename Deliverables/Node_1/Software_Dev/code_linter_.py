# Dummy Python Code Linter

def lint(filename):
    try:
        with open(filename) as f:
            for i, line in enumerate(f, 1):
                if len(line) > 79:
                    print(f"Line {i} too long ({len(line)} chars)")
    except Exception as e:
        print("Error reading file:", e)

if __name__ == "__main__":
    lint(input("Enter .py file path: "))
