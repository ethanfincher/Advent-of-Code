cups = [int(char) for char in open("2020\\2020-23\\input.txt").read().strip()]
current_cup = cups[0]
for i in range(10000000):
    removed_cups = []
    destination_cup = current_cup
    # find the index for the current cup
    # create sublist of 3 cups after the current cup + remove them from the list
    for j in range(3):
        removed_cups.append(cups.pop((cups.index(current_cup)+1)%len(cups)))
    # find the destination cup
    destination_cup -= 1
    while destination_cup not in cups:
        destination_cup -= 1
        if destination_cup < min(cups):
            destination_cup = max(cups)
    # place the cups back after the desitnation cup
    cups = cups[:cups.index(destination_cup)+1] + removed_cups + cups[cups.index(destination_cup)+1:]
    # find the new current cup
    current_cup = cups[(cups.index(current_cup)+1)%len(cups)]
print(cups)