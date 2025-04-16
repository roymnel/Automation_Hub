# Periodic Table Quiz (CLI)
quiz = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "C": "Carbon",
    "O": "Oxygen"
}

score = 0
for symbol, name in quiz.items():
    answer = input(f"What element has the symbol '{symbol}'? ")
    if answer.strip().lower() == name.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer was {name}.\n")

print(f"🏁 Final Score: {score}/{len(quiz)}")
