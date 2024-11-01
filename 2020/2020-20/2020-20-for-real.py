import numpy as np
import re
raw_tiles = open("2020\\2020-20\\input.txt").read().strip().split("\n\n")
numbers = [int(re.search(r'Tile (\d*):', tile).group(1)) for tile in raw_tiles]
tiles = np.array([[list(line)for line in tile.split("\n")[1:]] for tile in raw_tiles])
sides = {}
for index, tile in enumerate(tiles):
    sides[numbers[index]] = {"top": tile[0, :], "bottom": tile[-1, :], "left": tile[:, 0], "right": tile[:, -1]}
    
# this takes a couple seconds, but at this point I'm just gonna go for it
matching_sides = {}
# for each tile
for tile_number, tile_sides in sides.items():
    # find and label all matching sides
    matches = {"top": [], "bottom": [], "left": [], "right": [], }
    # go through each side name and its corresponding side (list of chars)
    for side_name, side in tile_sides.items():
        # then go through all other tiles, 
        for different_tile_number, different_tile_sides in sides.items():
            if different_tile_number == tile_number: continue
            # if any of its sides match, add it to matches
            if any(np.array_equal(side, different_side) or np.array_equal(side[::-1], different_side) for different_side in different_tile_sides.values()):
                matches[side_name].append(different_tile_number)
    matching_sides[tile_number] = matches

top_left = {key: value for key, value in matching_sides.items() if not value['top'] and not value['left']}
# you can get all 4 corners for part 1 from here, I'm going straight to part 2
quick_check = [item for sublist in [list(sides.values()) for sides in list(matching_sides.values())] for item in sublist if len(item) == 1]










# # start with top left (2971). the right side of 2981 matches with 1091
# # find which side of 1091 matches 2971 and do the same thing for the opposite side.
# def get_next_direction(direction):
#     return "left" if direction == "right" else "left" if direction == "right"
# def build_number_grid(current_number, direction, current_grid, index):
#     current_grid[index] = current_number
#     next_number = matching_sides[current_number][direction]
#     matching_direction = [key for key, value in matching_sides[next_number[0]].items() if current_number in value]

# build_number_grid(2971, "right", np.empty(tiles.shape), (0,0))