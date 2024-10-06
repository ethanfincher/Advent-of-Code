import re
with open("2020-7\input.txt", "r") as tfile:
    bag_requirements_list = tfile.read().strip().split("\n")
requirement_dicts = []
for requirement in bag_requirements_list:
    requirement_dict = {"parent_bag_color": "", "child_bags": []}
    requirement_dict["parent_bag_color"] = re.search(r'^(.*?) bag', requirement).group(1)
    for bag in re.findall(r'(\d+ .*?) bag', requirement):
        requirement_dict["child_bags"].append({
            "child_bag_color": re.search(r'\d* (.*)', bag).group(1),
            "num_of_bags": int(re.search(r'(\d*)', bag).group())
        })
    requirement_dicts.append(requirement_dict)

# Part 1
def find_parent_bag(child_bag_color):
    approved_bags_set = set()
    # find all parent bags that have a matching child bag color
    parent_bags = [parent_bag for parent_bag in requirement_dicts if [matching_bag for matching_bag in parent_bag["child_bags"] if matching_bag["child_bag_color"] == child_bag_color]]
    for parent_bag in parent_bags:
        # add bag color to set (to prevent dupes)
        approved_bags_set.add(parent_bag["parent_bag_color"])
        # call recursivly
        find_parent_bag(parent_bag["parent_bag_color"])
        return approved_bags_set
print(len(find_parent_bag("shiny gold")))

# Part 2
def sum_child_bags(parent_bag_color):
    bag_total = 0
    child_bags = next(bag for bag in requirement_dicts if bag["parent_bag_color"] == parent_bag_color)["child_bags"]
    for child_bag in child_bags:
        bag_total += child_bag["num_of_bags"] + (child_bag["num_of_bags"] * sum_child_bags(child_bag["child_bag_color"]))
    return bag_total

print(sum_child_bags("shiny gold"))