import json
lines = open("2015/8/input.txt").read().strip().split("\n")
character_total = 0
string_total = 0
for line in lines:
    line = json.dumps(line) # add this for part 2
    character_total += len(line)
    string_total += len(eval(line))
print(character_total - string_total)