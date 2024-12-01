lines = open("2024/1/input.txt").read().strip().split("\n")
map_1 = []
map_2 = []
for line in lines:
    maps = line.split("   ")
    map_1.append(int(maps[0]))
    map_2.append(int(maps[1]))

map_1.sort()
map_2.sort()

difs = []
for index, location in enumerate(map_1):
    difs.append(abs(location - map_2[index]))

# print(sum(difs))

sim_score = 0

for location in map_1:
    sim_score += location * map_2.count(location)

print(sim_score)