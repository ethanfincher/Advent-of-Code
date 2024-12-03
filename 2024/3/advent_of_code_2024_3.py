import re
lines = open("2024/3/input.txt").read().strip().split("\n")

# sections takes each line and splits it by "do()"s and "don't()"s
# this creates a list that looks like ["do()", "unasjdnfyhbnasdoufyb", "don't()", "uiadjfiunadunbf", "don't()", ect]
sections = []
for line in lines:
    sections.extend(re.split(r"(do\(\)|don't\(\))", line))

    

total = 0
do = True

for subsection in sections:
    # if the current subsection is a do or dont, set do accordingly
    if subsection == "don't()":
        do = False
    elif subsection == "do()":
        do = True
    else:
        # if its  a chunch of text, do it if do is True, otherwise go to next subsection
        if do:
            # this regex pulls out all of the mul(num,num)
            all_muls = re.findall(r"mul\(\d+,\d+\)", subsection)
            # for each one of those, get the two numbers out of it with more regex, multiply and add to total
            for mul in all_muls:
                nums = re.findall(r"\d+", mul)
                total += int(nums[0]) * int(nums[1])

print(total)