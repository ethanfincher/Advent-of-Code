import re
instructions = open("2015/7/input.txt").read().strip().split("\n")


def connect_signals(instructions):
    connected_signals = {}

    def find_num(value: str):
        return (int(value) if value.isdigit() else connected_signals[value])
    
    while instructions:
        not_enough_info = []
        for instruction in instructions:
            # if a -> b
            if match := re.search(r'^([a-z0-9]+) -> ([a-z]+)$', instruction):
                # if raw number
                if match.group(1).isdigit() or match.group(1) in connected_signals: 
                    connected_signals[match.group(2)] = find_num(match.group(1))
                else: not_enough_info.append(instruction)

            # if a AND|OR|LSHIFT|RSHIFT b -> c
            elif match := re.search(r'^([a-z0-9]+) (AND|OR|LSHIFT|RSHIFT) ([a-z0-9]+) -> ([a-z]+)$', instruction):
                value_1 = match.group(1)
                value_2 = match.group(3)
                connection = match.group(4)
                operator = match.group(2)
                if all(value in connected_signals or value.isdigit() for value in [value_1, value_2]):
                    if operator == "AND":
                        connected_signals[connection] = find_num(value_1) & find_num(value_2)
                    elif operator == "OR":
                        connected_signals[connection] = find_num(value_1) | find_num(value_2)
                    elif operator == "LSHIFT":
                        connected_signals[connection] = find_num(value_1) << find_num(value_2)
                    elif operator == "RSHIFT":
                        connected_signals[connection] = find_num(value_1) >> find_num(value_2)
                else: not_enough_info.append(instruction)

            # if NOT a -> b
            elif match := re.search(r'^NOT ([a-z0-9]+) -> ([a-z]+)$', instruction):
                if match.group(1) in connected_signals or match.group(1).isdigit():
                    connected_signals[match.group(2)] = (~find_num(match.group(1))) & 0xFFFF
                else: not_enough_info.append(instruction)
        instructions = not_enough_info
    return connected_signals

# Part 1
new_b = connect_signals(instructions)["a"]
print(new_b)
# Part 2
old_b_pattern = r'\d+ -> b'
instructions = [re.sub(old_b_pattern, f'{new_b} -> b', item) if re.match(old_b_pattern, item) else item for item in instructions]
print(connect_signals(instructions)["a"])