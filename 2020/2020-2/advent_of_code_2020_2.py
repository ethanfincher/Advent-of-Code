import re
# Part 1
with open("2020-2\input.txt", "r") as tfile:
    raw_passwords = tfile.read()

password_list = raw_passwords.strip().split("\n")

good_password_total_part_one = 0
good_password_total_part_two = 0
for password in password_list:
    # Get max and min from the string
    min = int(re.search(r'^(\d*)-' , password).group(1))
    max = int(re.search(r'-(\d*)' , password).group(1))
    # Get letter to match
    letter = re.search(r'(\w):' , password).group(1)
    # get string
    password_string = re.search(r': (\w*)$' , password).group(1)
    if min <= password_string.count(letter) <= max:
        good_password_total_part_one += 1
    # Part 2, everything can be done in the same loop
    # Subtract 1 to compensate for zero-index based arrays (silly normal-thinking sled rental company)
    first_position_match = password_string[min-1] == letter
    second_position_match = password_string[max-1] == letter
    if (first_position_match and not second_position_match) or (not first_position_match and second_position_match):
        good_password_total_part_two += 1

print(good_password_total_part_one)
print(good_password_total_part_two)