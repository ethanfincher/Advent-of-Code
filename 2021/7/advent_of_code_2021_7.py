import statistics
crab_positions = [int(num) for num in open("2021\\7\\input.txt", "r").read().strip().split(",")]
# Part 1
median = int(statistics.median(crab_positions))
total = 0
for number in crab_positions:
    total += abs(number - median)
print(total)
# Part 2, just brute forced it, should used the mean and just checked the number given the floor and ceiling of the mean
total_2 = 1000000000000000000000000000000000000
for i in range(min(crab_positions), max(crab_positions)):
    current_total = 0
    for number in crab_positions:
        current_total += sum([i+1 for i in range(abs(number-i))])
    if current_total < total_2: total_2 = current_total; the_number = i
print(total_2)
