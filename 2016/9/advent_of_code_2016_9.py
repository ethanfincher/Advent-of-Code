import re
uncompressed_chars = open("2016/9/input.txt").read().strip()
# Part 1
# compressed_chars = ""
# index = 0
# while index < len(uncompressed_chars):
#     if uncompressed_chars[index] == "(":
#         num_of_chars = int(re.search(r'(\d+)x', uncompressed_chars[index:]).group(1))
#         num_of_repeats = int(re.search(r'x(\d+)\)', uncompressed_chars[index:]).group(1))
#         string_chunk_start = int(re.search(r'\)', uncompressed_chars[index:]).end()) + index
#         compressed_chars += uncompressed_chars[string_chunk_start:string_chunk_start+num_of_chars] * num_of_repeats
#         index = string_chunk_start+num_of_chars
#     else:
#         compressed_chars += uncompressed_chars[index]
#         index += 1
# print(len(compressed_chars))

# Part 2
def decompress(char_set):
    total_length = 0
    index = 0
    while index < len(char_set):
        if char_set[index] == "(":
            num_of_chars = int(re.search(r'(\d+)x', char_set[index:]).group(1))
            num_of_repeats = int(re.search(r'x(\d+)\)', char_set[index:]).group(1))
            string_chunk_start = int(re.search(r'\)', char_set[index:]).end()) + index
            new_substring = char_set[string_chunk_start:string_chunk_start+num_of_chars]
            total_length += decompress(new_substring) * num_of_repeats
            index = string_chunk_start+num_of_chars
        else:
            index += 1
            total_length += 1

    return total_length

print(decompress(uncompressed_chars))