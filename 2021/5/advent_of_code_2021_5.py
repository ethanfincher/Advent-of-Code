import re
raw_input = open("2021\\5\\input.txt", "r").read().strip().split("\n")
pipe_coordinate_groups = []
for row in raw_input:
    row_regex = re.search(r'^(\d*),(\d*) -> (\d*),(\d*)', row)
    pipe_coordinate_groups.append((int(row_regex.group(1)), int(row_regex.group(2)), int(row_regex.group(3)), int(row_regex.group(4))))

pipe_spots = []

for coordinates in pipe_coordinate_groups:
    if coordinates[0] == coordinates[2]:
        for i in range(min(coordinates[1],coordinates[3]), max(coordinates[1],coordinates[3])+1): 
            pipe_spots.append(f'{coordinates[0]},{i}')
    elif coordinates[1] == coordinates[3]:
        for i in range(min(coordinates[0],coordinates[2]), max(coordinates[0],coordinates[2])+1): 
            pipe_spots.append(f'{i},{coordinates[1]}')
    elif abs(coordinates[0] - coordinates[2]) == abs(coordinates[1] - coordinates[3]):
        for i in range(abs(coordinates[0] - coordinates[2])+1):
            pipe_spots.append(f'{coordinates[0]-i if coordinates[0]>coordinates[2] else coordinates[0]+i},{coordinates[1]-i if coordinates[1]>coordinates[3] else coordinates[1]+i}')
counter = 0
for spot in set(list(pipe_spots)):
    if pipe_spots.count(spot) > 1: counter += 1
print(counter)