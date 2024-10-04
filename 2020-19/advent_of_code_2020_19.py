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

possible_strings = [len(string.replace('"', "")) for string in find_possible_strings("31", [""])]
print(possible_strings)
possible_strings = [len(string.replace('"', "")) for string in find_possible_strings("42", [""])]
print(possible_strings)
# print(sum([1 for match in messages if match in possible_strings]))