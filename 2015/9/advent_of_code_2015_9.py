import re
lines = open("2015/9/input.txt").read().strip().split("\n")
city_routes = {}
all_cities = []
for line in lines:
    line_regex = re.search(r"(\w+) to (\w+) = (\d+)", line)
    current_cities = [line_regex.group(1), line_regex.group(2)]
    all_cities.extend(current_cities)
    city_routes[f"{line_regex.group(1)},{line_regex.group(2)}"] = int(line_regex.group(3))
all_cities = list(set(all_cities))

# print(max(city_routes, key=city_routes.get))
min_distance = 100000000000000
for starting_city in all_cities:
    remaining_cities = [city for city in all_cities if city != starting_city]
    