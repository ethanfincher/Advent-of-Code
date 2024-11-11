import re
import math
lines = open("2021/18/input.txt").read().strip().split("\n")
def reduce_numbers(number_1, number_2):
    number_to_calc = f"[{number_1},{number_2}]"
    # check for explosions
    while True:
        levels_deep = 0
        # check for explosions
        for index, char in enumerate(number_to_calc):
            if char == ",":
                continue
            elif char == "[": 
                levels_deep += 1
            elif char == "]":
                levels_deep -= 1
            # Past here, char must be a number
            elif levels_deep >= 5:
                current_pair = re.search(r'(\d+),(\d+)', number_to_calc[index:])
                # first half
                first_part = number_to_calc[:index-1]
                first_number = re.search(r'(\d+)(?=\D*$)', first_part)
                if first_number:
                    first_part = re.sub(r'(\d+)(?=\D*$)', str(int(first_number.group()) + int(current_pair.group(1))), first_part)
                # second half
                second_part = number_to_calc[index+len(current_pair.group())+1:]
                second_number = re.search(r'\d+', second_part)
                if second_number:
                    second_part = re.sub(r'\d+', str(int(second_number.group(0)) + int(current_pair.group(2))), second_part, count=1)
                # combine
                number_to_calc = first_part + "0" + second_part
                break
        else:
            # check for splits
            for index, char in enumerate(number_to_calc):
                if char in "[],":
                    continue
                elif int(re.search(r'^\d+', number_to_calc[index:]).group()) >= 10:
                    big_num = re.search(r'^\d+', number_to_calc[index:]).group()
                    number_to_calc = number_to_calc.replace(big_num, f"[{math.floor(int(big_num)/2)},{math.ceil(int(big_num)/2)}]", 1)
                    break
            else:
                break
    return number_to_calc
    
def sum_number(current_number):
    while not re.search(r'^\d+$', current_number):
        current_pair = re.search(r'\[(\d+),(\d+)\]', current_number)
        current_number = current_number.replace(current_pair.group(), str((3 *int(current_pair.group(1))) + (2 * int(current_pair.group(2)))))
    return int(current_number)

# Part 1
final_number = lines[0]
for line in lines[1:]:
    final_number = reduce_numbers(final_number, line)
print(sum_number(final_number))

# Part 2
largest_sum = 0
for index, first_line in enumerate(lines[:-1]):
    for second_line in lines[index+1:]:
        forward_sum = sum_number(reduce_numbers(first_line, second_line))
        backward_sum = sum_number(reduce_numbers(second_line, first_line))
        if forward_sum > largest_sum: largest_sum = forward_sum
        if backward_sum > largest_sum: largest_sum = backward_sum
print(largest_sum)