import re
command_lines = open("2021/22/input.txt").read().strip().split("\n")
lights_on = set()
for line in command_lines: 
    line_re = re.search(r"^(\w+) x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)$", line)
    x_range = [num for num in range(max(int(line_re.group(2)), -50), min(int(line_re.group(3)), 50) + 1)]
    y_range = [num for num in range(max(int(line_re.group(4)), -50), min(int(line_re.group(5)), 50) + 1)]
    z_range = [num for num in range(max(int(line_re.group(6)), -50), min(int(line_re.group(7)), 50) + 1)]
    for x in x_range:
        for y in y_range:
            for z in z_range:
                if line_re.group(1) == "on":
                    lights_on.add((x,y,z))
                else:
                    lights_on.discard((x,y,z))

print(len(lights_on))