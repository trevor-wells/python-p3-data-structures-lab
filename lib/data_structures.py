spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [item["name"] for item in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = [item for item in spicy_foods if item["heat_level"] > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶' * item['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food = [item for item in spicy_foods if item["cuisine"] == cuisine]
    return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat_levels = [item["heat_level"] for item in spicy_foods]
    total_heat = 0
    for i in range(len(heat_levels)):
        total_heat += heat_levels[i]
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    pass
