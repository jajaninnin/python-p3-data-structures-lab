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
    name_list = []
    for food in spicy_foods:
        food_name = food.get('name')
        print(food_name)
        name_list.append(food_name)
    return name_list

def get_spiciest_foods(spicy_foods):
    spicy = []
    for food in spicy_foods:
        spice_level = food.get('heat_level')
        if spice_level > 5:
            print(food)
            spicy.append(food)
    return spicy


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name')
        cusine = food.get('cuisine')
        spice_level = food.get('heat_level')
        spicy = (spice_level) * ("🌶")
        print(name + " (" + cusine + ")" + " | Heat Level: " + spicy)
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    result = {}
    for food in spicy_foods:
        cuisine_dict = food.get('cuisine')
        if cuisine_dict == cuisine:
            result = food
    return result

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name')
        cusine = food.get('cuisine')
        spice_level = food.get('heat_level')
        if spice_level > 5:
            spicy = (spice_level) * ("🌶")
            print(name + " (" + cusine + ")" + " | Heat Level: " + spicy)

def get_average_heat_level(spicy_foods):
    count = 0
    total = 0
    for food in spicy_foods:
        spice_level = food.get('heat_level')
        total += spice_level 
        count += 1
    average = total / count
    return average

def create_spicy_food(spicy_foods, spicy_food):
    # spicy_food = {
    #     'name': "Griot",
    #     'cuisine': "Haitian",
    #     'heat_level': 10,
    # }
    spicy_foods.append(spicy_food)
    return spicy_foods