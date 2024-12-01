target_number = int(open("2015/20/input.txt").read().strip())
def calc_presents(number):
    # Find divisors efficiently
    divisors = set()  # Use a set to avoid duplicates
    # Changes for part 2
    # for i in range(1, int(number**0.5) + 1):
    for i in range(1, min(51, int(number**0.5) + 1)):
        if number % i == 0:
            # Changes for part 2
            # divisors.add(i)
            divisors.add(number // i)  # Add the paired divisor
    # Sum and multiply by 11 (Part 2) or 10 (Part 1)
    return sum(divisors) * 11



house_number = 1
while True:
    presents = calc_presents(house_number)
    if presents >= target_number: 
        print(house_number)
        break
    else:
        house_number += 1
