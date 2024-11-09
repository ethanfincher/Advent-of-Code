directions = open("2015/3/input.txt").read().strip()
# all positions start at 0,0
houses = [(0,0)]
santa_x, robo_x, santa_y, robo_y = 0,0,0,0

def move_houses(x, y, direction):
    if direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    elif direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    houses.append((x,y))
    return x,y

for index, direction in enumerate(directions):
    if index % 2 == 0:
        santa_x, santa_y = move_houses(santa_x, santa_y, direction)
    else:
        robo_x, robo_y = move_houses(robo_x, robo_y, direction)
print(len(set(houses)))