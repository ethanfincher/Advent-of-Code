import re
import math
from collections import defaultdict

# Redid this with some light reading and suggestions from redit, learning how to aproach "make it faster" problems
raw_input = open("2021\\14\\input.txt").read().strip().split("\n\n")

string_polymer = raw_input[0]
# default dict is cool, its a short hand way of doing "if exists, add to total, else create and set equal"
current_polymer = defaultdict(int)
# create initial pairs
for index, letter in enumerate(string_polymer[:-1]):
    current_pair = letter + string_polymer[index+1]
    current_polymer[current_pair] += 1

pairs_template = {}
# parse pair template into a dict
for pair in raw_input[1].split("\n"):
    pair_regex = re.search(r"(\w\w) -> (\w)", pair)
    pairs_template[pair_regex.group(1)] = pair_regex.group(2)

# rather then saving the whole string in memory, since we dont care about positions we can just save totals
for i in range(40):
    new_polymer = defaultdict(int)
    for key, value in current_polymer.items():
        if key in pairs_template:
            new_letter = pairs_template[key]
            new_polymer[key[0]+new_letter] += value
            new_polymer[new_letter+key[1]] += value
    current_polymer = new_polymer

totals = defaultdict(int)
for key, value in current_polymer.items():
    totals[key[0]] += value
    totals[key[1]] += value

# totals will always be half of what was saved in the current polymer (except for the first and last char from the original polymer)
# we compensate for that with the math.ceil
totals = {k:math.ceil(v/2) for k,v in totals.items()}

print(max(totals.values()) - min(totals.values()))