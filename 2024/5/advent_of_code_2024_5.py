input_parts = open("2024/5/input.txt").read().strip().split("\n\n")
rules = input_parts[0].split("\n")
rules = [[int(num) for num in rule.split("|")] for rule in rules]
updates = input_parts[1].split("\n")
updates = [[int(num) for num in update.split(",")] for update in updates]

good_updates_total = 0
naughty_update_total = 0

for update in updates:
    matching_rules = [rule[0] for rule in rules if rule[0] in update and rule[1] in update]
    matching_rules.sort()
    page_num_order = [0] * len(update)
    for num in update:
        page_num_order[len(update)-1-matching_rules.count(num)] = num
    if update == page_num_order:
        good_updates_total += update[int((len(update) - 1)/2)]
    else:
        naughty_update_total += page_num_order[int((len(page_num_order) - 1)/2)]

print(good_updates_total)
print(naughty_update_total)