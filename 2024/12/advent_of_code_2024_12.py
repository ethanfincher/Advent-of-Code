# No comments tonight, this solution is horid and its 2 AM and 56 degrees right now
import numpy as np
garden = np.array([list(line) for line in open("2024/12/input.txt").read().strip().split("\n")])
garden_shape = garden.shape

all_indexes = list(np.ndindex(garden_shape))

neighbor_deltas = [(-1,0),(1,0),(0,-1),(0,1)]

# Part 1
# def find_region(current_index):
#         all_indexes.remove(current_index)
#         perimeter = 0
#         area = 1
#         current_flower = garden[current_index]
#         for d in neighbor_deltas:
#             r,c = current_index[0] + d[0], current_index[1] + d[1]
#             if 0 <= r < garden_shape[0] and 0 <= c < garden_shape[1] and garden[r,c] == current_flower:
#                 if (r,c) in all_indexes:
#                     new_flowers = find_region((r,c))
#                     perimeter += new_flowers[0]
#                     area += new_flowers[1]
#             else:
#                 perimeter += 1
#         return (perimeter, area)

# Part 2
def find_region(current_index):
        all_indexes.remove(current_index)
        flower_indexes = [current_index]
        current_flower = garden[current_index]
        for d in neighbor_deltas:
            r,c = current_index[0] + d[0], current_index[1] + d[1]
            if 0 <= r < garden_shape[0] and 0 <= c < garden_shape[1] and garden[r,c] == current_flower:
                if (r,c) in all_indexes:
                    new_flowers = find_region((r,c))
                    flower_indexes.extend(new_flowers)
        return (flower_indexes)

flower_bed_values = []
while all_indexes:
    new_bed = find_region(all_indexes[0])
    sides_dict = {"t": [],"r": [],"b": [],"l": []}
    sides = 0

    for index in new_bed:
        # top
        if (index[0] - 1, index[1]) not in new_bed:
            sides_dict["t"].append((index[0], index[1]))
        # bottom
        if (index[0] + 1, index[1]) not in new_bed:
            sides_dict["b"].append((index[0], index[1]))
        # left
        if (index[0], index[1] - 1) not in new_bed:
            sides_dict["l"].append((index[0], index[1]))
        # right
        if (index[0], index[1] + 1) not in new_bed:
            sides_dict["r"].append((index[0], index[1]))

    sides_dict["t"] = sorted(sides_dict["t"], key=lambda x: (x[0], x[1]))
    sides_dict["b"] = sorted(sides_dict["b"], key=lambda x: (x[0], x[1]))
    sides_dict["l"] = sorted(sides_dict["l"], key=lambda x: (x[1], x[0]))
    sides_dict["r"] = sorted(sides_dict["r"], key=lambda x: (x[1], x[0]))

    for index, side in enumerate(sides_dict["t"]):
        if index == len(sides_dict["t"]) - 1:
            sides += 1
        else:
            if side[0] == sides_dict["t"][index+1][0] and side[1]+1 == sides_dict["t"][index+1][1]:
                continue
            else:
                sides += 1

    for index, side in enumerate(sides_dict["b"]):
        if index == len(sides_dict["b"]) - 1:
            sides += 1
        else:
            if side[0] == sides_dict["b"][index+1][0] and side[1] + 1 == sides_dict["b"][index+1][1]:
                continue
            else:
                sides += 1

    for index, side in enumerate(sides_dict["r"]):
        if index == len(sides_dict["r"]) - 1:
            sides += 1
        else:
            if side[1] == sides_dict["r"][index+1][1] and side[0] + 1 == sides_dict["r"][index+1][0]:
                continue
            else:
                sides += 1

    for index, side in enumerate(sides_dict["l"]):
        if index == len(sides_dict["l"]) - 1:
            sides += 1
        else:
            if side[1] == sides_dict["l"][index+1][1] and side[0] + 1 == sides_dict["l"][index+1][0]:
                continue
            else:
                sides += 1

    flower_bed_values.append(sides * len(new_bed))

print(sum(flower_bed_values))