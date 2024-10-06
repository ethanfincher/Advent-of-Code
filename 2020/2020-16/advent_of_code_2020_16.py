import numpy
import re
with open("2020-16\\input.txt", "r") as tfile:
    input_parts = tfile.read().strip().split("\n\n")

# Part 1
# # make list of exceptable numbers
fields = input_parts[0].split("\n")
acceptable_numbers = []
for field in fields:
    field_regex = re.search(r"(\d*)-(\d*) or (\d*)-(\d*)", field)
    acceptable_numbers.extend(list(range(int(field_regex.group(1)), int(field_regex.group(2)) + 1)))
    acceptable_numbers.extend(list(range(int(field_regex.group(3)), int(field_regex.group(4)) + 1)))
acceptable_numbers = list(set(acceptable_numbers))

# # make list of ticket numbers
# ticket_numbers = input_parts[2].replace("nearby tickets:", "").strip().replace("\n", ",").split(",")

# # calculate scanning_error_rate
# scanning_error_rate = 0
# for number in ticket_numbers:
#     if int(number) not in acceptable_numbers: scanning_error_rate += int(number)
# print(scanning_error_rate)

# Part 2, yes I could have made this faster using a max and min number to compare instead of creating a whole list of possible numbers, but the input is small enough and this is more readable to me
# Create a list of tickets, with a ticket being an int list of numbers
tickets = [[int(number) for number in ticket.split(",")] for ticket in input_parts[2].replace("nearby tickets:", "").strip().split("\n")]

# Remove bad tickets from ticket list
naughty_list = []
for ticket in tickets:
    for number in ticket:
        if number not in acceptable_numbers:
            naughty_list.append(ticket)
            break
tickets = [ticket for ticket in tickets if ticket not in naughty_list]

# make list of possible numbers per field
field_number_ranges = {}
for field in fields:
    field_regex = re.search(r"^([\w ]*): (\d*)-(\d*) or (\d*)-(\d*)$", field)
    field_number_ranges[field_regex.group(1)] = list(range(int(field_regex.group(2)), int(field_regex.group(3)) + 1)) + list(range(int(field_regex.group(4)), int(field_regex.group(5)) + 1))

def check_single_possibility(possible_fields, fields_by_index):
    for current_index_possible_fields in fields_by_index:
        if len(current_index_possible_fields) == 1 and current_index_possible_fields[0] in possible_fields:
            possible_fields.remove(current_index_possible_fields[0])
            fields_by_index = [[item for item in sublist if len(sublist) == 1 or item != current_index_possible_fields[0]] for sublist in fields_by_index]
            possible_fields, fields_by_index = check_single_possibility(possible_fields, fields_by_index)
    return (possible_fields, fields_by_index)


# this is a list of field names that are still availible
possible_fields = [key for key in field_number_ranges]
# this is the master list. each index in this list is a list of keywords that the matching index on any ticket could be
fields_by_index = []
# for each column of numbers in tickets
for index, col in enumerate(tickets[0]):
    # add all availible fields to the column
    fields_by_index.append(possible_fields[:])
    # for each number in that column
    for row in tickets:
        # check every field in the remaining possible fields (makes for loop simpler then checking and removing from the current index's possible fields)
        for field in possible_fields:
            # if the current number isnt in the field's range of numbers and the field is still one of the possible fields for the column, remove it
            if field in fields_by_index[index] and row[index] not in field_number_ranges[field]: fields_by_index[index].remove(field)
    # once all impossible fields have been filtered from the current col, if there was only one possibility (and that possibility is still on the posibility list for recursion), remove that possibility from all other cols and the possible_fields list
    # call this recursivly just incase this created another single possibility
    possible_fields, fields_by_index = check_single_possibility(possible_fields, fields_by_index)

# create list of indexes of fields with the word departure by flattening out the fields_by_index list
departure_indexes = [index for index, field in enumerate([ item for innerlist in fields_by_index for item in innerlist ]) if field.count("departure")]
my_ticket_departures = [int(num) for index, num in enumerate(input_parts[1].split("\n")[1].split(",")) if index in departure_indexes]
print(numpy.prod(my_ticket_departures))