import math
with open("2020-13\input.txt", "r") as tfile:
    notes = tfile.read().strip().split("\n")
# Part 1
bus_numbers = [int(num) for num in notes[1].replace("x,", "").split(",")]
# 1,014,511
# earliest_timestamp = int(notes[0])
# closest_bus = {"bus_number": 0, "proximity": 10000000}
# for bus_num in bus_numbers:
#     closest_multiplier = math.ceil(earliest_timestamp/bus_num)
#     time_dif = (bus_num * closest_multiplier) - earliest_timestamp
#     if time_dif < closest_bus["proximity"]:
#         closest_bus["bus_number"] = bus_num
#         closest_bus["proximity"] = time_dif
# print(closest_bus["bus_number"] * closest_bus["proximity"])
# Part 2
def lcm(a, b):
    return a * b // math.gcd(a, b)

bus_positions = []
bus_info = notes[1].split(",")
# create tuple for each bus number (number, offset from first)
for index, number in enumerate(bus_info):
    if number != "x":
        bus_positions.append((int(number), index))

timestamp = 0
# the first increment is the fist bus number
increment = bus_positions[0][0]

for bus_number, offset in bus_positions[1:]:
    # while the current time stamp plus the current offset is not divisible by the bus number
    while (timestamp + offset) % bus_number != 0:
        # increase the timestamp by the current incrementor until the lcm (with the addition of the offset) is found
        timestamp += increment
    # Update increment to be the LCM of all bus numbers found so far
    increment = lcm(increment, bus_number)

print(timestamp)