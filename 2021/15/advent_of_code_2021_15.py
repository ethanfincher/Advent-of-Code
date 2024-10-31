import numpy as np
import sys
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())
cave = np.array([[int(num) for num in list(line)] for line in open("2021\\15\\input.txt").read().strip().split("\n")])

exit_index = (cave.shape[0] - 1, cave.shape[1] - 1)
lowest_path_sum = 10000000000000000

def find_path(indexes_visited: list, total_value: int, current_index: tuple):
    global lowest_path_sum
    if total_value >= lowest_path_sum: return
    if current_index != (0,0):
        total_value += cave[current_index]
    if current_index == exit_index:
        if total_value < lowest_path_sum: 
            lowest_path_sum = total_value
    else:
        for delta in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current_index[0]-delta[0], current_index[1]-delta[1])
            if (0 <= neighbor[0] <= exit_index[0] and 0 <= neighbor[1] <= exit_index[1]) and neighbor not in indexes_visited:
                find_path(indexes_visited+[current_index], total_value, neighbor)
find_path([], 0, (0,0))
print(lowest_path_sum)