# needed some help on this one
# get original numbers as a list
numbers = [int(num) for num in open("2020\\2020-23\\input.txt").read().strip()]
# create empty list 1 million (and 1) chars long
linked_nums = [0] * (1000001)
# given cup value n, linked_nums[n] will return the value of the cup next to n (indexes are cup numbers, list values are the right hand neighbors cup number)
for index, cup_number in enumerate(numbers[:-1]):
    linked_nums[cup_number] = numbers[index+1]
linked_nums[numbers[-1]] = len(numbers) + 1
# continue linking through one mil
for num in range(len(numbers) + 1, len(linked_nums) - 1):
    linked_nums[num] = num + 1
# link last item back to the front of the list (aside from 0)
linked_nums[-1] = numbers[0]

current_cup = numbers[0]
# loop ten mil times
for _ in range(10000000):
    # get values of removed cups, use those values to find their neighbors
    removed_cups = []
    removed_cups.append(linked_nums[current_cup])
    for _ in range(2):
        removed_cups.append(linked_nums[removed_cups[-1]])
    # reconnect the cap left by the removed cups
    linked_nums[current_cup] = linked_nums[removed_cups[-1]]

    # find destination cup
    destination_cup = current_cup - 1
    while destination_cup in removed_cups or destination_cup <= 0:
        destination_cup -= 1
        if destination_cup <= 0:
            destination_cup = max(linked_nums)
    
    # make new links for removed cups
    linked_nums[removed_cups[-1]] = linked_nums[destination_cup]
    linked_nums[destination_cup] = removed_cups[0]
    # re-assign current cup
    current_cup = linked_nums[current_cup]

# runs pretty quick! Had to watch some youtube on examples of solutions using linked lists, fun stuff to learn about!
print(linked_nums[1] * linked_nums[linked_nums[1]])