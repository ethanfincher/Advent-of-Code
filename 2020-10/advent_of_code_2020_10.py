with open("2020-10\input.txt", "r") as tfile:
    jolts_list = [int(jolt) for jolt in tfile.read().strip().split("\n")]
    jolts_list.sort()
    jolts_list.insert(0, 0)
    jolts_list.append(jolts_list[len(jolts_list) -1] + 3)
# Part 1
jolt_jumps = []
for index, jolt in enumerate(jolts_list[:-1]):
    jolt_jumps.append(jolts_list[index+1] - jolt)
print(jolt_jumps.count(1) * jolt_jumps.count(3))

# Part 2
def number_finder(num):
    result = 1
    for i in range(1, num + 1):
        result = result + (i-1)
    return result

result = 1
ones_in_a_row = 0
for index, jump in enumerate(jolt_jumps):
    # if jump is a one, increase incrementor
    if jump == 1: ones_in_a_row += 1
    # if it is not or its the last item in list, call number finder and multiply result
    if jump == 3 or index == len(jolt_jumps) - 1:
        if ones_in_a_row >= 2:
            result = result * number_finder(ones_in_a_row)
        ones_in_a_row = 0
print(result)