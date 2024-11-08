floor_code = open("2015/1/input.txt").read()
# Part 1
print(floor_code.count("(") - floor_code.count(")"))
# Part 2
for index, char in enumerate(floor_code):
    if floor_code[:index+1].count(")") > floor_code[:index+1].count("("):
        print(index + 1)
        break