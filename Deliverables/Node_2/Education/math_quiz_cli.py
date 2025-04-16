# Simple Math Quiz CLI App
import random

def ask_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = a + b
    try:
        user_input = int(input(f"What is {a} + {b}? "))
        if user_input == answer:
            print("✅ Correct!\n")
            return True
        else:
            print(f"❌ Wrong. The correct answer is {answer}.\n")
            return False
    except ValueError:
        print("Please enter a valid number.\n")
        return False

if __name__ == "__main__":
    score = 0
    for _ in range(5):
        if ask_question():
            score += 1
    print(f"Final Score: {score}/5")
