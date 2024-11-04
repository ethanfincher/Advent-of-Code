# my last failure at least showed that every side only matches with one other side, I just messed up how I was doing it at some point, and didnt comment my code so its impossible to go back to
import re
import numpy as np
import math
# Create dictionary of tile_number: 2d array of tile
tiles_list = [tile.split("\n") for tile in open("2020\\2020-20\\input.txt").read().strip().split("\n\n")]
tiles = {int(re.search(r"Tile (\d*):", rows[0]).group(1)): np.array([list(row) for row in rows[1:]]) for rows in tiles_list}
possible_tiles = list(tiles.keys())

# Find top left corner
def get_edges(tile):
    # Top = 0, Right = 1, Bottom = 2, Left = 3
    return np.array((tile[0, :], tile[:, -1], tile[-1, :], tile[:, 0]))

# 3d list of all edges
all_edges = np.array([get_edges(tile) for tile in tiles.values()])
# flattens into 2d array
all_edges = all_edges.reshape(-1, all_edges.shape[-1])
# add inversions
all_edges = np.concatenate((all_edges, all_edges[:, ::-1]), axis=0)

# values are the actual tiles, keys are numbers
for number, tile in tiles.items():
    current_edges = get_edges(tile)
    # if top and left edges only show up in all edges once (just themselves, no matches), then that tile is top left
    if all((np.sum(np.all(all_edges == edge, axis=1)) == 1 for edge in [current_edges[0], current_edges[3]])):
        top_left = tile
        top_left_number = number
        break

# Create empty grid
# creates square of squares. outer square is sqrt the number of total tiles, inner squares are the same dimention as the top left tile
tile_grid = np.empty((int(math.sqrt(len(tiles_list))), int(math.sqrt(len(tiles_list))), len(top_left), len(top_left[0])), dtype='<U1')
# add top left to grid
tile_grid[0,0] = top_left
# once a tile has been added to the grid, remove it from possible tiles
possible_tiles.remove(top_left_number)

def find_matching_tile(starting_tile, match_right):
    # if we're matching to the right, starting side is the right side, and we're matching the left side of a tile to it
    if match_right:
        starting_side = get_edges(starting_tile)[1]
        side_to_match = 3
    # if we're not matching the right, then wer're matching the bottom, so sude to match is the top
    else: 
        starting_side = get_edges(starting_tile)[2]
        side_to_match = 0
    
    # find the matching tile
    for possible_tile_number in possible_tiles:
        possible_tile = tiles[possible_tile_number]
        if np.any(np.all((np.append(get_edges(possible_tile), get_edges(possible_tile)[:, ::-1], axis=0)) == starting_side, axis=1)):
            matching_tile = possible_tile
            # remove tile once its been found (since it will be added later and we have the number now)
            possible_tiles.remove(possible_tile_number)
            break
    # rotate the tile until the correct side matches the starting tile
    flips = 0
    while not np.array_equal(get_edges(matching_tile)[side_to_match], starting_side):
        # if this doesn't work, inverse and try again
        if flips == 4:
            matching_tile = matching_tile[:, ::-1]
            flips = 0
        else:
            matching_tile = np.rot90(matching_tile)
            flips += 1
    return matching_tile

for row in range(len(tile_grid)):
    # match, rotate, and add all tiles to the right of it
    for col in range(len(tile_grid[0])):
        # last col will have already been added
        if col != len(tile_grid[0]) - 1:
            tile_grid[row, col+1] = find_matching_tile(tile_grid[row, col], True)
    # then find the tile below the current tile, and repeat the steps until all tiles are added. dont go past last row
    if row != len(tile_grid) - 1:
        tile_grid[row+1, 0] = find_matching_tile(tile_grid[row, 0], False)

# removes borders of tiles
tile_grid = tile_grid[:, :, 1:-1, 1:-1]
# This turns the 4d array into a 2d array
original_shape = np.shape(tile_grid)
combined_square_size = original_shape[0] * original_shape[2]
combined_grid = np.empty((combined_square_size, combined_square_size), dtype=object)
for tr_index, tile_row in enumerate(tile_grid):
    for tc_index, tile_col in enumerate(tile_row):
        for pr_index, pixel_row in enumerate(tile_col):
            for pc_index, pixel_col in enumerate(pixel_row):
                combined_grid[tr_index*original_shape[2] + pr_index][tc_index*original_shape[2] + pc_index] = pixel_col

# # Write to a text file
# multi_line_string = '\n'.join(''.join(map(str, row)) for row in combined_grid)
# with open('array_output.txt', 'w') as f:
#     f.write(multi_line_string)

sea_monsters = 0
counter = 0
# this flips the picture if no sea monsters were found
while sea_monsters == 0:
    hash_count = 0
    total_spaces_checked = 0
    # this checks each hash, its inefficient, but works
    for index, value in np.ndenumerate(combined_grid):
        # try catch incase if all statement goes out of bounds
        try:
            if value == "#":
                # add all hashes, then subtract sea monsters at the end
                hash_count += 1
                # check for sea monsters
                if all(combined_grid[index[0]+location[0], index[1]+location[1]] == "#" for location in 
                        [(1,1), (1,0), (1,-1), (1,-6), (1,-7), (1,-12), (1,-13), (1,-18), (2,-2), (2,-5), (2,-8), (2,-11), (2,-14), (2,-17)]):
                    sea_monsters += 1
        except:
            continue
    # if the picture has been flipped 4 times, invert it
    if counter == 4: combined_grid = combined_grid[::-1]
    # otherwise, flip it
    else: combined_grid = np.rot90(combined_grid)
    counter += 1

print(hash_count - (sea_monsters*15))