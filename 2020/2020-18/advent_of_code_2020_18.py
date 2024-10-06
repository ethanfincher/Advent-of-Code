import re
# Part 1
with open("2020-18\\input.txt", "r") as tfile:
    expressions = tfile.read().strip().split("\n")

def funny_math(exp: str) -> str:
    while re.search(r"[+]", exp):
        exp_chunk = re.findall(r"\d+ [+] \d+", exp)[0]
        exp = exp.replace(exp_chunk, str(eval(exp_chunk)), 1)
    while not re.search(r"^\d*$", exp):
        exp_chunk = re.findall(r"\d+ [*] \d+", exp)[0]
        exp = exp.replace(exp_chunk, str(eval(exp_chunk)), 1)
    return exp

my_total = 0
for index, exp in enumerate(expressions):
    while exp.count("("):
        for match in re.findall(r'\([\d *+]*\)', exp):
            exp = exp.replace(match, funny_math(match[1:-1]))
    my_total += int(funny_math(exp))
print(my_total)

# Part 2 just added the first while loop to funny_math to calculate addition first