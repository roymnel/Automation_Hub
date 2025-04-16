# Typing Speed Test CLI
import time

TEST_PHRASE = "The quick brown fox jumps over the lazy dog."

def typing_test():
    print("⌨️ Type the following:")
    print(TEST_PHRASE)
    input("Press Enter when ready...")
    start = time.time()
    typed = input("> ")
    end = time.time()

    elapsed = end - start
    words = len(typed.split())
    wpm = (words / elapsed) * 60

    print(f"\n⏱️ Time: {elapsed:.2f} seconds")
    print(f"💨 Speed: {wpm:.2f} words per minute")

    if typed.strip() == TEST_PHRASE:
        print("✅ Perfect match!")
    else:
        print("⚠️ Text did not match exactly.")

if __name__ == "__main__":
    typing_test()
