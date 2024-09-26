with open("2020-12\input.txt", "r") as tfile:
    moves = [move for move in tfile.read().strip().split("\n")]
# Part 1
# current_direction = "E"
# directions = ["E", "S", "W", "N"]
# for move in moves:
#     letter = move[0]
#     num = int(move[1:])
#     if letter == "F": letter = current_direction
#     match letter:
#         case "N":
#             y_position += num
#         case "S":
#             y_position -= num
#         case "E":
#             x_position += num
#         case "W":
#             x_position -= num
#         case "R":
#             current_direction = directions[int((directions.index(current_direction) + num/90)%4)]
#         case "L":
#             current_direction = directions[int((directions.index(current_direction) - num/90)%4)]
# print(abs(x_position) + abs(y_position))
ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1

def sector_finder(delta):
    # Find current sector
    current_sector = 0
    if waypoint_y > 0:
        if waypoint_x > 0: current_sector = 0
        else: current_sector = 3
    else: 
        if waypoint_x > 0: current_sector = 1
        else : current_sector = 2
    current_sector = (current_sector + delta)%4
    x = waypoint_x if delta%2 == 0 else waypoint_y
    y = waypoint_y if delta%2 == 0 else waypoint_x
    # Find new sector
    match current_sector:
        case 0:
            return(abs(x), abs(y))
        case 1:
            return(abs(x), -abs(y))
        case 2:
            return(-abs(x), -abs(y))
        case 3:
            return(-abs(x), abs(y))

for move in moves:
    letter = move[0]
    num = int(move[1:])
    match letter:
        case "N":
            waypoint_y += num
        case "S":
            waypoint_y -= num
        case "E":
            waypoint_x += num
        case "W":
            waypoint_x -= num
        case "F":
            ship_x += (waypoint_x*num)
            ship_y += (waypoint_y*num)
        case "R":
            waypoint_x, waypoint_y = sector_finder(int(num/90))
        case "L":
            waypoint_x, waypoint_y = sector_finder(int(-num/90))
print(abs(ship_x) + abs(ship_y))