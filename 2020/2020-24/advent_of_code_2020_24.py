raw_lines = open("2020\\2020-24\\input.txt").read().strip().split("\n")

instructions = []
for line in raw_lines:
    instruction = []
    while len(line) != 0:
        if line[0] not in ("n", "s"):
            instruction.append(line[0])
            line = line[1:]
        else:
            instruction.append(line[0:2])
            line = line[2:]
    instructions.append(instruction)

flipped_positions = []
for instruction in instructions:
    x = 0
    y = 0
    for move in instruction:
        if move == "e": x += 1
        elif move == "w": x -= 1
        # if your moving vertically and to the right, if the current y is odd, add one to x
        elif move == "ne":
            if y % 2 == 1: x += 1
            y += 1
        elif move == "se":
            if y % 2 == 1: x += 1
            y -= 1
        # if your moving vertically and to the left, if the current y is even, add one to x
        elif move == "nw":
            if y % 2 == 0: x -= 1
            y += 1
        elif move == "sw":
            if y % 2 == 0: x -= 1
            y -= 1
    if (x,y) in flipped_positions: 
        flipped_positions.remove((x,y))
    else: 
        flipped_positions.append((x,y))
# print(len(flipped_positions))

# Part 2
def get_neighbors(position):
    x,y = position
    neighbors = [(x-1,y),(x+1,y)]
    # if y is odd
    if y % 2 == 1:
        # add x and x+1
        neighbors.extend([(x,y-1),(x+1,y-1),(x,y+1),(x+1,y+1)])
    # if y is even
    else:
        # add x and x-1
        neighbors.extend([(x,y-1),(x-1,y-1),(x,y+1),(x-1,y+1)])
    return neighbors

for _ in range(100):
    new_positions = []
    for position in flipped_positions:
        flipped_neighbors = 0
        for neighbor in get_neighbors(position):
            # if tile is currently flipped
            if neighbor in flipped_positions:
                flipped_neighbors += 1
            # if its not, check it to see if there are exactly 2 flipped tiles next to it. if so, flip it
            else:
                # this part is slow but works, so im just gonna let it be for now
                if neighbor not in new_positions and len([position for position in get_neighbors(neighbor) if position in flipped_positions]) == 2:
                    new_positions.append(neighbor)
        # if a black tile has 0 for more then 2 flipped neighbors, flip it back to white
        if flipped_neighbors not in (0,3,4,5,6):
            new_positions.append(position)
    flipped_positions = (new_positions)

print(len(flipped_positions))