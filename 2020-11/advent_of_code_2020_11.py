import copy
# Part 1
with open("2020-11\input.txt", "r") as tfile:
    seats = [list(row) for row in tfile.read().strip().split("\n")]
rows = len(seats)
cols = len(seats[0])
new_seats = [[0 for i in range(cols)] for j in range(rows)]

def count_occupied_seats(row_index, col_index):

    def check_direction(row_delta, col_delta):
        # create instance of params
        current_row, current_col = row_index, col_index
        # while grid points are in bounds
        while 0 <= current_row + row_delta < rows and 0 <= current_col + col_delta < cols:
            current_row += row_delta
            current_col += col_delta
            if seats[current_row][current_col] == "#":
                return 1  # Found an occupied seat
            if seats[current_row][current_col] == "L":
                return 0 # No occupied seat found
        return 0  # No occupied seat found

    # Check all directions
    occupied_seats = (
        check_direction(-1, -1) +  # Top left
        check_direction(-1, 0) +   # Top
        check_direction(-1, 1) +   # Top right
        check_direction(0, -1) +   # Left 
        check_direction(0, 1) +    # Right
        check_direction(1, -1) +   # Bottom left
        check_direction(1, 0) +    # Bottom
        check_direction(1, 1)      # Bottom right
    )

    return occupied_seats

no_more_seat_changes = False
while not no_more_seat_changes:
    for row_index, row in enumerate(seats):
        for col_index, col in enumerate(row):
            # if current spot is floor, continue
            if col == ".":
                new_seats[row_index][col_index] = "."
                continue
            # Run function to find number of seats visible from current spot
            occupied_seats = count_occupied_seats(row_index, col_index)
            if col == "L":
                # if seat to check is empty, if no seats were taken, add taken to the list
                if not occupied_seats: new_seats[row_index][col_index] = "#"
                # if seat to check is empty and any seats are taken, add empty to list
                else: new_seats[row_index][col_index] = "L"
            else: 
                # if seat is taken, and seats taken is less then 4, add taken to list
                if occupied_seats >= 5: new_seats[row_index][col_index] = "L"
                # if seat is taken and 4 seats are taken, add empty to list
                else: new_seats[row_index][col_index] = "#"
    # if no seats have changed, then exit the loop
    if seats == new_seats:
        no_more_seat_changes = True
    else:
        # otherwise, set seats equal (to a copy of) the new seats
        seats = copy.deepcopy(new_seats)
print(sum([row.count("#") for row in seats]))
# Part 2 turns the position checkers into while loops