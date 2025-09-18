import time

print("\n COUNTDOWN TIMER")
print("Count down from your chosen seconds! ")

while True:
    try:
        seconds = int(input("\n Enter seconds to countdown from: "))

        #Validate input
        if seconds <= 0:
            print("Please enter a positive number.")
            continue

        print(f"Starting countdown from {seconds} seconds!")

        for i in range(seconds, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("\n COUNTDOWN COMPLETE!")

        again = input("\n Start another countdown? (y/n): ").lower()
        if not again.startswith("y"):
            print("Thank you, Goodbye! ")
            break
    except ValueError:
        print("Please enter a number.")

