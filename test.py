# 1 = 1
# 2 = (1 + 1) 2
# 3 = (2 + 2) 4
# 4 = (3 + 4) 7
# 5 = (4 + 7) 11
# 6 = 16
# 7 = 22
# 8 = 29
# 9 = 37

def number_finder(num):
    result = 1
    for i in range(1, num + 1):
        result = result + (i-1)
    return result
num = 9

print(f"{num} final answer: {number_finder(num)}")