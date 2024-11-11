import hashlib

def get_hash(value):
    return hashlib.md5(value.encode("utf-8")).hexdigest()

secret_key = open("2015/4/input.txt").read().strip()

current_lowest_hash = None
answer = 0
# got lucky with the range, im sure this is a horrible solution but the brute force worked this time
for i in range(100000,10000000):
    current_hash = get_hash(secret_key+str(i))
    if current_hash[0:6].count("0") == 6:
        if not current_lowest_hash or current_hash < current_lowest_hash:
            current_lowest_hash = current_hash
            answer = i
print(answer)