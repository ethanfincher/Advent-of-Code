import numpy as np
lines = open("2024/4/input.txt").read().strip().split("\n")
crossword = np.array([list(line) for line in lines])
crossword_shape = crossword.shape

searchword = "XMAS"
neighbor_deltas = [
        (-1, -1),  # Top-left
        (-1,  0),  # Top
        (-1,  1),  # Top-right
        ( 0, -1),  # Left
        ( 0,  1),  # Right
        ( 1, -1),  # Bottom-left
        ( 1,  0),  # Bottom
        ( 1,  1),  # Bottom-right
    ]

total_xmas = 0

def check_for_next_letter(index, letter_index, direction_delta):
        r, c = index[0] - direction_delta[0], index[1] - direction_delta[1]
        # check that index to check is in bounds
        if 0 <= r < crossword_shape[0] and 0 <= c < crossword_shape[1]:
            # if correct letter is found
            if crossword[r,c] == searchword[letter_index]:
                # if its the last letter in the search phrase, add to total xmas
                if letter_index == len(searchword) - 1:
                    return 1
                else:
                    # if its not the last, check for the next letter
                    return check_for_next_letter((r,c), letter_index+1, direction_delta)
        return 0

for char_index, char in np.ndenumerate(crossword):
    if char == searchword[0]:
        for d in neighbor_deltas:
            total_xmas += check_for_next_letter(char_index, 1, d)
    
print(total_xmas)