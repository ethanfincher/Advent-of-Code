import re
# Part 1
with open("2020-19\\input.txt", "r") as tfile:
    input_sections = [section.split("\n") for section in tfile.read().strip().split("\n\n")]
raw_rules = input_sections[0]
messages = input_sections[1]
rules = {}
for rule in raw_rules:
    key = rule[:rule.index(":")]
    values = [values.strip().split() for values in rule[rule.index(":")+1:].split("|")]
    rules[key] = values

def find_possible_strings(starting_number: str, starting_strings: list):
    # print()
    # print(f'function start, starting number: {starting_number}, starting strings: {starting_strings}')
    return_strings = []
    # get rule options for current number
    rule_options = rules[starting_number]
    # print(f'options: {rule_options}')
    # if there are multiple options (|), then each of their results to the options
    for option in rule_options:
        # print(f'working on option {option}')
        strings_copy = starting_strings.copy()
        # print(f'current strings: {strings_copy}')
        # for each number in the current option
        for number in option:
            # print(f'working on option number {number}')
            # if the number translates to one of the chars, then add it to the end of the current string
            if re.search(r"[a-zA-Z]", rules[number][0][0]):
                strings_copy = [string + rules[number][0][0] for string in strings_copy]
                # print(f'hit letter {rules[number][0][0]}! string copy now looks like {strings_copy}')
            else:
                # otherwise, call possible strings on the number and append the result to starting strings
                # print(f'letter not found, going into next level')
                strings_copy = find_possible_strings(number, strings_copy)
        # print(f'adding {strings_copy} to return strings')
        return_strings += strings_copy
    # print(f'returning {return_strings}')
    return return_strings
# print(find_possible_strings("0", [""]))
# possible_strings = [string.replace('"', "") for string in find_possible_strings("0", [""])]
# print(sum([1 for match in messages if match in possible_strings]))

# Part 2, going to hardcode some of this because I've been on it for a while and 
# "Remember, you only need to handle the rules you have; building a solution that could handle any hypothetical combination of rules would be significantly more difficult"
# Now to try and explain; part 2 reaplces 8 with "42 | 42 8", and 11 with "42 31 | 42 11 31". Also important to note, that 0 starts with "8 11", so 8 will never occur in 11 and vise versa
# This also means 8 will always come first, and 8 can only ever translate to 42, or 42 and itself. 
# so rather then calculating all possible combos like before (which would be impossible), I just need to see if any messages start with any number of any of the 42 possibilities
# 11 is a little trickier, it's pattern is 42 then itself then 31, which just means that at the end of the message, 42 needs to occur as many times as 31
# so to boil it down, at a minimum the message needs to start with a 42 combo, then it needs to have another 42 combo and a 31 combo, therefore we need to check for 2 things
# 1: the pattern needs to be 42x 42y 31y, and therefore the occurances for 42 must be greater then that of 31. Now the easy part, write code!

# get list of possibilities for 42 and 31
pos_for_42 = [string.replace('"', "") for string in find_possible_strings("42", [""])]
pos_for_31 = [string.replace('"', "") for string in find_possible_strings("31", [""])]
# create strings from both of those lists that will work in regex
string_for_31 = f"({")|(".join(pos_for_31)})"
string_for_42 = f"({")|(".join(pos_for_42)})"
# length of any combo in list (they are consistent thankfully)
len_42 = len(pos_for_42[0])
len_31 = len(pos_for_31[0])

# final counter var
matching_messages = 0
# loop through messages
for message in messages:
    # quick filter to make sure the message pattern is ok
    if not re.fullmatch(r'^(' + string_for_42 + r')+(' + string_for_31 + r')+$', message): continue
    # more temp counters
    match_42 = 0
    match_31 = 0
    # 42s will always be before 31s, so if the beginning of the string matches a 42 combo, add 1 to the counter and slice it
    while message.startswith(tuple(pos_for_42)):
        match_42 += 1
        message = message[len_42:]
    # once 42s are gone, do the same for 31s
    while message.startswith(tuple(pos_for_31)):
        match_31 += 1
        message = message[len_31:]

    # finally, if the 42s are greater then the 31s, the final counter
    if match_42 > match_31: matching_messages += 1

# certainly a convoluted way to make this work, but I'm trying to fix my sleep schedule and my head ain't worken right, so it's what we got for today
print(matching_messages)