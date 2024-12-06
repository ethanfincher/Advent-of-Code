input_parts = open("2024/5/input.txt").read().strip().split("\n\n")
rules = [[int(num) for num in rule.split("|")] for rule in input_parts[0].split("\n")]
updates = [[int(num) for num in update.split(",")] for update in input_parts[1].split("\n")]

good_updates_total = 0
naughty_update_total = 0

for update in updates:
    # this extracts the first number (the one that goes first) in the rules that contain 2 numbers from the current update
    matching_rules = [rule[0] for rule in rules if rule[0] in update and rule[1] in update]
    # this creates an "empty" list the same length as the current update
    page_num_order = [0] * len(update)
    # the correct order of the numbers is just the order of whichever number appears on the mathching rules list from most to least
    for num in update:
        # this just does what the comment above explains, but uses the fact that we know the size of the update to automatically assign indexes based on 
        # how many numbers a given number is to the left of (occurances in matching_rules)
        page_num_order[len(update)-matching_rules.count(num)-1] = num
    # if they're the same, add the middle number of the update to the good list
    if update == page_num_order:
        good_updates_total += update[int((len(update) - 1)/2)]
    # if they're different, we've already calculated what the right order should be, so add the middle of that to the naughty list
    else:
        naughty_update_total += page_num_order[int((len(page_num_order) - 1)/2)]

print(good_updates_total)
print(naughty_update_total)