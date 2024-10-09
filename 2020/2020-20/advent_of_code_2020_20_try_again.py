import re
import math
import numpy as np
# Part 1, but actually constructing the grid
with open("2020\\2020-20\\input.txt", "r") as tfile:
    # string of tiles, their numbers and new lines
    raw_tiles = [tile.split("\n") for tile in tfile.read().strip().split("\n\n")]
tile_grid_size = int((math.sqrt(len(raw_tiles))))
tile_size = len(raw_tiles[0][1])
tiles = []
for raw_tile in raw_tiles:
    tiles.append(np.array([list(line) for line in raw_tile[1:]]))

def extract_edges(tile):
    top = tile[0, :]
    bottom = tile[-1, :]
    left = tile[:, 0]
    right = tile[:, -1]
    return top, bottom, left, right
already_used = []
def matching_tile(edge_to_match, original_tile, side_to_match=None):
    for index, tile in enumerate([tile for tile in tiles if not np.array_equal(tile, original_tile)]):
        edges = extract_edges(tile)
        if np.any(np.all(edges == edge_to_match, axis=1)) or np.any(np.all(edges == edge_to_match[::-1], axis=1)): 
            if side_to_match != None:
                for _ in range(4):
                    if np.array_equal(extract_edges(tile)[side_to_match], edge_to_match): 
                        del tiles[index]
                        return tile
                    tile = np.rot90(tile)
                tile = tile[::-1, :]
                for _ in range(4):
                    if np.array_equal(extract_edges(tile)[side_to_match], edge_to_match): 
                        del tiles[index]
                        return tile
                    tile = np.rot90(tile)
            return tile
    return None

tile_grid = np.empty((tile_grid_size,tile_grid_size,tile_size,tile_size), dtype=object)
for tile in tiles:
    edges = extract_edges(tile)
    if not isinstance(matching_tile(edges[0], tile), np.ndarray) and not isinstance(matching_tile(edges[2], tile), np.ndarray): tile_grid[0][0] = tile


for index, row in enumerate(tile_grid[:-1]):
    current_tile = row[0]
    edges = extract_edges(current_tile)
    tile_grid[index+1][0] = matching_tile(edges[1], current_tile, 0)

for r_index, row in enumerate(tile_grid):
    for c_index, col in enumerate(row[:-1]):
        current_tile = col
        edges = extract_edges(current_tile)
        tile_grid[r_index][c_index+1] = matching_tile(edges[3], current_tile, 2)


# tile_grid = tile_grid[:, :, 1:-1, 1:-1]
original_shape = np.shape(tile_grid)
combined_square_size = original_shape[0] * original_shape[2]
combined_grid = np.empty((combined_square_size, combined_square_size), dtype=object)
for tr_index, tile_row in enumerate(tile_grid):
    for tc_index, tile_col in enumerate(tile_row):
        for pr_index, pixel_row in enumerate(tile_col):
            for pc_index, pixel_col in enumerate(pixel_row):
                combined_grid[tr_index*original_shape[2] + pr_index][tc_index*original_shape[2] + pc_index] = pixel_col

multi_line_string = '\n'.join(' '.join(map(str, row)) for row in combined_grid)

# Write to a text file
with open('array_output.txt', 'w') as f:
    f.write(multi_line_string)
# sea_monsters = 0
# counter = 0
# while sea_monsters == 0:
#     hash_count = 0
#     total_spaces_checked = 0
#     for index, value in np.ndenumerate(combined_grid):
#         try:
#             if value == "#":
#                 hash_count += 1
#                 if all(combined_grid[index[0]+location[0], index[1]+location[1]] == "#" for location in 
#                         [(1,1), (1,0), (1,-1), (1,-6), (1,-7), (1,-12), (1,-13), (1,-18), (2,-2), (2,-5), (2,-8), (2,-11), (2,-14), (2,-17)]):
#                     sea_monsters += 1
#         except:
#             continue
#     if counter == 4: combined_grid = combined_grid[::-1]
#     else: combined_grid = np.rot90(combined_grid)
#     counter += 1
# print(np.shape(tile_grid))
# print(np.shape(combined_grid))
# print(total_spaces_checked)
# print(sea_monsters)
# print(hash_count)
