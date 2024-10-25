import re
from collections import Counter
raw_input = open("2021\\14\\input.txt").read().strip().split("\n\n")
polymer = raw_input[0]
pairs = {}
for pair in raw_input[1].split("\n"):
    pair_regex = re.search(r"(\w\w) -> (\w)", pair)
    pairs[pair_regex.group(1)] = pair_regex.group(2)
for i in range(40):
    new_polymer = ""
    for index, char in enumerate(polymer[:len(polymer)-1]):
        current_pair = char + polymer[index+1]
        new_polymer += char
        if current_pair in pairs:
            new_polymer += pairs[current_pair]
    new_polymer += polymer[-1]
    polymer = new_polymer

print(max(Counter(polymer).values()) - min(Counter(polymer).values()))