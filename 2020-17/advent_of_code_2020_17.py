import numpy as np
# Part 1
with open("2020-17\\input.txt", "r") as tfile:
    starting_grid = [[[list(row) for row in tfile.read().strip().split("\n")]]]
np_cube_grid = np.array(starting_grid)
for i in range(6):
    np_cube_grid = np.pad(np_cube_grid, pad_width=1, mode='constant', constant_values='.')
    np_cube_grid_copy = np_cube_grid.copy()
    with np.nditer(np_cube_grid, flags=['multi_index']) as cubes:
        for value in cubes:
            # Get the current position (indices) in the array
            position = cubes.multi_index
            x_start = max(position[0] - 1, 0)
            x_end = min(position[0] + 2, np_cube_grid.shape[0])
            y_start = max(position[1] - 1, 0)
            y_end = min(position[1] + 2, np_cube_grid.shape[1])
            z_start = max(position[2] - 1, 0)
            z_end = min(position[2] + 2, np_cube_grid.shape[2])
            a_start = max(position[3] - 1, 0)
            a_end = min(position[3] + 2, np_cube_grid.shape[3])
            neighbors = np_cube_grid[x_start:x_end, y_start:y_end, z_start:z_end, a_start:a_end].flatten()
            active_neighbors = np.sum(neighbors == '#')
            if value == "#":
                # the current cube is included in the neighbor list still, so remove one active to account
                active_neighbors -= 1
                if active_neighbors in (2,3):
                    np_cube_grid_copy[position] = "#"
                else: 
                    np_cube_grid_copy[position] = "."
            else:
                if active_neighbors == 3:
                    np_cube_grid_copy[position] = "#"
                else: 
                    np_cube_grid_copy[position] = "."
    np_cube_grid = np_cube_grid_copy
print(sum(np_cube_grid.flatten() == "#"))

# Part 2 was very simple given part 1, just add an additional 4th dimension (a)