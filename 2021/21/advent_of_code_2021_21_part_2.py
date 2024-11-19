from functools import lru_cache
# going to aproach using cached game statuses
# at any given point, a game has x states
# p_turn, die total, p1_total, p2_total, p1_pos, p2_pos
# the last thing you need for a state is; should that state be followed to the end, how many p1_wins and p2_wins occur
possible_die_totals = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9]
                                                                                                                                                               
@lru_cache(maxsize=None)  # Set maxsize=None for an unlimited cache
def play_turn(is_p1_turn, die_total, p1_total, p1_pos, p2_total, p2_pos):
    outcome = {"p1_wins": 0, "p2_wins": 0}
    
    if is_p1_turn:
        p1_pos = (p1_pos + die_total) % 10 or 10
        p1_total += p1_pos
    else:
        p2_pos = (p2_pos + die_total) % 10 or 10
        p2_total += p2_pos

    if p1_total >= 21: 
        outcome["p1_wins"] = 1
        return outcome
    elif p2_total >= 21:
        outcome["p2_wins"] = 1
        return outcome
    else:
        for new_die_total in possible_die_totals:
            next_turns = play_turn(not is_p1_turn, new_die_total, p1_total, p1_pos, p2_total, p2_pos)
            outcome = {key: outcome[key] + next_turns[key] for key in outcome}
        return outcome
    

starting_positions = [int(line[-1]) for line in open("2021/21/input.txt").read().strip().split("\n")]
total_outcome = {"p1_wins": 0, "p2_wins": 0}
for new_die_total in possible_die_totals:
        next_turns = play_turn(True, new_die_total, 0, starting_positions[0], 0, starting_positions[1])
        total_outcome = {key: total_outcome[key] + next_turns[key] for key in total_outcome}
print(total_outcome)