from collections import defaultdict
numbers_input = [int(num) for num in open("2024/11/input.txt").read().strip().split(" ")]

numbers = defaultdict(int)
for number in numbers_input:
    numbers[number] += 1

def blink(old_numbers: dict):
    new_numbers = defaultdict(int)
    for number, occurances in old_numbers.items():
        if number == 0:
            new_numbers[1] += occurances
        elif len(str(number)) % 2 == 0:
            string_num = str(number)
            first_num = int(string_num[:len(string_num) // 2])
            second_num = int(string_num[len(string_num) // 2:])
            new_numbers[first_num] += occurances
            new_numbers[second_num] += occurances
        else:
            new_numbers[number*2024] += occurances
    return new_numbers

for _ in range(75):
    numbers = blink(numbers)

print(sum(list(numbers.values())))