import re
import math
input_sections = open("2024/17/input.txt").read().strip().split("\n\n")

register_lines = input_sections[0].split("\n")
a  = int(register_lines[0].split(": ")[1])
b  = int(register_lines[1].split(": ")[1])
c  = int(register_lines[2].split(": ")[1])
program = [int(num) for num in re.findall(r"\d", input_sections[1])]


def find_output(a,b,c):

    def combo_operand(num):
        if num <= 3:
            return num
        elif num == 4:
            return a
        elif num == 5:
            return b
        elif num == 6:
            return c
        
    current_index = 0
    output = []
    while current_index < len(program):
        match program[current_index]:
            case 0:
                a = int(a // (math.pow(2, combo_operand(program[current_index+1]))))
            case 1:
                b = b ^ program[current_index+1]
            case 2:
                b = combo_operand(program[current_index+1]) % 8
            case 3:
                if a != 0:
                    current_index = program[current_index+1]
                    current_index -= 2
            case 4:
                b = b ^ c
            case 5:
                output.append(combo_operand(program[current_index+1]) % 8)
            case 6:
                b = int(a // (math.pow(2, combo_operand(program[current_index+1]))))
            case 7:
                c = int(a // (math.pow(2, combo_operand(program[current_index+1]))))
        current_index += 2

    return output

a = 180000000000000
while find_output(a,b,c) != program:
    print(".".join([str(item) for item in find_output(a,b,c)]))
    a += 1

print(a)