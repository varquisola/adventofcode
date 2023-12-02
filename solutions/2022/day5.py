"""
            [G] [W]         [Q]
[Z]         [Q] [M]     [J] [F]
[V]         [V] [S] [F] [N] [R]
[T]         [F] [C] [H] [F] [W] [P]
[B] [L]     [L] [J] [C] [V] [D] [V]
[J] [V] [F] [N] [T] [T] [C] [Z] [W]
[G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
[R] [J] [S] [Z] [R] [S] [D] [L] [J]
 1   2   3   4   5   6   7   8   9
"""
import re

config = {
    1: ['R', 'G', 'J', 'B', 'T', 'V', 'Z'],
    2: ['J', 'R', 'V', 'L'],
    3: ['S', 'Q', 'F'],
    4: ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'],
    5: ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'],
    6: ['S', 'W', 'T', 'C', 'H', 'F'],
    7: ['D', 'Z', 'C', 'V', 'F', 'N', 'J'],
    8: ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'],
    9: ['J', 'B', 'W', 'V', 'P']
}


def process_instructions(instructions):
    copy_config = config.copy()

    for line in instructions:
        p = re.compile(r'\d+')
        extracted_info = p.findall(line)
        num_to_move, source, dest = int(extracted_info[0]), int(extracted_info[1]), int(extracted_info[2])
        source_row = copy_config[source]
        len_source_row = len(source_row)
        copy_config[dest].extend(source_row[len_source_row-num_to_move:len_source_row])
        for i in range(num_to_move):
            copy_config[source].pop()

    result = ""
    for key in copy_config.keys():
        result += copy_config[key][-1]

    return result
