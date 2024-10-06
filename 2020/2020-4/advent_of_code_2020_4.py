import re
master_list = ["ecl", "eyr", "hcl", "pid", "iyr", "byr", "hgt"]

# import file
with open("./input.txt", "r") as tfile:
    text = tfile.read()

# create array based on single line strings on empty new lines then strip
text_array = text.split("\n\n")

# create array of 3 char items based on : char
text_array = [item.replace("\n", " ").strip() for item in text_array]

possible_passports = [{item[:3]:item[4:] for item in passport} for passport in[item.split(" ") for item in text_array if all(e in item for e in master_list)]]

real_passports1 = [passport for passport in possible_passports if 
                  (1920 <= int(passport["byr"]) <= 2002) and 
                  (2010 <= int(passport["iyr"]) <= 2020) and 
                  (2020 <= int(passport["eyr"]) <= 2030) and 
                  ((re.match(r'\d{3}cm', passport["hgt"]) and 150 <= int(passport["hgt"][:3]) <= 193) or (re.match(r'\d{2}in', passport["hgt"]) and 59 <= int(passport["hgt"][:2]) <= 76)) and
                  (re.match(r'#[0-9a-f]{6}', passport["hcl"])) and
                  (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and 
                  (re.match(r'^\d{9}$', passport["pid"]))]

print(len(real_passports1))