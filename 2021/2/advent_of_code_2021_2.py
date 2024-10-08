import re
# Part 1
commands = open("2021\\2\\input.txt", "r").read().strip().split("\n")
horizontal = 0
depth = 0
# for command in commands:
#     num = int(re.search(r'\d+', command).group(0))
#     if "up" in command:
#         depth -= num
#     elif "down" in command:
#         depth += num
#     elif "forward" in command:
#         horizontal += num
#     else:
#         print("something went wrong")
# print(horizontal*depth)

# Part 2
aim = 0
for command in commands:
    num = int(re.search(r'\d+', command).group(0))
    if "up" in command:
        aim -= num
    elif "down" in command:
        aim += num
    elif "forward" in command:
        horizontal += num
        depth = depth + (aim*num)
print(horizontal*depth)