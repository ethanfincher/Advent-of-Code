# Part 1
binary_numbers = open("2021\\3\\input.txt", "r").read().strip().split("\n")
gamma_rate = ""
epsilon_rate = ""
for i in range(len(binary_numbers[0])):
    counter = 0
    for number in binary_numbers:
        if number[i] == "1":
            counter += 1
        else: 
            counter -= 1
    gamma_rate = gamma_rate + ("1" if counter > 0 else "0")
    epsilon_rate = epsilon_rate + ("0" if counter > 0 else "1")

# print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2
numbers_copy = binary_numbers.copy()
for i in range(len(binary_numbers[0])):
    if len(numbers_copy) == 1: oxygen = int(numbers_copy[0], 2)
    counter = 0
    for number in numbers_copy:
        if number[i] == "1":
            counter += 1
        else: 
            counter -= 1
    numbers_copy = [numbers for numbers in numbers_copy if numbers[i] == ("1" if counter >= 0 else "0")]

numbers_copy = binary_numbers.copy()
for i in range(len(binary_numbers[0])):
    if len(numbers_copy) == 1: scrubber  = int(numbers_copy[0], 2)
    counter = 0
    for number in numbers_copy:
        if number[i] == "1":
            counter += 1
        else: 
            counter -= 1
    numbers_copy = [numbers for numbers in numbers_copy if numbers[i] == ("0" if counter >= 0 else "1")]

print(oxygen * scrubber)