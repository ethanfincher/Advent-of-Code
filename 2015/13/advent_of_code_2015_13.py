import re
raw_input = open("2015/13/input.txt").read().strip().split("\n")
# Set of all names
all_people = set()
# Dict with names of each people as key, and the value being a nested dict with names of other people the their neighbor value
people_dict = {}
for line in raw_input:
    line_re = re.search(r"^(\w+).*?(\w+) (\d+).* \b(\w+).$", line)
    current_person = line_re.group(1)
    all_people.add(current_person)
    number = int(line_re.group(3)) * (-1 if line_re.group(2) == "lose" else 1)
    neighbor = line_re.group(4)
    people_dict.setdefault(current_person,{})[neighbor] = number

# Part 2 adds me
for person in people_dict:
    people_dict[person]["Ethan"] = 0
people_dict["Ethan"] = {person: 0 for person in all_people}
all_people.add("Ethan")

totals = []
def seat_people(starting_person, current_total, remaining_people, current_person):
    # removes current person from remaining people to seat
    remaining_people = [person for person in remaining_people if person != current_person]
    # if the last person is seated, add the value of that person and the first person (close the loop). Add the total to totals
    if not remaining_people:
        totals.append(current_total + people_dict[starting_person][current_person] + people_dict[current_person][starting_person])
    # otherwise, find the new total for the current person and every other remaining person, and seat the new person
    else:
        for person in remaining_people:
            new_total = current_total + people_dict[current_person][person] + people_dict[person][current_person]
            seat_people(starting_person, new_total, remaining_people, person)

# go through every person as the first person seated and find all totals to populate totals list
for person in all_people:
    seat_people(person, 0, list(all_people), person)

print(max(totals))