import numpy as np
lines = open("2024/4/input.txt").read().strip().split("\n")
crossword = np.array([list(line) for line in lines])
crossword_shape = crossword.shape

searchword = "XMAS"
mas_1_delta = [
    (-1, -1),  # Top-left
    ( 1,  1),  # Bottom-right
]
mas_2_delta = [
    (-1,  1),  # Top-right
    ( 1, -1),  # Bottom-left
]

total_xmas = 0

def check_for_next_letter(index):
    if all(0 <= index[0] + d[0] < crossword_shape[0] and 0 <= index[1] + d[1] < crossword_shape[1] for d in mas_1_delta+mas_2_delta):
        # this is a gross way of getting diagonal letters and checking if they're either SM or MS
        if all(crossword[index[0] + mas_delta[0][0], index[1] + mas_delta[0][1]] + crossword[index[0] + mas_delta[1][0], index[1] + mas_delta[1][1]] in ["SM", "MS"] for mas_delta in [mas_1_delta, mas_2_delta]):
            return 1
    return 0

for char_index, char in np.ndenumerate(crossword):
        if char == "A":
            total_xmas += check_for_next_letter(char_index)

print(total_xmas)