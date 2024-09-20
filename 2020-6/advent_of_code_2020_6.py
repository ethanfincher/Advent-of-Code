# Part 1
with open("2020-6\input.txt", "r") as tfile:
    raw_answers = tfile.read()
# Split based on empty new line
answer_groups = raw_answers.strip().split("\n\n")
# Create list of totals for each unique letter in every group
unique_chars_per_group = [len(set(group.replace("\n", ""))) for group in answer_groups]
print(sum(unique_chars_per_group))
# Part 2
total = 0
for group in answer_groups:
    # Number of people in each group is one more then the number of new lines
    people = group.count("\n") + 1
    # This creates a list of unique letters for a group
    # Then checks to see if the number of times that letter appears in total for the group is equal to the number of people
    for char in list(set(group.replace("\n", ""))):
        if group.count(char) == people:
            total += 1
print(total)