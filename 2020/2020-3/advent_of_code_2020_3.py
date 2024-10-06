# Part 1
with open("2020-3\input.txt", "r") as tfile:
    raw_spaces_and_trees = tfile.read()

spaces_and_trees_list = raw_spaces_and_trees.strip().split("\n")
max_horizontal_position = len(spaces_and_trees_list[0]) - 1
def tree_counter(moves_across, moves_down):
    horizontal_position = 0
    total_trees = 0
    for row in spaces_and_trees_list[::moves_down]:
        if row[horizontal_position] == "#":
            total_trees += 1
        horizontal_position += moves_across
        if horizontal_position > max_horizontal_position:
            horizontal_position -= (max_horizontal_position + 1)
    return total_trees
print(tree_counter(3, 1))
# Part 2, changes to part 1 include turning the main loop into a function
print(tree_counter(1, 1) * tree_counter(3, 1) * tree_counter(5, 1) * tree_counter(7, 1) * tree_counter(1, 2))