public_keys = [int(line) for line in open("2020\\2020-25\\input.txt").read().strip().split("\n")]
loop_sizes = []
for key in public_keys:
    loop_size = 0
    value = 1
    while value != key:
        loop_size += 1
        value *= 7
        value = value % 20201227
    loop_sizes.append(loop_size)
encryption_key = 1
for _ in range(loop_sizes[1]):
    encryption_key *= public_keys[0]
    encryption_key = encryption_key % 20201227
print(encryption_key)