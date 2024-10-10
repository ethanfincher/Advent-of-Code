import re
# Part 1
ingredients_input = open("2020\\2020-21\\input.txt").read().strip().split("\n")
recipes = []
# populate ingredients_and_allergens list
for ingredient in ingredients_input:
    new_recipe = {}
    ingredient_groups = re.search(r'^(.*)\(contains (.*)\)$', ingredient)
    new_recipe["ingredients"] = ingredient_groups.group(1).strip().split(" ")
    new_recipe["allergens"] = ingredient_groups.group(2).strip().split(", ")
    recipes.append(new_recipe)
# get all unique allergens
all_allergens = list(set([allergen for allergens in [recipe["allergens"] for recipe in recipes] for allergen in allergens]))
all_ingredients = [ingredient for ingredients in [recipe["ingredients"] for recipe in recipes] for ingredient in ingredients]

allergen_translations = {}
# for allergen
for allergen in all_allergens:
    allergen_translations[allergen] = []
    # get list of recipes with that allergen
    recipes_with_allergen = [recipe for recipe in recipes if allergen in recipe["allergens"]]
    # get list of all possible ingredients
    all_possible_ingredients = list(set([ingredient for ingredients in [recipe["ingredients"] for recipe in recipes_with_allergen] for ingredient in ingredients]))
    # for each ingredient, if every recipe has that ingredient, keep it in possibles, otherwise remove it
    for ingredient in all_possible_ingredients:
        if all(ingredient in recipe["ingredients"] for recipe in recipes_with_allergen):
            allergen_translations[allergen].append(ingredient)

def remove_from_allergen_possibilities(item_to_remove):
    for key in allergen_translations:
            if type(allergen_translations[key]) == list:
                allergen_translations[key] = [value for value in allergen_translations[key] if value != item_to_remove]
    for key in allergen_translations:
        if type(allergen_translations[key]) == list:
            if len(allergen_translations[key]) == 1:
                allergen_translations[key] = allergen_translations[key][0]
                remove_from_allergen_possibilities(allergen_translations[key])

index = 0
while any(type(value) == list for value in allergen_translations.values()):
    key = list(allergen_translations.keys())[index]
    if type(allergen_translations[key]) != list: continue
    remaining_ingredient_posibilities = [ingredient for ingredients in allergen_translations.values() if type(ingredients) == list for ingredient in ingredients]
    matching_ingredient = [ingredient for ingredient in allergen_translations[key] if remaining_ingredient_posibilities.count(ingredient) == 1]
    if len(matching_ingredient) != 1:
        index += 1
        continue
    else:
        allergen_translations[key] = matching_ingredient[0]
        remove_from_allergen_possibilities(matching_ingredient[0])
        index = 0

print(len([ingredient for ingredient in all_ingredients if ingredient not in allergen_translations.values()]))

# Part 2
sorted_dict = {key: value for key, value in sorted(allergen_translations.items())}
print(",".join([value for value in sorted_dict.values()]))