from itertools import product

# Set the total sum and number of elements
target_sum = 100
num_elements = 4

# Generate all combinations of numbers
combinations = []
for combo in product(range(1, target_sum + 1), repeat=num_elements):
    if sum(combo) == target_sum:
        combinations.append(combo)

# Print the results
print(f"Total combinations: {len(combinations)}")
# for combo in combinations:
#     print(combo)