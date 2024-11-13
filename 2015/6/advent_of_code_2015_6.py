import numpy as np
import re
# Part 1
# light_arrangement = np.zeros((1000, 1000), dtype=bool)
# for command in open("2015/6/input.txt").read().strip().split("\n"):
#     line_regex = re.search(r"(^[a-z ]+)(\d+),(\d+) through (\d+),(\d+)$", command)
#     words = line_regex.group(1).strip()
#     print(words)
#     light_arrangement[int(line_regex.group(2)):int(line_regex.group(4))+1, int(line_regex.group(3)):int(line_regex.group(5))+1] = True if words == "turn on" else False if words == "turn off" else ~light_arrangement[int(line_regex.group(2)):int(line_regex.group(4))+1, int(line_regex.group(3)):int(line_regex.group(5))+1]
# print(len([light for light in light_arrangement.flatten() if light]))

# Part 2
light_arrangement = np.zeros((1000, 1000), dtype=int)

for command in open("2015/6/input.txt").read().strip().split("\n"):
    line_regex = re.search(r"(^[a-z ]+)(\d+),(\d+) through (\d+),(\d+)$", command)
    
    # Extract the command type and coordinates
    words = line_regex.group(1).strip()
    x1, y1 = int(line_regex.group(2)), int(line_regex.group(3))
    x2, y2 = int(line_regex.group(4)), int(line_regex.group(5))
    # gpt gave me this, love it
    slice_range = slice(x1, x2+1), slice(y1, y2+1)

    # Update the light arrangement based on the command
    if words == "turn on":
        light_arrangement[slice_range] += 1
    elif words == "turn off":
        light_arrangement[slice_range] = np.maximum(light_arrangement[slice_range] -1, 0)
    elif words == "toggle":
        light_arrangement[slice_range] += 2

# Sum up the total brightness
print("Total brightness:", np.sum(light_arrangement))