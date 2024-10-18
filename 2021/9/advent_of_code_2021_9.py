import numpy as np
heightmap = np.array([list([int(num) for num in line]) for line in open("2021\\9\\input.txt").read().strip().split("\n")])
rows, cols = heightmap.shape
total = 0
low_points = []
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
        low_points.append(index)
        total += (value+1)
# print(total)

# Part 2
def find_lower(array, position):
    # save value of current position
    current_value = array[position]
    # change position to 10 (so we can count it later, and so it is never used twice)
    array[position] = 10
    # left top right bottom
    neighbors = [(-1,0),(0,-1),(0,1),(1,0)]
    for rd, cd in neighbors:
        row, col = position[0] + rd, position[1] + cd
        # if in bounds and the neighbor is greater then the current val, find_lower on it
        if (0 <= row < rows and 0 <= col < cols) and array[row,col] > current_value and array[row,col] != 9:
            find_lower(array, (row,col))

# saves all basin sizes (inefficient)
basin_sizes = []
# saves last basin total (counting 10s)
total_basin_counter = 0
for low_point in low_points:
    find_lower(heightmap, low_point)
    # number of 10s in current basin minus the total on the height map before calculating current basin
    current_basin_count = np.count_nonzero(heightmap == 10) - total_basin_counter
    basin_sizes.append(current_basin_count)
    # set to new total
    total_basin_counter = np.count_nonzero(heightmap == 10)

basin_sizes.sort()
# print(basin_sizes)
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
