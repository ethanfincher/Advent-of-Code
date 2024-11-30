import re
from collections import defaultdict


input_parts = open("2015/19/input.txt").read().strip().split("\n\n")
replacement_strings = input_parts[0].split("\n")
starting_string = input_parts[1]
replacements = {}
for line in replacement_strings:
    line_parts = line.split(" => ")
    replacements[line_parts[1]] = line_parts[0]

print(replacements)
    
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

