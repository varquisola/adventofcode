from util import read_input_file
from functools import cmp_to_key


def compare(left, right):
    if type(left) is list and type(right) is list:
        inner_len = min(len(left), len(right))

        for l in range(inner_len):
            res = compare(left[l], right[l])
            if res == -1:
                return -1
            elif res == 1:
                return 1

        else:
            if len(left) > len(right):
                return -1
            elif len(left) < len(right):
                return 1
            else:
                return 0
    elif type(left) is list:
        right = [right]
        return compare(left, right)
    elif type(right) is list:
        left = [left]
        return compare(left, right)
    else:
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0


def solve():
    data = open('inputs/testcase.txt').read().strip()
    print("Data:", data)
    for group in data.split('\n\n'):
        print("Group:",group)
        p1,p2 = group.split('\n')
        print(p1,p2)


    lines = read_input_file('inputs/day13.txt')
    contenders = {}
    num_lines = len(lines)
    index = 1
    for i in range(0, num_lines, 3):
        contenders[index] = []
        for j in range(2):
            contenders[index].append(eval(lines[i + j]))
        index += 1

    score = 0
    for i in range(len(contenders)):
        left = contenders[i + 1][0]
        right = contenders[i + 1][1]
        if compare(left, right) == 1:
            score += (i + 1)

    print("Part 1: ", score)


def part2():
    file_name = 'inputs/day13.txt'
    lines = []
    with open(file_name) as f:
        for line in f:
            line = line.strip('\n')
            if line != '':
                lines.append(eval(line))
    print(lines)

    lines.append([[2]])
    lines.append([[6]])
    contenders = {}
    num_lines = len(lines)
    index = 1
    print(lines)
    lines = sorted(lines, reverse=True, key=cmp_to_key(compare))
    print(lines)
    indices = []
    for i, line in enumerate(lines):
        if line == [[2]]:
            indices.append(i + 1)
        elif line == [[6]]:
            indices.append(i + 1)

    print(indices[0] * indices[1])

    # for i in range(0, num_lines, 3):
    #     contenders[index] = []
    #     for j in range(2):
    #         contenders[index].append(ast.literal_eval(lines[i + j]))
    #     index += 1
    #
    # score = 0
    # for i in range(len(contenders)):
    #     left = contenders[i + 1][0]
    #     right = contenders[i + 1][1]
    #     if compare(left, right) == 1:
    #         score += (i + 1)

