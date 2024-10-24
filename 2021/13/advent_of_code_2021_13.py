import re
import numpy as np
input_parts = open("2021\\13\\input.txt").read().strip().split("\n\n")
# puts coordinates into (x,y)
coordinates = [tuple(map(int, coordinate.split(','))) for coordinate in input_parts[0].split("\n")]
# puts folds in ("x or y", num)
folds = [(re.search(r'(\w)=', text).group(1), int(re.search(r'=(\d*)$', text).group(1))) for text in input_parts[1].split("\n")]

# populates paper
paper = np.full((max(coordinate[1] for coordinate in coordinates)+1, max(coordinate[0] for coordinate in coordinates)+1), '.')
for dot in coordinates:
    paper[dot[::-1]] = "#"

for fold in folds:
    if fold[0] == "y":
        # cuts paper in half, inverses first half
        first_half = paper[:fold[1]][::-1]
        second_half = paper[fold[1]+1:]
        # correct sides are matching now, replace # in first half
        for index, value in np.ndenumerate(second_half):
            if value == "#":
                first_half[index] = value
        # re-inverse to correctly orient paper, then assign back
        paper = first_half[::-1]
    # this does the same thing except for the columns, cuz numpy is awesome
    elif fold[0] == "x":
        first_half = paper[:, :fold[1]][:, ::-1]
        second_half = paper[:, fold[1]+1:]
        for index, value in np.ndenumerate(second_half):
            if value == "#":
                first_half[index] = value
        paper = first_half[:, ::-1]
print(np.count_nonzero(paper == "#"))
np.savetxt('2021\\13\\camera-code.txt', paper, fmt='%s', delimiter=' ')
