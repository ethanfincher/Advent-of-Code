import re
reindeer_details = open("2015/14/input.txt").read().strip().split("\n")

scores = [0 for _ in range(len(reindeer_details))]
TOTAL_TIME = 2503
for seconds in range(1, TOTAL_TIME +1):
    distances = []
    for index, reindeer in enumerate(reindeer_details):
        line_re = [int(num) for num in re.findall(r"\d+", reindeer)]
        full_sets_distance = (seconds // (line_re[1] + line_re[2])) * line_re[0] * line_re[1]
        partial_set_distance = min([(seconds % (line_re[1] + line_re[2])), line_re[1]]) * line_re[0]
        distances.append(full_sets_distance + partial_set_distance)
    
    scores[distances.index(max(distances))] += 1
print(max(scores))