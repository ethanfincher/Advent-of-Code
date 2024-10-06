import re
import numpy as np
# Part 1, but actually constructing the grid
with open("2020-20\\input.txt", "r") as tfile:
    # string of tiles, their numbers and new lines
    raw_tiles = [tile.split("\n") for tile in tfile.read().strip().split("\n\n")]
tiles = []
for tile in raw_tiles:
    new_tile = {}
    new_tile["number"] = re.search(r' (\d*):', tile[0]).group(1)
    new_tile["top"] = tile[1]
    new_tile["right"] = "".join([col[-1] for col in tile[1:]])
    new_tile["bottom"] = tile[-1]
    new_tile["left"] = "".join([col[0] for col in tile[1:]])
    new_tile["inside"] = [col[1:-1] for col in tile[2:-1]]
    print(new_tile)
    exit()
# find top left, start a new list
# from there, find the one that matches to the right, and append it to the list
# also have to reorient the tile
# do this until there are no more matches to the right, then find bottom of the top left match and repeat
# do this until there are no more matches at the right and the bottom