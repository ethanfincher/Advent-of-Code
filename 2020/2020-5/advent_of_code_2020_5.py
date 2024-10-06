# Part 1
with open("2020-5\input.txt", "r") as tfile:
    raw_seats = tfile.read()
seat_list = raw_seats.strip().split("\n")

highest_seat_number = 0
lowest_seat_number = 100000000
# This list is created using the highest and lowest seat numbers
possible_seat_ids = list(range(53, 896+1))

for seat in seat_list:
    possible_seat_rows = list(range(128))
    possible_seat_cols = list(range(8))
    for letter in seat[:7]:
        possible_seat_rows = possible_seat_rows[len(possible_seat_rows)//2:] if letter == "B" else possible_seat_rows[:len(possible_seat_rows)//2]
    for letter in seat[7:]:
        possible_seat_cols = possible_seat_cols[len(possible_seat_cols)//2:] if letter == "R" else possible_seat_cols[:len(possible_seat_cols)//2]
    seat_number = possible_seat_rows[0] * 8 + possible_seat_cols[0]
    if highest_seat_number < seat_number: highest_seat_number = seat_number
    if lowest_seat_number > seat_number: lowest_seat_number = seat_number
    print(seat_number)
    # Part 2 
    # Also added lowest_seat_number and possible_seat_ids to beginning
    possible_seat_ids.remove(seat_number)
print(lowest_seat_number)
print(highest_seat_number)
print(possible_seat_ids)