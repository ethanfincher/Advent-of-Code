input_sections = open("2021/19/input.txt").read().strip().split("\n\n")
scanners = [[[int(num) for num in text.split(",")] for text in lines.split("\n")[1:]] for lines in input_sections]
scanner_difs = []
# goal of this is to find absolute difference between all beacons in a scanner by axis
for scanner in scanners:
    scanner_dif = []
    for index, beacon in enumerate(scanner):
        other_beacons = scanner[:index] + scanner[index+1:]
        beacon_dif = []
        for axis_index, axis in enumerate(beacon):
            axis_difs = []
            for other_beacon in other_beacons:
                axis_difs.append(abs(axis - other_beacon[axis_index]))
            beacon_dif.append(axis_difs)
        scanner_dif.append(beacon_dif)
    scanner_difs.append(scanner_dif)

# go through all scanner difs and find their matching pair
# once a pair is found, mark the match as the new current scanner, and remove the last scanner from scanner_difs
scanner_matches = {i:[] for i in range(len(scanner_difs))}
for index, current_scanner in enumerate(scanner_difs):
    orientation = 0
    while orientation < 3:
        # check all other scanners for a match on the current orientation
        for other_scanner in [other_scanner for other_scanner in scanner_difs if other_scanner != current_scanner]:
            beacon_matchups = {}
            # check each beacon of scanner being compared
            for other_beacon_index, other_beacon in enumerate(other_scanner):
                # check beacon being compared to all current beacons
                for current_beacon_index, current_beacon in enumerate(current_scanner):
                    # if 11 or more beacon differences are found
                    if len([dif for dif in other_beacon[orientation] if dif in current_beacon[0]]) >= 11:
                        # add to beacon matchups
                        beacon_matchups[current_beacon_index] = other_beacon_index
            # if 12 beacons are found to be simular in the current comparison scanner, a match has been found
            if len(beacon_matchups) >= 12:
                scanner_matches[index].append(scanner_difs.index(other_scanner))
        orientation += 1
print(scanner_matches)