import numpy as np
import re

lines = open("2016/8/input.txt").read().strip().split("\n")

tall, wide = 6,50
grid = np.full((tall, wide), ".")

def get_digits(string_to_search):
    return [int(num) for num in re.search(r'.*?(\d+).*?(\d+)', string_to_search).groups()]

for i, line in enumerate(lines):
    if "rect" in line:
        x, y = get_digits(line)
        grid[0:y, 0:x] = "#"
    elif "rotate row" in line:
        row, row_change = get_digits(line)
        new_left = grid[row, -row_change:].copy()
        new_right = grid[row, :wide-row_change].copy()
        grid[row, :row_change] = new_left
        grid[row, -(wide-row_change):] = new_right
    elif "rotate column" in line:
        col, col_change = get_digits(line)
        new_top = grid[-col_change:, col].copy()
        new_bottom = grid[:tall-col_change, col].copy()
        grid[:col_change, col] = new_top
        grid[-(tall-col_change):, col] = new_bottom


print(np.sum(grid == "#"))
# To help readability in the final txt file, add a space every 5 columns (control+alt)
np.savetxt(f"./2016/8/final_grid.txt", grid, fmt="%s", delimiter="")