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
print(len(flipped_positions))