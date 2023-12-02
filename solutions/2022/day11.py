import math
import re

from util import read_input_file


def parse_inputs(lines):
    monkeys = {}
    monkey_ops = {}
    monkey_test = {}
    p = re.compile(r'\d+')
    for line in lines:
        cmd = line.strip().split(' ')
        if cmd[0] == 'Monkey':
            curr_monkey = int(cmd[1].strip(':'))
            monkeys[curr_monkey] = []
        elif cmd[0] == 'Starting':
            nums = p.findall(line)
            for num in nums:
                monkeys[curr_monkey].append(int(num))
        elif cmd[0] == 'Operation:':
            # Interpret the op
            monkey_ops[curr_monkey] = cmd[3:6]
        elif cmd[0] == 'Test:':
            monkey_test[curr_monkey] = [cmd[3]]
        elif cmd[0] == 'If' and cmd[1] == 'true:':
            monkey_test[curr_monkey].extend(cmd[5])
        elif cmd[0] == 'If' and cmd[1] == 'false:':
            monkey_test[curr_monkey].extend(cmd[5])

    return monkeys, monkey_ops, monkey_test


def monkey_moves(monkey_map, monkey_ops, monkey_test):
    monkey_op_counts = [0 for _ in range(len(monkey_map))]
    for _ in range(10000):
        for i in range(len(monkey_map)):
            print('Monkey: ', i)
            while len(monkey_map[i]) > 0:
                # Execute operation
                curr_item_worry_level = monkey_map[i].pop(0)
                print("At pop:", curr_item_worry_level)
                left, op, right = monkey_ops[i][0], monkey_ops[i][1], monkey_ops[i][2]
                if op == '+':
                    if left == 'old' and right == 'old':
                        curr_item_worry_level = curr_item_worry_level + curr_item_worry_level
                    elif left == 'old' and right != 'old':
                        curr_item_worry_level = curr_item_worry_level + int(right)
                    elif left != 'old' and right == 'old':
                        curr_item_worry_level = int(left) + curr_item_worry_level
                elif op == '-':
                    if left == 'old' and right == 'old':
                        curr_item_worry_level = curr_item_worry_level - curr_item_worry_level
                    elif left == 'old' and right != 'old':
                        curr_item_worry_level = curr_item_worry_level - int(right)
                    elif left != 'old' and right == 'old':
                        curr_item_worry_level = int(left) - curr_item_worry_level
                elif op == '*':
                    if left == 'old' and right == 'old':
                        curr_item_worry_level = curr_item_worry_level * curr_item_worry_level
                    elif left == 'old' and right != 'old':
                        curr_item_worry_level = curr_item_worry_level * int(right)
                    elif left != 'old' and right == 'old':
                        curr_item_worry_level = int(left) * curr_item_worry_level
                elif op == '/':
                    if left == 'old' and right == 'old':
                        curr_item_worry_level = int(curr_item_worry_level / curr_item_worry_level)
                    elif left == 'old' and right != 'old':
                        curr_item_worry_level = int(curr_item_worry_level / int(right))
                    elif left != 'old' and right == 'old':
                        curr_item_worry_level = int(int(left) / curr_item_worry_level)

                # Count monkey op
                monkey_op_counts[i] += 1

                # Divide by 3 if not worried
                # curr_item_worry_level = int(curr_item_worry_level / 3)
                curr_item_worry_level = curr_item_worry_level % math.prod(int(monkey_test[i][0]) for i in range(len(monkey_test)))
                # print('At divide by 3: ', curr_item_worry_level)
                # Check if current worry level divisible by test
                if curr_item_worry_level % int(monkey_test[i][0]) == 0:
                    target_monkey = int(monkey_test[i][1])
                    print('Throwing to monkey: ', target_monkey)
                    monkey_map[target_monkey].append(curr_item_worry_level)
                    print('Monkey map after throw: ', monkey_map)
                else:
                    target_monkey = int(monkey_test[i][2])
                    print('Throwing to monkey: ', target_monkey)
                    monkey_map[target_monkey].append(curr_item_worry_level)
                    print('Monkey map after throw: ', monkey_map)

    monkey_op_counts.sort(reverse=True)
    print(monkey_map)
    print(monkey_op_counts)
    return monkey_op_counts[0] * monkey_op_counts[1]

def solve():
    lines = read_input_file('inputs/day11.txt')
    monkey_map, monkey_ops, monkey_test = parse_inputs(lines)
    monkey_business = monkey_moves(monkey_map, monkey_ops, monkey_test)
    print(monkey_business)

