import statistics
import math
boxes = [[int(num) for num in box.split("x")] for box in open("2015/2/input.txt").read().strip().split("\n")]
total_paper = 0
for box in boxes:
    total_paper += (2 * box[0] * box[1]) + (2 * box[1] * box[2]) + (2 * box[2] * box[0]) + min([(box[0] * box[1]), (box[1] * box[2]), (box[2] * box[0])])
# print(total_paper)
total_ribbon = 0
for box in boxes:
    total_ribbon += (min(box) * 2 + statistics.median(box) * 2) + (math.prod(box))
print(total_ribbon)