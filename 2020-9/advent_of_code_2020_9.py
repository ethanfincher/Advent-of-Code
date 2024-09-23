# Part 1
with open("2020-9\input.txt", "r") as tfile:
    num_list = [int(num) for num in tfile.read().strip().split("\n")]
# for every number in the list after the preamble
for index, target_num in enumerate(num_list[25:]):
    # index of the current preamble
    index = index+25
    sum_found = False
    # for every number in the 25 numbers before the target num (except for the last one)
    for i in num_list[index-25:index-1]:
        # current position of the first number to add
        i_position = num_list.index(i)
        # for every number between first number to add and the target number
        for j in num_list[i_position+1:index]:
            # if the first and second numbers add together, then set sum_found and break to target num loop
            if i + j == target_num:
                sum_found = True
                break
        if sum_found: break
    # either the summing loops have broken or ended at this point
    # if they broke then sum_found is true and the loop continues
    # if not then print the number and break the loop
    if not sum_found: print(f"bad number is {target_num}"); break
# Part 2
target_num = 36845998
for index, i in enumerate(num_list):
    total_sum = i
    for j in num_list[index+1:]:
        total_sum += j
        if total_sum == target_num:
            print(f"{i} + {j} = {i+j}")
            exit()
        elif i + j > target_num: break