depths = [int(depth) for depth in open("input.txt", "r").read().strip().split("\n")]
depths = [(depth + depths[index+1] + depths[index+2]) for index, depth in enumerate(depths[:-2])]
print(len(depths))
print(sum([1 for index, current_depth in enumerate(depths[1:]) if current_depth > depths[index]]))