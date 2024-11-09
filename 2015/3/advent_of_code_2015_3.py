directions = open("2015/3/input.txt").read().strip()
houses = [(0,0)]
x,y = 0,0
for direction in directions:
    if direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    elif direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    houses.append((x,y))
print(len(set(houses)))