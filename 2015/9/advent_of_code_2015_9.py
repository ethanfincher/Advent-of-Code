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

max_distance = 0

def travel_cities(current_city, remaining_cities, total_distance):
    if not remaining_cities:
        global max_distance
        # for part 2, just change min to max and change less than to greater than
        if total_distance > max_distance:
            max_distance = total_distance
    else:
        for remaining_city in remaining_cities:
            route_distance = next(iter([value for key, value in city_routes.items() if all(city in key for city in [current_city, remaining_city])]), None)
            travel_cities(remaining_city, [city for city in remaining_cities if city != remaining_city], total_distance + route_distance)

for starting_city in all_cities:
    travel_cities(starting_city, [city for city in all_cities if city != starting_city], 0)
print(max_distance)