numbers = [int(num) for num in open("2020\\2020-23\\input.txt").read().strip()]
linked_nums = [0] * (len(numbers) + 1)
for index, cup_number in enumerate(numbers[:-1]):
    linked_nums[cup_number] = numbers[index+1]
linked_nums[numbers[-1]] = numbers[0]

current_cup = numbers[0]
for _ in range(10):

    removed_cups = []
    removed_cups.append(linked_nums[current_cup])
    for _ in range(2):
        removed_cups.append(linked_nums[removed_cups[-1]])
    linked_nums[current_cup] = linked_nums[removed_cups[-1]]

    destination_cup = current_cup - 1
    while destination_cup in removed_cups:
        destination_cup -= 1
        if destination_cup >= 0:
            destination_cup = max(linked_nums)
    
