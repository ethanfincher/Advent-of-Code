import numpy as np
raw_input = open("2021/20/input.txt").read().strip().split("\n\n")
enhancement_string = raw_input[0]
starting_picture = np.array([list(line) for line in raw_input[1].split("\n")])

def enhance_picture(input_array, iteration):
    # pad the current picture with either . or #
    # need to add the ternary statement at the end because the 0 index on the enhancement string makes all the dark spots light
    padded_input = np.pad(input_array, pad_width=3, mode='constant', constant_values = ('.' if iteration % 2 == 0 else "#"))
    current_image_shape = padded_input.shape
    new_image = np.full(current_image_shape, "?", dtype='<U1')
    for index, value in np.ndenumerate(padded_input):
        pixel_binary = []
        for rd, cd in [(-1,-1), (-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
            r, c = index[0] + rd, index[1] + cd
            if 0 <= r < current_image_shape[0] and 0 <= c < current_image_shape[1]:
                bit = "1" if padded_input[r,c] == "#" else "0"
                pixel_binary.append(bit)
            else:
                # same ternary statement as the padding line
                pixel_binary.append("0" if iteration % 2 == 0 else "1")

        new_image[index] = enhancement_string[int("".join(pixel_binary), 2)]
    return new_image

for iteration in range(50):
    starting_picture = enhance_picture(starting_picture, iteration)

print(np.count_nonzero(starting_picture == '#'))