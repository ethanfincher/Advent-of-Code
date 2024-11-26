import re
import math
ingredients = [[int(num) for num in re.findall(r"[-\d]+", line)] for line in open("2015/15/input.txt").read().strip().split("\n")]

all_totals = [0]

def find_combo(current_combo):
    # for numbers 0 through 100 (max ingredients)
    for i in range(101):
        # new combo is old combo plus the new number of the next ingredient
        new_combo = current_combo + [i]
        # if the sum of ingredients in the current combo is greater then 100, dont continue
        if sum(new_combo) <= 100:
            # if the number of ingredients in the current combo is less then 4, go to the next ingredient
            if len(new_combo) < 4:
                find_combo(new_combo)
            # otherwise, if all ingridients have been added and the sum is == 100
            elif sum(new_combo) == 100:
                # create a list of 0s for each ingredient property
                property_totals = [0 for _ in range(len(ingredients[0]))]
                # for each ingredient
                for ingredient_index, ingredient in enumerate(ingredients):
                    # add (to prop_totals) the prod of the current number of each prop in the current ingredient times the number of that ingredient in the current combo
                    for i in range(len(property_totals)):
                        property_totals[i] += ingredient[i] * new_combo[ingredient_index]
                # Part 2 checks for caleries to be 500
                if property_totals[-1] == 500:
                    all_totals.append((math.prod([max(prop, 0) for prop in property_totals[:-1]])))
                
find_combo([])
print(max(all_totals))