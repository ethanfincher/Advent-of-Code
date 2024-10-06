import re
# Part 1
with open("2020-20\\input.txt", "r") as tfile:
    # string of tiles, their numbers and new lines
    raw_tiles = [tile.split("\n") for tile in tfile.read().strip().split("\n\n")]
    # list of strings representing tiles
    whole_tiles = [tile[1:] for tile in raw_tiles]
    # numers that match the tile in the corresponding index
    tile_numbers = [int(re.search(r' (\d*):', tile[0]).group(1)) for tile in raw_tiles]
    # list of sides (left top right bottom) of each tile, index still matches
    tile_sides = []
# for each tile, get 4 sides
for index, tile in enumerate(whole_tiles):
    left_top_right_bottom = ["".join([row[0] for row in tile]), tile[0], "".join([row[-1] for row in tile]), tile[-1]]
    tile_sides.append(left_top_right_bottom)
# this is a flattened list of all sides found, to make it easier to search through
all_sides = [j for sub in tile_sides for j in sub]

# final counter, mulitplying the 4 corners, so starts at 1
final_product = 1

# for each tile (looping through the tile sides list)
for index, sides in enumerate(tile_sides):
    # this makes a list that we can search through that exludes the current 4 sides from the list
    all_sides_but_current = all_sides[:index*4] + all_sides[index*4+4:]
    # check each side and see if it matches another on the all sides list
    left = sides[0] in all_sides_but_current or sides[0][::-1] in all_sides_but_current
    top = sides[1] in all_sides_but_current or sides[1][::-1] in all_sides_but_current
    right = sides[2] in all_sides_but_current or sides[2][::-1] in all_sides_but_current
    bottom = sides[3] in all_sides_but_current or sides[3][::-1] in all_sides_but_current
    # if the tile is a corner piece, update the final product
    if ((top and left and not bottom and not right) or 
        (top and right and not bottom and not left) or
        (bottom and left and not top and not right) or
        (bottom and right and not top and not left)):
        final_product = final_product * tile_numbers[index]
print(final_product)