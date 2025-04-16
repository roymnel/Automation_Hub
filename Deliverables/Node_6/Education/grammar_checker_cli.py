# Grammar Checker CLI (Keyword-based simulation)
def check_grammar(sentence):
    errors = []
    if "ain't" in sentence.lower():
        errors.append("⚠️ Informal: 'ain't' is not recommended.")
    if "i " in sentence.lower():
        errors.append("⚠️ Capitalization: 'I' should be uppercase.")
    if sentence.strip().endswith("because"):
        errors.append("⚠️ Sentence ends with 'because' — possibly incomplete.")
    return errors

if __name__ == "__main__":
    sentence = input("Enter a sentence: ").strip()
    issues = check_grammar(sentence)
    if not issues:
        print("✅ No obvious grammar issues.")
    else:
        print("\n".join(issues))
