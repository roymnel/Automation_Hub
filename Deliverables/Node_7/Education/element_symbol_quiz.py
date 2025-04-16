# Element Symbol Quiz
quiz = {
    "Hydrogen": "H",
    "Oxygen": "O",
    "Nitrogen": "N",
    "Sodium": "Na",
    "Iron": "Fe"
}

score = 0
for element, symbol in quiz.items():
    guess = input(f"What is the symbol for {element}? ").strip()
    if guess.lower() == symbol.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer was {symbol}.\n")

print(f"🏁 Final Score: {score}/{len(quiz)}")
