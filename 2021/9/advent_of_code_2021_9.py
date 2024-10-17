import numpy as np
heightmap = np.array([list([int(num) for num in line]) for line in open("2021\\9\\input.txt").read().strip().split("\n")])
rows, cols = heightmap.shape
total = 0
for index, value in np.ndenumerate(heightmap):
    is_lowest = True
    neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for rd, cd in neighbors:
        row, col = index[0] + rd, index[1] + cd
        # if position is out of bounds or neighbor is less than current value, check the next
        if not (0 <= row < rows and 0 <= col < cols) or heightmap[row,col] > value:
            continue
        # otherwise, move onto next value
        else:
            is_lowest = False
            break
    # if value is lower then all its neighbors, add to total (+1)
    if is_lowest: 
        total += (value+1)
print(total)

# Part 2