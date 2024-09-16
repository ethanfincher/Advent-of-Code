with open("2020-1\input.txt", "r") as input_file:
    input = input_file.read()

numbers = [int(num) for num in input.strip().split("\n")]
for index, num in enumerate(numbers):
    for i in range(index+1, len(numbers) - 2):
        for j in range(index+2, len(numbers) - 1):
            if num+numbers[i]+numbers[j] == 2020:
                print(num*numbers[i]*numbers[j])
                exit()