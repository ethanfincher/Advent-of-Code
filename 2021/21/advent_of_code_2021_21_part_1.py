starting_positions = [int(line[-1]) for line in open("2021/21/input.txt").read().strip().split("\n")]
p1_position = starting_positions[0]
p1_score = 0
p2_position = starting_positions[1]
p2_score = 0

def play_turn(starting_position, die_number):
    new_position = (starting_position + ((die_number+1) + (die_number+2) + (die_number+3))) % 10
    if new_position == 0: new_position = 10
    return new_position
    

die_number = 0
while p2_score < 1000:
    p1_position = play_turn(p1_position, die_number)
    p1_score += p1_position
    die_number += 3
    if p1_score >= 1000: break

    p2_position = play_turn(p2_position, die_number)
    p2_score += p2_position
    die_number += 3

print((die_number) * [score for score in (p1_score, p2_score) if score < 1000][0])