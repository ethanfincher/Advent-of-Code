import re
lines = open("2021\\12\\input.txt").read().strip().split("\n")
caves = {}
for line in lines: 
    # for each line, append the second part of the line to the key matching the first part, and vise versa
    line_regex = re.search(r'(\w*)-(\w*)', line)
    if line_regex.group(1) not in caves:
        caves[line_regex.group(1)] = [line_regex.group(2)]
    else:
        caves[line_regex.group(1)].append(line_regex.group(2))

    if line_regex.group(2) not in caves:
        caves[line_regex.group(2)] = [line_regex.group(1)]
    else:
        caves[line_regex.group(2)].append(line_regex.group(1))

paths = []
def find_path(current_route, small_cave_visited):
    # for each cave that connects to the current cave
    for cave in caves[current_route[-1]]:
        # always end if cave is "end"
        if cave == "end":
            paths.append(current_route + ["end"])
        # Part 2 here, if we havent visited a cave twice before, the visit it again. Also can't visit "start" twice
        elif cave.islower() and cave in current_route and not small_cave_visited and cave != "start":
            find_path(current_route + [cave], True)
        # if the cave is small and hasn't been visited yet, then visit it
        elif cave.islower() and cave not in current_route:
            find_path(current_route + [cave], small_cave_visited)
            # if the cave is big, visit it
        elif not cave.islower():
            find_path(current_route + [cave], small_cave_visited)

# start as "start"
find_path(["start"], False)
print(len(paths))