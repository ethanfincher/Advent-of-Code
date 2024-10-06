with open("2020-15\\input.txt", "r") as tfile:
    numbers = [int(num) for num in tfile.read().split(",")]

# Part 1
# for i in range(len(numbers)-1, 2019):
#     if not numbers.count(numbers[i]) > 1:
#         numbers.append(0)
#     else:
#         last_occurance = len(numbers) - 2 - numbers[:-1][::-1].index(numbers[i])
#         numbers.append(i - last_occurance)
# print(f"final number: {numbers[-1]}")

# Part 2, part 1 is too fast and I can't think of an equation to calculate this, so gotta make it faster
last_seen = {number: index for index, number in enumerate(numbers[:-1])}
# print(f"Turn 1: new number is {numbers[0]}")
# print()
# print(f"Turn 2: new number is {numbers[1]}")
# print()
# print(f"Turn 3: new number is {numbers[2]}")
# print()
current_num = numbers[-1]
for i in range(len(numbers)-1, 30000000 - 1):
    # print(f"Turn {i + 2}: ")
    # print(f"last seen list: {last_seen}")
    # print(f"looking at index {i}")
    # print(f"current number is {current_num}")
    if current_num not in last_seen:
        # print("current num not found")
        last_seen[current_num] = i
        current_num = 0
    else:
        # print(f"found that number at index {last_seen[current_num]}")
        new_num = i - last_seen[current_num]
        last_seen[current_num] = i
        current_num = new_num
    # print(f"new number is {current_num}")
    # print()

print(current_num)