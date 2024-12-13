import re
raw_machines = open("2024/13/input.txt").read().strip().split("\n\n")

machines = []
for raw_machine in raw_machines:
    single_line = "".join([line for line in raw_machine.split("\n")])
    machine_numbers = [int(num) for num in re.findall(r"\d+", single_line)]
    new_machine = {}
    new_machine["a"] = {"x": machine_numbers[0], "y": machine_numbers[1]}
    new_machine["b"] = {"x": machine_numbers[2], "y": machine_numbers[3]}
    new_machine["prize"] = {"x": machine_numbers[4] + 10000000000000, "y": machine_numbers[5] + 10000000000000}
    machines.append(new_machine)

# Part 1
# total_tokens = 0
# for machine in machines:
#     print(machine)
#     possible_pushes = []
#     a_presses = 0
#     while a_presses * machine["a"]["x"] <= machine["prize"]["x"]:
#         if (machine["prize"]["x"] - (a_presses * machine["a"]["x"])) % machine["b"]["x"] == 0:
#             b_presses = (machine["prize"]["x"] - (a_presses * machine["a"]["x"])) // machine["b"]["x"]
#             if machine["a"]["y"] * a_presses + machine["b"]["y"] *  b_presses == machine["prize"]["y"]:
#                 possible_pushes.append(a_presses * 3 + b_presses)
#         a_presses += 1
#     if possible_pushes: 
#         print(possible_pushes)
#         total_tokens += min(possible_pushes)

# print(total_tokens)

# Part 2
for machine in machines:
    max_b_x = machine["prize"]["x"] // machine["b"]["x"]
    min_a_x = None
    b_x_delta = None
    a_x_delta = None
    for count in range(max_b_x, -1, -1):  # Start from max_count and work down
        remainder = machine["prize"]["x"] - (count * machine["b"]["x"])
        if remainder % machine["a"]["x"] == 0:
            if not min_a_x:
                max_b_x = count
                min_a_x = remainder // machine["a"]["x"]
            else:
                b_x_delta = count - max_b_x
                a_x_delta = (remainder // machine["a"]["x"]) - min_a_x
                break
    
    max_b_y = machine["prize"]["y"] // machine["b"]["y"]
    min_a_y = None
    b_y_delta = None
    a_y_delta = None
    for count in range(max_b_y, -1, -1):  # Start from may_count and work down
        remainder = machine["prize"]["y"] - (count * machine["b"]["y"])
        if remainder % machine["a"]["y"] == 0:
            if not min_a_y:
                max_b_y = count
                min_a_y = remainder // machine["a"]["y"]
            else:
                b_y_delta = count - max_b_y
                a_y_delta = (remainder // machine["a"]["y"]) - min_a_y
                break

    possible_x = []
    while max_b_x > 0:
        possible_x.append((max_b_x, min_a_x))
        max_b_x = max_b_x + b_x_delta
        min_a_x = min_a_x + a_x_delta

    possible_y = []
    while max_b_y > 0:
        possible_y.append((max_b_y, min_a_y))
        max_b_y = max_b_y + b_y_delta
        min_a_y = min_a_y + a_y_delta

    print([x for x in possible_x if x in possible_y])
