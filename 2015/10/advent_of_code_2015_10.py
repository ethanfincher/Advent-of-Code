import itertools
current_numbers = open("2015/10/input.txt").read()

for _ in range(50):
    new_string = []
    number_groups = [''.join(group) for _, group in itertools.groupby(current_numbers)]
    for number_group in number_groups:
        new_string.append(f"{len(number_group)}{number_group[0]}")
    current_numbers = "".join(new_string)
print(len(current_numbers))