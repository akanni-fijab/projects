food_items={
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine" : 50,
    "orange": 80,
    "peach": 60,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine":50,
    "watermelon":80,
    "pear":100,

}

get_food_item = input("Item: ").lower()

if get_food_item in food_items:
    print(f"Calories: {food_items[get_food_item]}")
else:
    print()