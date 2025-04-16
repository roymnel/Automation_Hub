# Basic Multiplication Quiz
import random

def multiplication_quiz():
    score = 0
    for _ in range(5):
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        answer = a * b
        try:
            guess = int(input(f"What is {a} x {b}? "))
            if guess == answer:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. Answer: {answer}\n")
        except ValueError:
            print("❌ Invalid input.\n")
    print(f"🏁 Final Score: {score}/5")

if __name__ == "__main__":
    multiplication_quiz()
