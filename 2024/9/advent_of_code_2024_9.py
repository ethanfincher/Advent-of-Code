disk = open("2024/9/input.txt").read().strip()

# Part 1
# blocks = []
# file_num = 0
# # this creates a list of numbers and dots, each one is a single element
# for index, num in enumerate(disk):
#     # if it is a file
#     if index % 2 == 0:
#         blocks.extend([str(file_num)] * int(num))
#         file_num += 1
#     # if it is free space
#     else:
#         blocks.extend(["."] * int(num))
# # copy to alter, need to pop later
# blocks_copy = blocks.copy()
# ordered_blocks = []
# block_index = 0
# # every time we either come across a number, we either continue or add it to ordered blocks
# # so when ordered blocks contains every number, we have finished sorting
# while len(ordered_blocks) < len([char for char in blocks if char != "."]):
#     char = blocks[block_index]
#     # if current char is a number, no need to move anything, so add it and continue on
#     if char != ".":
#         ordered_blocks.append(char)
#     # if it is a dot, swap it out with the last number on the blocks list (copy we made)
#     else:
#         # we do this by popping chars off of the back of the copies list until we hit a number, then add that to ordered blocks
#         last_char = "."
#         while last_char == ".":
#             last_char = blocks_copy.pop(-1)
#         ordered_blocks.append(last_char)
#     block_index +=  1

# # after we've ordered the files, we calc the total
# total = 0
# for index, num in enumerate(ordered_blocks):
#     total += index * int(num)
# print(total)

# Part 2 is very different
blocks = []
file_num = 0
# this creates a list of files (dicts with file numbers as keys and the the number of times that files exists as the key), and empty space (the number of empty spaces in a row)
for index, num in enumerate(disk):
    # if it is a file
    if index % 2 == 0:
        blocks.append({file_num: int(num)})
        file_num += 1
    # if it is free space
    else:
        blocks.append(int(num))

# go through the list from back to front to find every group of files (dicts)
for file_index, file in enumerate(blocks[::-1]):
    if type(file) == dict:
        file_size = list(file.values())[0]
        # go through the empty spaces that come before the current file group and see if there is a space the group can be moved to
        matching_index = None
        for i, v in enumerate(blocks[:blocks.index(file)]):
            if type(v) == int:
                if v >= file_size:
                    matching_index = i
                    matching_number = blocks[matching_index]
                    break
        # if so
        if matching_index:
            # the current location of the file group becomes the number of files that were in it
            blocks[blocks.index(file)] = file_size
            # the location of the empty spaces becomes the file group
            blocks[matching_index] = file
            # any space left over from the empty space = file group size becomes more empty space (number)
            if matching_number - file_size > 0:
                blocks.insert(matching_index+1, matching_number - file_size)

# sum it up at the end
total = 0
index_counter = 0
for item in blocks:
    if type(item) == dict:
        for _ in range(list(item.values())[0]):
            total += int(list(item.keys())[0]) * index_counter
            index_counter += 1
    else:
        index_counter += item
print(total)