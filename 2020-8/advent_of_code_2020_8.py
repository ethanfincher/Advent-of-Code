import re
with open("2020-8\input.txt", "r") as tfile:
    game_instructions = [{
        "command": re.search(r'^(\w{3})', instruction).group(1), 
        "num":int(re.search(r'((?:\+|\-)\d*$)', instruction).group(1))} 
    for instruction in tfile.read().strip().split("\n")]

def try_instructions(instructions):
    indexes_visited = []
    accumulator = 0
    current_index = 0
    while current_index not in indexes_visited:
        try:
            instruction = instructions[current_index]
        except:
            return f"success! accumulator total = {accumulator}"
        command = instruction["command"]
        num = instruction["num"]
        indexes_visited.append(current_index)
        if command == "jmp":
            current_index += num
            continue
        elif command == "nop":
            current_index += 1
            continue
        elif command == "acc":
            accumulator += num
            current_index += 1
            continue
    return f"infinite loop detected, accumulator total = {accumulator}"
# Part 1
# print(try_instructions(game_instructions))

# Part 2
for index, instruction in enumerate(game_instructions):
    if instruction["command"].count("nop"):
        instruction["command"] = instruction["command"].replace("nop", "jmp")
        current_result = try_instructions(game_instructions)
        if current_result.count("success"):
            print(current_result)
            exit()
        instruction["command"] = instruction["command"].replace("jmp", "nop")
    elif instruction["command"].count("jmp"):
        instruction["command"] = instruction["command"].replace("jmp", "nop")
        current_result = try_instructions(game_instructions)
        if current_result.count("success"):
            print(current_result)
            exit()
        instruction["command"] = instruction["command"].replace("nop", "jmp")