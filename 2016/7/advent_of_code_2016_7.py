import re
lines = open("2016/7/input.txt").read().strip().split("\n")

abba_ips = 0
aba_bab_ips = 0

for ip in lines:
    bracketed_parts = re.findall(r'\[(.*?)\]', ip)
    bracketless_parts = re.split(r'\[.*?\]', ip)
    # ABBA part
    if any(re.search(r"([a-z])(?!\1)([a-z])\2\1", part) for part in bracketless_parts):
        if not any(re.search(r"([a-z])(?!\1)([a-z])\2\1", part) for part in bracketed_parts):
            abba_ips += 1

    # ABA part
    ABAs = [aba for part_ABAs in [["".join(m.groups()) for m in re.finditer(r'(?=([a-z])(?!\1)([a-z])(\1))', part)] for part in bracketless_parts] for aba in part_ABAs]
    BABs = [bab for part_BABs in [["".join(m.groups()) for m in re.finditer(r'(?=([a-z])(?!\1)([a-z])(\1))', part)] for part in bracketed_parts] for bab in part_BABs]
    if ABAs and any(f"{aba[1]}{aba[0]}{aba[1]}" in BABs for aba in ABAs):
        aba_bab_ips += 1


print(abba_ips)
print(aba_bab_ips)