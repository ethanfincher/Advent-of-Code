import re
lines = open("2015/16/input.txt").read().strip().split("\n")

matching_sue = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}
sues = {}
for line in lines:
    line_re = re.search(r"^(Sue \d+): (.*)$", line)
    sues[line_re.group(1)] = {item.split(": ")[0]: int(item.split(": ")[1]) for item in line_re.group(2).split(", ")}

for sue, details in sues.items():
    # if all(key in matching_sue and matching_sue[key] == value for key, value in details.items()):
    for detail_name, detail_value in details.items():
        if detail_name in ["cats", "trees"]: 
            if not detail_value > matching_sue[detail_name]: break
        elif detail_name in ["pomeranians", "goldfish"]:
            if not detail_value < matching_sue[detail_name]: break
        else:
            if not detail_value == matching_sue[detail_name]: break
    else:
        print(details)
        print(sue)
        break