def read_input_file(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    return lines


def decimal_to_binary(num):
    return bin(num).replace("0b", "")


def binary_to_decimal(num):
    return int(num, 2)



