import re
import sympy as sp

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
token_total = 0
for machine in machines:
    # need to solve for system
    # ax * a + bx * b = px
    # ay * a + by * b = py
    # first time using sympy, chat GPT helped me arrive at the solution
    a, b = sp.symbols('a b')
    eq1 = sp.Eq(machine["a"]["x"] * a + machine["b"]["x"] * b, machine["prize"]["x"])
    eq2 = sp.Eq(machine["a"]["y"] * a + machine["b"]["y"] * b, machine["prize"]["y"])

    # Solve the system of equations
    solution = sp.solve([eq1, eq2], (a, b))
    if solution[a].is_integer and solution[b].is_integer:
        token_total += solution[a]*3 + solution[b]

print(token_total)