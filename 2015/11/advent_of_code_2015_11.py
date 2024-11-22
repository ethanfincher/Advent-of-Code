import re
starting_password = "hxbxwxba"
# converts letters to numbers 1-26
password_numbers = [ord(letter.upper()) - ord('A') + 1 for letter in starting_password]

# checks that there are 3 ascending numbers in a row, and that there are 2 pairs of matching numbers
def check_validity(password):
    if any(password[i] == password[i+1]-1 == password[i+2]-2 for i in range(len(password_numbers)-2)) and len(re.findall(r'\b(\d+),\1\b', ",".join(str(num) for num in password))) >= 2:
        return True

index = -1
# added for part 2
first_match_found = False
while True:
    # replaces i, o, and l
    password_numbers = [num + 1 if num in [9, 12, 15] else num for num in password_numbers]
    if check_validity(password_numbers):
        # turns back into string
        print(''.join(chr(num + ord('A') - 1).lower() for num in password_numbers))
        if first_match_found:
            break
        else:
            first_match_found = True

    # if current index is z, go back to a and move to next index
    if password_numbers[index] == 26:
        password_numbers[index] = 1
        index -= 1
    # else, move to next letter in current index
    else:
        password_numbers[index] += 1
        index = -1