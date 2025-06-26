import random

print("MUSIC RECOMMENDER")

genres = {
    "rock":["The Rolling", "GnR", "Queen", "Aerosmith", "Black Sabbath"],
    "pop":["Espresso", "Beautiful Things", "Die With A Smile", "One Of The Girls", "Starboy"],
    "hip-hop":["good kid", "All Eyez on Me", "The Message", "Juicy", "Humble "]
}

choice = input("What genre do you like? (rock/pop/hip-hop):")

if choice not in genres:
    print("Sorry, I don't know that genre.")
else:
    print(f"Check out! {random.choice(genres[choice])}")
