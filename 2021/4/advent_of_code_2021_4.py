import numpy as np
raw_input = open("2021\\4\\input.txt", "r").read().strip().split("\n\n")
drawn_numbers = raw_input[0].split(",")
# this creates arrays of strings for every board
boards = [number_group.split("\n") for number_group in raw_input[1:]]
# this turns that list of strings into a a 2d np array of numbers
boards = np.array([
    [line.strip().replace("  ", " ").split(" ") for line in board]
    for board in boards
])

turns_to_win = []
last_numbers = []

for b_index, board in enumerate(boards):
    for n_index, number in enumerate(drawn_numbers):
        if np.any(board == number):
            board[board == number] = "B"
            if np.any(np.all(board == board[:, [0]], axis=1)) or np.any(np.all(board == board[0, :], axis=0)):
                turns_to_win.append(n_index)
                last_numbers.append(number)
                # print(f"board {b_index+1} bingo on turn {n_index}")
                break
winning_index = turns_to_win.index(min(turns_to_win))
winning_total = 0
for element in np.nditer(boards[winning_index]):
    if element != "B":
        winning_total += int(element)
print(int(last_numbers[winning_index]) * winning_total)

# Part 2
losing_index = turns_to_win.index(max(turns_to_win))
losing_total = 0
for element in np.nditer(boards[losing_index]):
    if element != "B":
        losing_total += int(element)
print(int(last_numbers[losing_index]) * losing_total)
