import numpy as np
# with open("test.txt", 'w') as f:
    # pass  # This clears the file
levels = np.array([[int(char) for char in line] for line in open("2021\\11\\input.txt").read().strip().split("\n")])
rows, cols = levels.shape
neighbors = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
flashes = 0
def flash(levels_array, current_index, flash_list):
    # access global counter
    global flashes
    flashes += 1
    # set flashed index to 0, add it to flashed list
    levels_array[current_index] = 0
    flash_list.append(str(current_index))
    # check neighbors
    for rd, cd in neighbors:
        row, col = current_index[0] + rd, current_index[1] + cd
        if 0 <= row < rows and 0 <= col < cols:
            if levels_array[row, col] + 1 != 10:
                if str((row, col)) not in flash_list:
                    levels_array[row, col] += 1
            else:
                flash(levels_array, (row, col), flash_list)
steps = 0
# for i in range (100):
while not np.all(levels == 0):
    # keep track of which indexes have flashed
    already_flashed = []
    for index, level in np.ndenumerate(levels):
        if level + 1 != 10:
            # if they've flashed this step, then don't change from 0
            if str(index) not in already_flashed:
                levels[index] += 1
        else:
            flash(levels, index, already_flashed)
    steps += 1
    # with open("test.txt", 'a') as f:  # Open in append mode
    #     for row in levels:
    #         line = ''.join(map(str, row))
    #         f.write(line + '\n')
    #     f.write("\n")
# print(flashes)
print(steps)
# Part 1 is partially commented out