import re
with open("2020-14\input.txt", "r") as tfile:
    commands = tfile.read().strip().split("\n")

# Part 1
mask = ""
# def apply_mask(value: int):
#     # binary string of value
#     b_value = bin(value).replace("0b", "").zfill(36)
#     # find position and value of 2 bits in the mask
#     for index, bit in enumerate(mask):
#         # swap those bits in the value string
#         if bit in ("0", "1"): b_value = b_value[:index] + bit + b_value[index+1:]
#     # return the int representation of the new value string
#     return int(b_value, 2)

# memory_list = {}
# for command in commands:
#     if command.count("mask"):
#         mask = re.search(r"= ([X\d]{36})", command).group(1)
#     else:
#         # pulls out the memory number and the new value
#         mem_regex = re.search(r"mem\[(\d*)\] = (\d*)", command)
#         memory_list[mem_regex.group(1)] = apply_mask(int(mem_regex.group(2)))
# print(sum(list(memory_list.values())))
# Part 2
def apply_mask(mem_loc: int, value: int):
    locations = {}
    # binary string of mem_loc
    b_value = bin(mem_loc).replace("0b", "").zfill(36)
    for index, bit in enumerate(mask):
        # swap 1 and "X" from mask into b_value
        if bit in ("X", "1"): b_value = b_value[:index] + bit + b_value[index+1:]
    # function that returns list of all possible int values from b_value with replaced x
    def replace_x(b_string: str):
        x_index = b_string.find("X")
        # if there is an x, then call replace x with a replaced value of 1 and 0 on the current x
        if b_string.find("X") != -1:
            replace_x(b_string[:x_index] + "0" + b_string[x_index+1:])
            replace_x(b_string[:x_index] + "1" + b_string[x_index+1:])
        # if not, then add the {b_string: value} to the locations list
        else: 
            locations[str(int(b_string, 2))] = value
    replace_x(b_value)
    return locations

memory_dict = {}
for command in commands:
    if command.count("mask"):
        mask = re.search(r"= ([X\d]{36})", command).group(1)
    else:
        # pulls out the memory number and the new value
        mem_regex = re.search(r"mem\[(\d*)\] = (\d*)", command)
        # update the memory dict with the new dict from the latest command (used in apply mask)
        memory_dict = memory_dict | apply_mask(int(mem_regex.group(1)), int(mem_regex.group(2)))
print(sum(list(memory_dict.values())))