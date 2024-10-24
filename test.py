my_list = [3, 4, 6, 7, 2, 5, 8, 9, 1]
my_index = my_list.index(8)
for i in range(3):
    print(f"my index: {my_index}")
    print(f"length: {len(my_list)}")
    print(f"math: {my_index+1} mod {len(my_list)} == {(my_index+1)%len(my_list)}")
    print(f"{my_list.pop((my_index+1)%len(my_list))}")