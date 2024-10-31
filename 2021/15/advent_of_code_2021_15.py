import numpy as np
cave = np.array([[int(num) for num in list(line)] for line in open("2021\\15\\input.txt").read().strip().split("\n")])

# add dimensions to cave for part 2
original_size = cave.shape
# add horizontal dimensions
for i in range(4):
    new_array = cave[:, i*(original_size[1]):] + 1
    # Change all 10s to 1s
    new_array[new_array == 10] = 1
    cave = np.hstack((cave, new_array))
# add vertical dimensions
for j in range(4):
    new_array = cave[j*(original_size[0]):, :] + 1
    # Change all 10s to 1s
    new_array[new_array == 10] = 1
    cave = np.vstack((cave, new_array))

# stays the same for part 2, takes about 5 seconds
max_size = cave.shape
# Looks like dijkstra is the way to go
shortest_paths = {index:10000000000 for index in np.ndindex(cave.shape)}
shortest_paths[(0,0)] = 0
really_big = 10000000000000000
queue = {(0,0): shortest_paths[(0,0)]}

while queue:
    current_position = min(queue, key=queue.get)
    del queue[current_position]
    neighbors = [(current_position[0]-a, current_position[1]-b) for (a,b) in [(1,0),(-1,0),(0,1),(0,-1)] if 0 <= current_position[0]-a < max_size[0] and 0 <= current_position[1]-b < max_size[1]]
    for neighbor in neighbors:
        if shortest_paths[current_position] + cave[neighbor] < shortest_paths[neighbor]:
            shortest_paths[neighbor] = shortest_paths[current_position] + cave[neighbor]
            queue[neighbor] = shortest_paths[neighbor]
print(shortest_paths[(max_size[0]-1, max_size[1]-1)])