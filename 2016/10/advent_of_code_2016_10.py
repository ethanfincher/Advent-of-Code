import re
instruction_list = open("2016/10/input.txt").read().strip().split("\n")

bot_values = {}
bot_instructions = {}
outputs = {}

# There are 2 kinds of lines, lines that provide values, and lines that explain how a bot will transfer chips once it as 2
for line in instruction_list:
    # This is for transfer instructions
    if re.search(r'^bot.*', line):
        current_bot, low_type, low_value, high_type, high_value = re.search(r"bot (\d+) .* (bot|output) (\d+) .* (bot|output) (\d+)", line).groups()
        bot_instructions[int(current_bot)] = [[low_type, int(low_value)], [high_type, int(high_value)]]
    # This is for value assignment 
    elif re.search(r'^value.*', line):
        value, bot_number = [int(val) for val in re.findall(r'(\d+)', line)]
        # Add to list if it exists, otherwise create a new one
        bot_values[bot_number] = bot_values[bot_number] + [value] if bot_values.get(bot_number) else [value]
 
# After initial values and chip swapping values have been assigned, find the first bot with 2 chips
double_chip_bot = next(key for key, value in bot_values.items() if len(value) > 1)
# While there is a bot with 2 chips, run the loop (new bots get assigned at the end of the loop)
while double_chip_bot != None:
    # print(f"start: {bot_values}")
    # Find the values and swapping instructions for the current bot number
    values = bot_values[double_chip_bot]
    current_instructions = bot_instructions[double_chip_bot]
    # Part 1
    # if 61 in values and 17 in values:
    #     print(double_chip_bot)
    #     exit()
    for index, instruction in enumerate(current_instructions):
        # print(f"current instruction: {instruction}")
        # First instruction always assigns the min, second assigns max
        current_value = min(values) if index == 0 else max(values)
        # Outputs always only have 1 value
        if instruction[0] == "output":
            outputs[instruction[1]] = current_value
        else: 
            # Add to list if it exists, otherwise create a new one
            bot_values[instruction[1]] = bot_values[instruction[1]] + [current_value] if bot_values.get(instruction[1]) else [current_value]

    # Reset current bot since chips have been handed off
    bot_values[double_chip_bot] = []
    # print(f"end: {bot_values}")
    # Set the next double chip, or set value to None if none are left
    double_chip_bot = next((key for key, value in bot_values.items() if len(value) > 1), None)
    # print(f"next double chip: {double_chip_bot}")

# Part 2
print(outputs[0] * outputs[1] * outputs[2])