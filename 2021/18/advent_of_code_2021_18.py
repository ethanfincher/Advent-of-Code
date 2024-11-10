import re
import math
lines = open("2021/18/input.txt").read().strip().split("\n")
current_number = lines[0]
for line in lines[1:]:
    number_to_calc = f"[{current_number},{line}]"
    # check for explosions
    while True:
        levels_deep = 0
        for index, char in enumerate(number_to_calc):
            if char == ",":
                continue
            elif char == "[": 
                levels_deep += 1
            elif char == "]":
                levels_deep -= 1
            # Past here, char must be a number
            # check for explosions
            elif levels_deep == 5:
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
                print(f"explode: {number_to_calc}")
                break

            # check for splits
            elif int(re.search(r'^\d+', number_to_calc[index:]).group()) >= 10:
                big_num = re.search(r'^\d+', number_to_calc[index:]).group()
                number_to_calc = number_to_calc.replace(big_num, f"[{math.floor(int(big_num)/2)},{math.ceil(int(big_num)/2)}]", 1)
                print(f"split: {number_to_calc}")
                break
        else:
            break
    print(number_to_calc)
    current_number = number_to_calc
    break
    
# print(number_to_calc)