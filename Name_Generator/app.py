import random

print("FANTASY NAME GENERATOR")

first_part = ["Sky", "Moon", "Star", "Sun", "Fire", "Ice"]
last_part = ["rider", "hunter", "walker", "dancer", "seeker", "keeper", "singer"]

count = int(input("How many names do you want? "))

for i in range(count):
    first_name = random.choice(first_part)
    last_name = random.choice(last_part)
    print(f"{first_name}{last_name}")
