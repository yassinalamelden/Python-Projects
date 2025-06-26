print("VOWEL COUNTER")

while True:
    text = input("\nEnter some text (or 'quit'): ")

    if text.lower() == "quit":
        print("Goodbye!")
        break

    vowel_count = 0
    for letter in text:
        if letter in ["a","i","e","o","u"]:
            vowel_count +=1
    print(f"That text has {vowel_count} vowels.")
