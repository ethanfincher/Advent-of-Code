hands = [[int(num) for num in player.split('\n')[1:]] for player in open("2020\\2020-22\\input.txt").read().strip().split("\n\n")]
player_1 = hands[0]
player_2 = hands[1]
def play_game(hand_1, hand_2):
    plays_history = []
    hands_history = []
    counter = 0
    while all(len(hand) != 0 for hand in [hand_1, hand_2]):
        counter += 1
        # check if exact hand has been played before
        # get indexes this play has occured
        indices = [i for i, x in enumerate(plays_history) if x == [hand_1[0],hand_2[0]]]
        # if this play (2 cards being compared) has occured before
        if indices:
            # see if there is a match in hands history
            if any([hand_1,hand_2] == hands for hands in [hands_history[index] for index in indices]):
                break
        plays_history.append([hand_1[0],hand_2[0]])
        hands_history.append([hand for hand in [hand_1[:],hand_2[:]]])
        # check if we need to start a recursive game
        if len(hand_1[1:]) >= hand_1[0] and len(hand_2[1:]) >= hand_2[0]:
            if play_game(hand_1[1:hand_1[0]+1], hand_2[1:hand_2[0]+1])[0] == 1:
                hand_1.extend([hand_1[0], hand_2[0]])
            else:
                hand_2.extend([hand_2[0], hand_1[0]])
        # if not, play like normal
        else:
            if hand_1[0] > hand_2[0]:
                hand_1.extend([hand_1[0], hand_2[0]])
            else:
                hand_2.extend([hand_2[0], hand_1[0]])
        hand_1 = hand_1[1:]
        hand_2 = hand_2[1:]
    # runs if game exits naturally (no repeat hands)
    else:
        if len(hand_1) != 0: return (1, hand_1)
        else: return (2, hand_2)
    # player 1 wins if game ends with a duplicate hand (will only happen if while loop breaks)
    return (1, hand_1)
# winning_hand = [hand for hand in [player_1, player_2] if len(hand) != 0][0]
winning_hand = play_game(player_1, player_2)[1]

total = 0
for index, num in enumerate(winning_hand[::-1]):
    total += num * (index+1)
print(total)