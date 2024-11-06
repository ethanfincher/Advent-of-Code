import re
import math
raw_min_max = re.findall(r"[-\d]+", open("2021/17/input.txt").read().strip())
x_min_max = (int(raw_min_max[0]), int(raw_min_max[1]))
y_min_max = (int(raw_min_max[2]), int(raw_min_max[3]))

# Part 1, took me wayyyyyy longer then it should have
def sum_of_ints(number):
    return int(number * (number + 1) / 2)
print(sum_of_ints(abs(y_min_max[0]) - 1))