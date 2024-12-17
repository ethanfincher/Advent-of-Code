import numpy as np
import sys

sys.setrecursionlimit(15000)

grid = np.array([list(line) for line in open("2024/16/input.txt").read().strip().split("\n")])
start = list(zip(*np.where(grid == "S")))[0]

best_score = 10000000000000000
neighbor_deltas = [(0,1),(1,0),(0,-1),(-1,0)]
def move_reindeer(current_position, indexes_visited: list, current_score, current_direction):
    global best_score
    if current_score > best_score: return
    for d in [delta for delta in neighbor_deltas if delta != (current_direction[0]*-1, current_direction[1]*-1)]:
        possible_spot = (current_position[0] + d[0], current_position[1] + d[1])
        if grid[possible_spot] == "#":
            continue
        elif grid[possible_spot] == "E":
            if current_score + 1 < best_score:
                best_score = current_score + 1
        else:
            if possible_spot not in indexes_visited:
                move_reindeer(possible_spot, indexes_visited+[current_position], current_score + 1 + (1000 if current_direction != d else 0), d)

move_reindeer(start, [], 0, (0,1))
print(best_score)