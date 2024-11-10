import re
lines = open("2015/5/input.txt").read().strip().split("\n")
# Part 1
counter_a = 0
for line in lines:
    if len(re.findall(r'[aeiou]', line)) >= 3 and re.search(r'(\w)\1+', line) and not re.search(r'ab|cd|pq|xy', line):
        counter_a += 1
# print(counter_a)

# Part 2
counter_b = 0
for line in lines:
    rule_1 = False
    rule_2 = False
    for index, char in enumerate(line[:-1]):
        if line.count(f"{char}{line[index+1]}") >= 2:
            rule_1 = True
        if index + 2 < len(line) and line[index+2] == char:
            rule_2 = True
    if rule_1 and rule_2:
        counter_b += 1
print(counter_b)