TOTAL_LITERS = 150
bottle_sizes = [int(num) for num in open("2015/17/input.txt").read().strip().split("\n")]
bottle_sizes.sort(reverse=True)

all_combos = []
def find_all_combos(current_combo, current_index):
    # if the current sum is equal to total liters, add it to the list and stop adding bottles
    if sum(current_combo) == TOTAL_LITERS:
        all_combos.append(current_combo)
    # otherwise, if the current sum is still less then the total liters and the current index is still in bounds
    elif sum(current_combo) < TOTAL_LITERS and current_index < len(bottle_sizes):
        # add one combo that adds the current index, and one that does not
        find_all_combos((current_combo + [bottle_sizes[current_index]]), current_index+1) 
        find_all_combos(current_combo, current_index+1)

find_all_combos([], 0)

min_containers = min([len(combo) for combo in all_combos])
print(len([combo for combo in all_combos if len(combo) == min_containers]))