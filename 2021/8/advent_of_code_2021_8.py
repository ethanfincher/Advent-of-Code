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
total = 0
for line in codes:
    jumbled_signals = line[0]
    values = line[1]
    # values are not all in the same order as their signal equivalent, this makes sure they are
    values = [''.join(sorted(value, key=lambda x: signal.index(x))) for value in values for signal in jumbled_signals if sorted(value) == sorted(signal)]
    # assign fixed signal values based upon patterns
    fixed_signals = {}
    fixed_signals[1] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 2)))
    fixed_signals[4] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 4)))
    fixed_signals[7] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 3)))
    fixed_signals[8] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 7)))
    fixed_signals[9] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if all(letter in s for letter in fixed_signals[4]) and len(s) == 6)))
    fixed_signals[3] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if all(letter in s for letter in fixed_signals[7]) and len(s) == 5)))
    fixed_signals[0] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if all(letter in s for letter in fixed_signals[7]) and len(s) == 6)))
    fixed_signals[6] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if len(s) == 6)))
    fixed_signals[2] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals if sum(1 for c in set(s) if c in fixed_signals[4]) == 2)))
    fixed_signals[5] = jumbled_signals.pop(jumbled_signals.index(next(s for s in jumbled_signals)))
    # fixed_signals = {k: fixed_signals[k] for k in sorted(fixed_signals)}
    # switch keys and values so we can use elems in the values list as keys
    fixed_signals = {v: k for k, v in fixed_signals.items()}
    # use string to line values up, then turn that into an int and add to total
    total += int(f"{fixed_signals[values[0]]}{fixed_signals[values[1]]}{fixed_signals[values[2]]}{fixed_signals[values[3]]}")
print(total)