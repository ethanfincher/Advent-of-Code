import re
input = open("2024/7/input.txt").read().strip().split("\n")
equations = [[int(num) for num in re.findall(r"\d+", line)] for line in input]

def combine_string(target_number, current_number, remaining_numbers):
    add_total = current_number + remaining_numbers[0]
    mult_total = current_number * remaining_numbers[0]
    combo_total = int(str(current_number)+str(remaining_numbers[0]))
    # if we added the last number, check to see if it matches the total. if so, return 1. else, return 0
    if len(remaining_numbers) == 1:
        if any(total == target_number for total in [add_total, mult_total, combo_total]):
            return 1
        else:
            return 0
    # if there are more numbers to calc, check if any of their results = 1, otherwise return 0
    else:
        if any (combine_string(target_number, total, remaining_numbers[1:]) == 1 for total in [add_total, mult_total, combo_total]): 
            return 1
        else:
            return 0

good_equation_total = 0
for equation in equations:
    target_num = int(equation[0])
    if combine_string(target_num, equation[1], equation[2:]) == 1:
        good_equation_total += int(target_num)

print(good_equation_total)