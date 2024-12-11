import numpy as np
grid = np.array([[int(num) for num in list(line)] for line in open("2024/10/input.txt").read().strip().split("\n")])
grid_shape = grid.shape

neighbor_deltas = [(-1,0), (0,-1), (1,0), (0,1)]

def go_down_trail(current_num, current_index):
    good_trails = []
    for d in neighbor_deltas:
            r, c = current_index[0]+d[0], current_index[1]+d[1]
            if 0 <= r < grid_shape[0] and 0 <= c < grid_shape[1]:
                if current_num == 8 and grid[r,c] == 9:
                    print(9, (r,c))
                    good_trails.append((r,c))
                elif grid[r,c] == current_num+1:
                    good_trails.extend(go_down_trail(current_num+1, (r,c)))
    return good_trails

hiking_scores = []
for index, num in np.ndenumerate(grid):
    if num == 0:
        # Part 1
        hiking_scores.append(len(set((go_down_trail(0, index)))))
        # Part 2
        hiking_scores.append(len((go_down_trail(0, index))))

print(sum(hiking_scores))