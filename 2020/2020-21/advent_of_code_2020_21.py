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
# get all unique allergens and ingredients (for later)
all_allergens = list(set([allergen for allergens in [recipe["allergens"] for recipe in recipes] for allergen in allergens]))
all_ingredients = [ingredient for ingredients in [recipe["ingredients"] for recipe in recipes] for ingredient in ingredients]

allergen_translations = {}
# for each alergen allergen
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
    # for each allergen key:val
    for key in allergen_translations:
            # if the value is a string, move on (already found)
            if type(allergen_translations[key]) == list:
                # remove item_to_remove
                allergen_translations[key] = [value for value in allergen_translations[key] if value != item_to_remove]
    # loop through again, if there is an allergen with only one possibility, set it and remove the val (call recursivly)
    for key in allergen_translations:
        if type(allergen_translations[key]) == list:
            if len(allergen_translations[key]) == 1:
                allergen_translations[key] = allergen_translations[key][0]
                remove_from_allergen_possibilities(allergen_translations[key])

# using a while with index to make things simple
index = 0
# while there are any lists left in translations dict (list means single val not found yet)
while any(type(value) == list for value in allergen_translations.values()):
    key = list(allergen_translations.keys())[index]
    # skip index if translation already found
    if type(allergen_translations[key]) != list: continue
    remaining_ingredient_posibilities = [ingredient for ingredients in allergen_translations.values() if type(ingredients) == list for ingredient in ingredients]
    # ingredients with only one in list
    singleton_ingredients = [ingredient for ingredient in allergen_translations[key] if remaining_ingredient_posibilities.count(ingredient) == 1]
    # if more then one possibility, continue
    if len(singleton_ingredients) != 1:
        index += 1
        continue
    else:
        # otherwise, set key value to string and remove from all allergen lists
        allergen_translations[key] = singleton_ingredients[0]
        remove_from_allergen_possibilities(singleton_ingredients[0])
        # reset index
        index = 0

print(len([ingredient for ingredient in all_ingredients if ingredient not in allergen_translations.values()]))

# Part 2
# sort vals by key
sorted_dict = {key: value for key, value in sorted(allergen_translations.items())}
print(",".join([value for value in sorted_dict.values()]))