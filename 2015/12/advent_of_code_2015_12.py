import re
import json
raw_input = open("2015/12/input.txt").read().strip()
full_json = json.loads(raw_input)

def find_numbers(object):
    total = 0
    if type(object) == dict:
        if not any (value == "red" for value in object.values()):
            for value in object.values():
                total += find_numbers(value)
    if type(object) == list:
        for item in object:
            total += find_numbers(item)
    else:
        if type(object) == int:
            total += object
    return total

print(find_numbers(full_json))