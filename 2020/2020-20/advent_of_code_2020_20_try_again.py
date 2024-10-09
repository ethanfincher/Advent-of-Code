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

def matching_tile(edge_to_match, original_tile, side_to_match=None):
    for tile in [tile for tile in tiles if not np.array_equal(tile, original_tile)]:
        edges = extract_edges(tile)
        if np.any(np.all(edges == edge_to_match, axis=1)) or np.any(np.all(edges == edge_to_match[::-1], axis=1)): 
            if side_to_match != None:
                for _ in range(4):
                    if np.array_equal(extract_edges(tile)[side_to_match], edge_to_match): 
                        return tile
                    tile = np.rot90(tile)
                tile = tile[::-1, :]
                for _ in range(4):
                    if np.array_equal(extract_edges(tile)[side_to_match], edge_to_match): 
                        return tile
                    tile = np.rot90(tile)
                exit()

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

tile_grid = tile_grid[:, :, 1:-1, 1:-1]
original_shape = np.shape(tile_grid)
combined_square_size = original_shape[0] * original_shape[2]
combined_grid = np.empty((combined_square_size, combined_square_size), dtype=object)
for tr_index, tile_row in enumerate(tile_grid):
    for tc_index, tile_col in enumerate(tile_row):
        for pr_index, pixel_row in enumerate(tile_col):
            for pc_index, pixel_col in enumerate(pixel_row):
                combined_grid[tr_index*original_shape[2] + pr_index][tc_index*original_shape[2] + pc_index] = pixel_col

combined_grid = np.rot90(combined_grid)
combined_grid = np.rot90(combined_grid)
combined_grid = np.rot90(combined_grid)