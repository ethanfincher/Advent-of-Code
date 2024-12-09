import numpy as np
grid = np.array([list(line) for line in open("2024/8/input.txt").read().strip().split("\n")])
grid_shape = grid.shape
unique_chars = np.unique(grid)

antinodes = []
for char in unique_chars:
    if char == ".": continue
    indexes = np.where(grid == char)
    # Combine the row and column indexes into coordinate pairs
    coordinates = list(zip(indexes[0], indexes[1]))

    for coordinate in coordinates:
        # part 2, each antenna is also an antinode now
        antinodes.append(coordinate)
        # for all other antennas of the same kind
        for other_coordinate in [c for c in coordinates if c != coordinate]:
            # find the dif between the 2, add it to the second antenna index to find the antinode index
            c_delta = (other_coordinate[0] - coordinate[0], other_coordinate[1] - coordinate[1])
            antinode_index = (other_coordinate[0] + c_delta[0], other_coordinate[1] + c_delta[1])
            # while the current antinode index is inbounds, add the indes to the antinodes list, and update to the next antinode index
            while 0 <= antinode_index[0] < grid_shape[0] and 0 <= antinode_index[1] < grid_shape[1]:
                antinodes.append(antinode_index)
                antinode_index = (antinode_index[0] + c_delta[0], antinode_index[1] + c_delta[1])

print(len(set(antinodes)))