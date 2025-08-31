import random

print("Random Recipe Generator")

proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies = ["broccoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs = ["rice", "pasta", "potatos", "quinoa", "bread"]
methods = ["baked", "grilled", "stir-fried", "roasted", "sauteed"]
flavors = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]

while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(f"\nYour random recipe: {flavor} {method} {protein} with {veggie} and {carb}")

    if not input(f"\nGenerate aanother one? (y/n): ").lower().startswith("y"):
        print("Goodbye")
        break
