# Vocabulary Quiz
quiz = {
    "apple": "manzana",
    "dog": "perro",
    "car": "coche",
    "sun": "sol",
    "book": "libro"
}

score = 0
for eng, esp in quiz.items():
    ans = input(f"What is the Spanish for '{eng}'? ")
    if ans.strip().lower() == esp:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. It was {esp}")
print(f"Score: {score}/{len(quiz)}")
