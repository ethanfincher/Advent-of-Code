import re
import math
raw_min_max = re.findall(r"[-\d]+", open("2021/17/input.txt").read().strip())
x_min_max = (int(raw_min_max[0]), int(raw_min_max[1]))
y_min_max = (int(raw_min_max[2]), int(raw_min_max[3]))

# Part 1, took me wayyyyyy longer then it should have
# def sum_of_ints(number):
#     return int(number * (number + 1) / 2)
# print(sum_of_ints(abs(y_min_max[0]) - 1))

possible_y = []

for y in range(y_min_max[0], abs(y_min_max[0])):
    velocity = y
    position = 0
    steps = 0
    possible_steps = []
    while position >= y_min_max[0]:
        position += velocity
        velocity -= 1
        steps += 1
        if position in range(y_min_max[0], y_min_max[1]+1):
            possible_steps.append(steps)
    possible_y.append(possible_steps)

# not super efficient, but im dumn today and it works
def check_x(possible_steps):
    x_values = []
    for steps in possible_steps:
        for x in range (1, x_min_max[1]+1):
            starting_x = x
            total = 0
            for _ in range(steps):
                total += x
                x -= 1 if x != 0 else 0
            if x_min_max[0] <= total <= x_min_max[1]:
                x_values.append(starting_x)
    return len(set(x_values))

total = 0
for possible_steps in possible_y:
    total += check_x(possible_steps)
print(total)