# Triangle Area and Perimeter Solver
def solve_triangle():
    try:
        a = float(input("Enter side A length (cm): "))
        b = float(input("Enter side B length (cm): "))
        c = float(input("Enter side C length (cm): "))
        if a + b <= c or a + c <= b or b + c <= a:
            print("❌ Invalid triangle: violates triangle inequality.")
            return

        perimeter = a + b + c
        s = perimeter / 2  # semi-perimeter
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        print(f"\n📏 Perimeter: {perimeter:.2f} cm")
        print(f"📐 Area: {area:.2f} cm²")
    except ValueError:
        print("❌ Please enter valid side lengths.")

if __name__ == "__main__":
    solve_triangle()
