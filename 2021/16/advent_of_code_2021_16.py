# decode hex transmission dict
hex_to_bit = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
bit_string = ""
for char in open("2021\\16\\input.txt").read().strip():
    bit_string += hex_to_bit[char]

version_counter = 0

def to_int(bits):
    return int(bits, 2)

def process_bits(num_of_bits, bit_string):
    popped_bits = bit_string[:num_of_bits]
    bit_string = bit_string[num_of_bits:]
    return bit_string, popped_bits

def find_packet(bit_string):
    global version_counter

    # now to find packets. packets always start with 6 bits
    # first 3 are are version number
    bit_string, version_number_bits = process_bits(3, bit_string)
    version_number = to_int(version_number_bits)
    version_counter += version_number

    # second 3 are packet type ID
    bit_string, packet_type_bits = process_bits(3, bit_string)
    packet_type = to_int(packet_type_bits)

    # now we need to determine what kind of packet it is. This is determined by the type ID
    # if the type ID is 4, we're working with a literal packet
    if packet_type == 4:
        first_bit = "1"
        # this is followed by a series of 5 bits. the first bit determines if there are more numbers (1), or if this is the last number (0)
        while first_bit == "1":
            bit_string, next_number_group = process_bits(5, bit_string)
            first_bit = next_number_group[0]
            current_num = to_int(next_number_group[1:])
            
    # anything else and its an operator packet
    else:
        # the bit after the packet type is the length type
        bit_string, length_type = process_bits(1, bit_string)
        # if the length type is 0, the next 15 bits determine the length in bits of this operator packet's sub packets
        if length_type == "0":
            bit_string, length_bits = process_bits(15, bit_string)
            length_of_sub_packet_bits = to_int(length_bits)
            bit_string, bit_substring = process_bits(length_of_sub_packet_bits, bit_string)
            while bit_substring:
                bit_substring = find_packet(bit_substring)

        # if its a 1, then the next 11 bits are a number that represent the number of sub packets in the current operator packet
        elif length_type == "1":
            bit_string, length_bits = process_bits(11, bit_string)
            num_of_sub_packets = to_int(length_bits)
            for _ in range(num_of_sub_packets):
                bit_string = find_packet(bit_string)
    return bit_string

# Part 1 is to find the sum of the version numbers of all the packets
find_packet(bit_string)
print(version_counter)