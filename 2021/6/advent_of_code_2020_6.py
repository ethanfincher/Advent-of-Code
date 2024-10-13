raw_input = [int(num) for num in open("2021\\6\\input.txt", "r").read().strip().split(",")]
# Part 1
fish_counter = {
    0: raw_input.count(0),
    1: raw_input.count(1),
    2: raw_input.count(2),
    3: raw_input.count(3),
    4: raw_input.count(4),
    5: raw_input.count(5),
    6: raw_input.count(6),
    7: raw_input.count(7),
    8: raw_input.count(8),
}
for day in range(1, 257):
    new_fish_day = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
}
    for i in range(9):
        if i == 0:
            new_fish_day[6] = new_fish_day[8] = fish_counter[0]
        else:
            new_fish_day[i-1] += fish_counter[i]
    fish_counter = new_fish_day
print(sum(fish_counter.values()))
# Part 2 is change the day loop from 81 (80 days) to 257 (256 days)