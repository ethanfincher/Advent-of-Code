import statistics
lines = open("2021\\10\\input.txt").read().strip().split("\n")
# Part 1
total = 0
good_list = []
completion_totals = []
for line in lines:
    opening_chars = ""
    for char in line:
        if char in "({[<":
            opening_chars = char + opening_chars
        else:
            if char == ")" and opening_chars[0] != "(":
                total += 3
                break
            elif char == "]" and opening_chars[0] != "[":
                total += 57
                break
            elif char == "}" and opening_chars[0] != "{":
                total += 1197
                break
            elif char == ">" and opening_chars[0] != "<":
                total += 25137
                break
            else:
                opening_chars = opening_chars[1:]
    # Part 2
    else:
        completion_total = 0
        for char in opening_chars:
            completion_total *= 5
            completion_total += "([{<".index(char) + 1
        completion_totals.append(completion_total)
        
print(total)
print(statistics.median(completion_totals))