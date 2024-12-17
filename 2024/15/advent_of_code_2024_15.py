import numpy as np
raw_input = open("2024/15/input.txt").read().strip().split("\n\n")

starting_grid = raw_input[0].strip().split("\n")
for line_index, line in enumerate(starting_grid):
    line = line.replace("#", "##")
    line = line.replace("O", "[]")
    line = line.replace(".", "..")
    line = line.replace("@", "@.")
    starting_grid[line_index] = line
grid = np.array([list(line) for line in starting_grid])

current_index = list(zip(*np.where(grid == "@")))[0]
instructions = "".join(raw_input[1].strip().split("\n"))

for instruction_index, instruction in enumerate(instructions):
    # np.savetxt(f'2024/15/moves/{instruction_index}.txt', grid, fmt='%s', delimiter='')
    delta = (0,-1) if instruction == "<" else (-1,0) if instruction == "^" else (0,1) if instruction == ">" else (1,0)
    new_index = (current_index[0] + delta[0], current_index[1] + delta[1])
    # if next spot is a dot, just update current location
    if grid[new_index] == ".":
        grid[current_index] = "."
        grid[new_index] = "@"
        current_index = new_index
    # if its a #, then dont do anything
    elif grid[new_index] == "#":
        continue
    else:
        # instruction set for left and right
        if instruction in ["<", ">"]:
            moves = 0
            box_positions = []
            while True:
                # find the next index to check (so many spaces over)
                moves += 1
                next_index = (new_index[0] + delta[0]*moves, new_index[1] + delta[1]*moves)
                # if the currently checked space is a #, then you can't move
                if grid[next_index] == "#":
                    break
                # if its a dot, then move everything in the current direction
                elif grid[next_index] == ".":
                    # every [ turns into ]. the last position (currently .) depends on the direction your moving
                    grid[next_index] = "[" if instruction == "<" else "]"
                    grid[current_index] = "."
                    grid[new_index] = "@"
                    current_index = new_index
                    for box_pos in box_positions:
                        grid[box_pos] = "[" if grid[box_pos] == "]" else "]"
                    break
                else:
                    # if its another box, add it to list to (potentially) update later
                    box_positions.append(next_index)
        # instruction set for up and down
        elif instruction in ["v", "^"]:
            # need to find both squares of the current box
            box_positions = [new_index, (new_index[0], new_index[1] + (1 if grid[new_index] == "[" else -1))]
            # index to check will always be the spaces above or below the last boxes found
            indexes_to_check = [(box[0] + (-1 if instruction == "^" else 1), box[1]) for box in box_positions]
            while True:
                # list of new boxes found
                boxes_found = []
                for index_to_check in indexes_to_check:
                    # if any space above/below a box is a #, then you can't move any of them
                    if grid[index_to_check] == "#":
                        break
                    # if its a ., then continue through iterations
                    elif grid[index_to_check] == ".":
                        continue
                    else:
                        # if its another box, the we need to check above/below it next while loop. add it to box positions (all boxes) and boxes found (to find spaces to check next iteration)
                        boxes_found.append(index_to_check)
                        box_positions.append(index_to_check)
                        # also need to append boxes other side
                        boxes_found.append((index_to_check[0], index_to_check[1] + (1 if grid[index_to_check] == "[" else -1)))
                        box_positions.append((index_to_check[0], index_to_check[1] + (1 if grid[index_to_check] == "[" else -1)))
                # if no # were found above any boxes
                else:
                    # if no more boxes were found and all spaces above are empty
                    if not boxes_found:
                        # do the move. sort the list either acsending or decending based on direction (if moving up, need to move the ones on top so the dont get overidden by the bottom updates)
                        for p_index, box in enumerate(sorted(set(box_positions), key=lambda x: x[0], reverse= False if instruction == "^" else True)):
                            grid[(box[0] + (-1 if instruction == "^" else 1), box[1])] = grid[box]
                            grid[box] = "."
                        grid[new_index] = "@"
                        grid[current_index] = "."
                        current_index = new_index
                        # go to next direction
                        break
                    # if there were boxes
                    else:
                        # add all the next spots to check for next iteration based on boxes found this iteration and the current direction
                        indexes_to_check = [(box[0] + (-1 if instruction == "^" else 1), box[1]) for box in set(boxes_found)]
                        continue
                # only hits this if a # was found (and for loop broke via statement). because there was a # above one of the boxes, no boxes can be moved
                break

        # Part 1
        # while True:
        #     next_index = (new_index[0] + delta[0]*moves, new_index[1] + delta[1]*moves)
        #     if grid[next_index] == ".":
        #         grid[next_index] = "O"
        #         grid[current_index] = "."
        #         grid[new_index] = "@"
        #         current_index = new_index
        #         break
        #     elif grid[next_index] == "#":
        #         break
        #     else:
        #         moves += 1

# np.savetxt(f'2024/15/moves/end.txt', grid, fmt='%s', delimiter='')
gps_total = 0
all_boxes = list(zip(*np.where(grid == "[")))
for box in all_boxes:
    gps_total += box[0] * 100 + box[1]
print(gps_total)