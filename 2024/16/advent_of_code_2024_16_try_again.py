import numpy as np

grid = np.array([list(line) for line in open("2024/16/input.txt").read().strip().split("\n")])
start = list(zip(*np.where(grid == "S")))[0]
end = list(zip(*np.where(grid == "E")))[0]
dots = list(zip(*np.where(grid == ".")))
unvisited = [start] + dots + [end]

neighbor_deltas = [(0,1),(1,0),(0,-1),(-1,0)]
def calc_distances(unvisited_nodes: list, start_index, start_direction):
    distances = {index: 100000000 for index in unvisited_nodes}
    distances[start_index] = 0
    to_check = {start_index: 0}
    while unvisited_nodes:
        current_node = min(to_check, key=to_check.get)
        next_indexes = [(current_node[0] + d[0], current_node[1] + d[1]) for d in neighbor_deltas if grid[(current_node[0] + d[0], current_node[1] + d[1])] != "#"]
    