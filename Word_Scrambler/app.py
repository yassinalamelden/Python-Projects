import random

print("WORD SCRAMBLER")

while True:
    word = input("\n Enter a word scramble ('or quit'):")
    if word.lower() == "quit":
        print("Goodbye!")
        break
    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {"".join(letters)}")
    