print("Reverse Nme Generator")

while True:
    name = input("\nEnter a name: ")

    if not name:
        break

    reverse_name = name[::-1]
    print(f"Your reversed name is {reverse_name}")
    print(f"In the parallel universe, they call you {reverse_name}")

    answer = input("\nTry another name? (y/n) ")
    if answer != "y":
        break

