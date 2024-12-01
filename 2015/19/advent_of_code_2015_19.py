import re
from collections import defaultdict
from functools import lru_cache


input_parts = open("2015/19/input.txt").read().strip().split("\n\n")
replacement_strings = input_parts[0].split("\n")
starting_string = input_parts[1]
    
# Part 1
# replacements = defaultdict(list)
# for line in replacement_strings:
#     line_parts = line.split(" => ")
#     replacements[line_parts[0]].append(line_parts[1])
# unique_molecules = set()
# for index in range(len(starting_string)):
#     one_char = starting_string[index]
#     if one_char in replacements:
#         for replacement in replacements[one_char]:
#             unique_molecules.add(starting_string[:index] + replacement + starting_string[index+1:])
#     if index < len(starting_string)-2:
#         two_chars = starting_string[index] + starting_string[index+1]
#         if two_chars in replacements:
#             for replacement in replacements[two_chars]:
#                 unique_molecules.add(starting_string[:index] + replacement + starting_string[index+2:])

# print(len(unique_molecules))

# Part 2
replacements = {}
for line in replacement_strings:
    line_parts = line.split(" => ")
    replacements[line_parts[1]] = line_parts[0]

@lru_cache()
def simplify_molecule(current_string, steps):
    min_steps = 10000000000
    print(current_string)
    if current_string == "e":
        return steps
    if current_string.count("e") != 0:
        return None
    else:
        for index, char in enumerate(current_string):
            for replacement in replacements:
                if current_string[index: index+len(replacement)] == replacement:
                    new_step_count = simplify_molecule(f"{current_string[:index]}{replacements[replacement]}{current_string[index+len(replacement):]}", steps+1)
                    if new_step_count and new_step_count < min_steps:
                        min_steps = new_step_count
        return min_steps

print(simplify_molecule("starting_string", 0))