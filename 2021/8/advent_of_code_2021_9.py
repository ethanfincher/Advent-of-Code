raw_input = open("2021\\8\\input.txt", "r").read().strip().split("\n")
codes = []
for line in raw_input:
    line_sections = line.split("|")
    codes.append((line_sections[0].strip().split(" "), line_sections[1].strip().split(" ")))
# One liner, inner most list replaces any char in any of the values that has a length of 2,3,4 or 7 with a 1, then outermost part merges all those lists together
second_parts = [number for num_list in [[1 for string in code[1] if len(string) in (2,4,3,7)] for code in codes] for number in num_list]
# then sum the ones (aka the whole list)
print(sum(second_parts))

# Part 2
for line in codes:
    jumbled_signals = line[0]
    fixed_signals = {}
    values = line[1]
    fixed_signals[1] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 2)))
    fixed_signals[4] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 4)))
    fixed_signals[7] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 3)))
    fixed_signals[8] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 7)))
    # fixed_signals[9] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if fixed_signals[1] in s)))
    # fixed_signals[0] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == i)))
    # fixed_signals[2] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == i)))
    # fixed_signals[3] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == i)))
    # fixed_signals[5] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == i)))
    # fixed_signals[6] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == i)))
    print(fixed_signals[1])
    print(jumbled_signals)
    print(fixed_signals)
    exit()
    