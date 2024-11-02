import numpy as np
import re
import math
raw_tiles = open("2020\\2020-20\\input.txt").read().strip().split("\n\n")
numbers = [int(re.search(r'Tile (\d*):', tile).group(1)) for tile in raw_tiles]
tiles = np.array([[list(line) for line in tile.split("\n")[1:]] for tile in raw_tiles])
sides = {}

def get_edges(tile):
    return {"top": tile[0, :], "bottom": tile[-1, :], "left": tile[:, 0], "right": tile[:, -1]}

for index, tile in enumerate(tiles):
    sides[numbers[index]] = get_edges(tile)
    
# this takes a couple seconds, but at this point I'm just gonna go for it
matching_sides = {}
# for each tile
for tile_number, tile_sides in sides.items():
    # find and label all matching sides
    matches = {"top": 0, "bottom": 0, "left": 0, "right": 0}
    # go through each side name and its corresponding side (list of chars)
    for side_name, side in tile_sides.items():
        # then go through all other tiles, 
        for different_tile_number, different_tile_sides in sides.items():
            if different_tile_number == tile_number: continue
            # if any of its sides match, add it to matches
            if any(np.array_equal(side, different_side) or np.array_equal(side[::-1], different_side) for different_side in different_tile_sides.values()):
                matches[side_name] = different_tile_number
    matching_sides[tile_number] = matches
# you can get all 4 corners for part 1 from here, I'm going straight to part 2

# match all the numbers up first (to make sure im not going crazy)
top_left = {key: value for key, value in matching_sides.items() if not value['top'] and not value['left']}
# starting with the top left, get the first row of numbers

# make empty 2d number grid
number_grid = np.zeros(((int(math.sqrt(len(tiles)))), (int(math.sqrt(len(tiles))))))
number_grid_shape = number_grid.shape
number_grid[0,0] = list(top_left.keys())[0]

directions = ["top", "right", "bottom", "left"]
def make_number_grid(side_to_match, current_tile_number, matching_position, direction):
    print(f"current grid: \n{number_grid}")
    print(f"moving {direction}")
    # find which number is to the right of the current number
    matching_tile_number = matching_sides[current_tile_number][side_to_match]
    print(matching_sides[matching_tile_number])
    # assign that index
    number_grid[matching_position] = matching_tile_number
    print(f"number {matching_tile_number} matched")
    # find which side matches up
    matching_side = next((key for key, value in matching_sides[matching_tile_number].items() if value == current_tile_number))
    print(f"{matching_side} lines up")
    # find the opposite side and repeat. stop when the opposite side doesnt exist. when it doesnt, move down one, then find a match to the left
    # if going right and you hit the edge
    if direction == "right" and matching_position[1] == number_grid_shape[1] - 1:
        if matching_position[0] == number_grid_shape[0] - 1: return
        next_direction = "down"
        next_position = (matching_position[0] + 1, matching_position[1])
        next_side_to_match = directions[(directions.index(matching_side) - 1) % 3]
    # going left and hit the edge
    elif direction == "left" and matching_position[1] == 0:
        if matching_position[0] == number_grid_shape[0] - 1: return
        next_direction = "down"
        next_position = (matching_position[0] + 1, matching_position[1])
        next_side_to_match = directions[(directions.index(matching_side) + 1) % 3]
    # just moved down and are on right edge
    elif direction == "down" and matching_position[1] == number_grid_shape[1] - 1:
        next_direction = "left"
        next_position = (matching_position[0], matching_position[1] - 1)
        next_side_to_match = directions[(directions.index(matching_side) - 1) % 3]
    # just moved down and hit the left edge
    elif direction == "down" and matching_position[1] == 0:
        next_direction = "right"
        next_position = (matching_position[0], matching_position[1] + 1)
        next_side_to_match = directions[(directions.index(matching_side) + 1) % 3]
    # keep moving right or left
    else:
        next_direction = direction
        next_position = (matching_position[0], matching_position[1] + (1 if direction == "right" else -1))
        next_side_to_match = directions[(directions.index(matching_side) + 2) % 4]
    print(f"next tile needs to match {next_side_to_match} side")
    print()
    make_number_grid(next_side_to_match, matching_tile_number, next_position, next_direction)



make_number_grid("right", list(top_left.keys())[0], (0,1), "right")


# tiles_shape = tiles.shape
# tile_grid = np.empty((int(math.sqrt(tiles_shape[0])), int(math.sqrt(tiles_shape[0])), tiles_shape[1], tiles_shape[2]), dtype=object)
# tile_grid[0,0] = tiles[numbers.index(list(top_left.keys())[0])]

