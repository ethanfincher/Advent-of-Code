import numpy as np
lights_grid = np.array([list(line) for line in open("2015/18/input.txt").read().strip().split("\n")])
grid_shape = lights_grid.shape

# Part 2
corners = [(0,0),(0, grid_shape[1]-1),(grid_shape[0]-1,0),(grid_shape[0]-1, grid_shape[1]-1)]
for corner in corners:
    lights_grid[corner] = "#"

def animate_lights():
    new_grid = lights_grid.copy()
    deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for index, value in np.ndenumerate(lights_grid):
        if index in corners:
            continue
        # get neighbors
        neighbors = []
        for d in deltas:
            neighbor_index = (index[0] + d[0], index[1] + d[1])
            # check if pos is in bounds
            if 0 <= neighbor_index[0] < grid_shape[0] and 0 <= neighbor_index[1] < grid_shape[1]:
                neighbors.append(lights_grid[neighbor_index])
        # if a light is on and 2 or 3 nieghbors are also on, then keep the light on, else turn it off
        if value == "#":
            new_grid[index] = "#" if neighbors.count("#") in [2,3] else "."
        # if a light is off and exaclty 3 neighbors are on, turn the light on, else keep it off
        elif value == ".":
            new_grid[index] = "#" if neighbors.count("#") == 3 else "."
    return new_grid

for _ in range(100):
    lights_grid = animate_lights()

print(np.sum(lights_grid == '#'))