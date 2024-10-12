import numpy as np
raw_input = binary_numbers = open("2021\\4\\input.txt", "r").read().strip().split("\n\n")
drawn_numbers = raw_input[0].split(",")
boards = [number_group.split("\n") for number_group in raw_input[1:]]
print(boards)

for b_index, board in enumerate(boards):
    for l_index, line in enumerate(board):
        board[b_index][l_index] = line.strip().replace("  ", " ").split(" ")
        print(board)