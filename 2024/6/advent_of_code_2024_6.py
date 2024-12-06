import numpy as np
import time
import threading
grid = open("2024/6/input.txt").read().strip().split("\n")
grid = [list(line) for line in grid]
grid = np.array(grid)
grid_size = grid.shape

starting_position = tuple(np.argwhere(grid == "^")[0])
grid[starting_position] = "."

direction_deltas = [
    (-1, 0), # Up, 0
    (0, 1), # Right, 1
    (1, 0), # Down, 2
    (0, -1)  # Left, 3
]

current_direction = 0
def walk_guard(current_grid, current_position):
    current_direction = 0
    positions_walked = []
    reps_on = False
    current_rep = []
    last_rep = []
    rep_direction = None
    while True:
        new_position = (current_position[0] + direction_deltas[current_direction][0], current_position[1] + direction_deltas[current_direction][1])
        if len(current_rep) > 10000:
            return None
        if not (0 <= new_position[0] < grid_size[0] and 0 <= new_position[1] < grid_size[1]):
            return len(set(positions_walked))
        elif current_grid[new_position] == ".":
            if reps_on:
                current_rep.append(new_position)
            positions_walked.append(new_position)
            current_position = new_position
        elif current_grid[new_position] in ["#", "0"]:
            if current_grid[new_position] == "0":
                if not reps_on: rep_direction = current_direction
                reps_on = True
                if current_direction == rep_direction:
                    if last_rep and last_rep == current_rep:
                        return None
                    else:
                        last_rep = current_rep.copy()
                        current_rep = []

            current_direction = (current_direction+1) % 4

total_obstacles = 0
for index, value in np.ndenumerate(grid):
    print(index)
    temp_grid = grid.copy()
    temp_grid[index] = "0"
    current_outcome = walk_guard(temp_grid, starting_position)
    if current_outcome == None:
        total_obstacles += 1
print(total_obstacles)