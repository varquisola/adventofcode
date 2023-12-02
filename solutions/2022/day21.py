def part1():
    monkeys = {}
    operations = {}
    with open('../../inputs/2022/day21.txt') as f:
        s = f.read().strip()
        lines = []
        for line in s.split("\n"):
            command = line.split(": ")
            a, b = command[0], command[1]
            lines.append((a, b))
            operations[a] = b.split(" ")

    for command in lines:
        a, b = command[0], command[1]
        if b.isnumeric():
            monkeys[a] = eval(b)

    while len(monkeys) != len(lines):
        for command in lines:
            a, b = command[0], command[1]
            if not b.isnumeric():
                ops = b.split(' ')
                c, d, e = ops[0], ops[1], ops[2]
                if d == '+' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) + int(monkeys[e])
                elif d == '-' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) - int(monkeys[e])
                elif d == '*' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) * int(monkeys[e])
                elif d == '/' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) // int(monkeys[e])
    print(monkeys['root'])



def evaluate(c):
    monkeys = {}
    operations = {}
    with open('../../inputs/2022/day21.txt') as f:
        s = f.read().strip()
        lines = []
        for line in s.split("\n"):
            command = line.split(": ")
            a, b = command[0], command[1]
            lines.append((a, b))
            operations[a] = b.split(" ")

    for command in lines:
        a, b = command[0], command[1]
        if b.isnumeric():
            if a == 'humn':
                monkeys[a] = c
            else:
                monkeys[a] = eval(b)

    while len(monkeys) != len(lines):
        for command in lines:
            a, b = command[0], command[1]
            if not b.isnumeric():
                ops = b.split(' ')
                c, d, e = ops[0], ops[1], ops[2]
                if d == '+' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) + int(monkeys[e])
                elif d == '-' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) - int(monkeys[e])
                elif d == '*' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) * int(monkeys[e])
                elif d == '/' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) // int(monkeys[e])

    return monkeys


def part2():
    monkeys = {}
    operations = {}
    with open('../../inputs/2022/day21.txt') as f:
        s = f.read().strip()
        lines = []
        for line in s.split("\n"):
            command = line.split(": ")
            a, b = command[0], command[1]
            lines.append((a, b))
            operations[a] = b.split(" ")

    for command in lines:
        a, b = command[0], command[1]
        if b.isnumeric():
            monkeys[a] = eval(b)

    while len(monkeys) != len(lines):
        for command in lines:
            a, b = command[0], command[1]
            if not b.isnumeric():
                ops = b.split(' ')
                c, d, e = ops[0], ops[1], ops[2]
                if d == '+' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) + int(monkeys[e])
                elif d == '-' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) - int(monkeys[e])
                elif d == '*' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) * int(monkeys[e])
                elif d == '/' and c in monkeys and e in monkeys:
                    monkeys[a] = int(monkeys[c]) // int(monkeys[e])

    a = 1
    b = int(1e16)
    while a < b:
        c = (a + b) // 2
        print(c)
        monkeys['humn'] = c
        monkeys = evaluate(c)
        if monkeys['vpmn'] < monkeys['pqtt']:
            # c needs to be bigger
            a = c + 1
        elif monkeys['vpmn'] > monkeys['pqtt']:
            b = c - 1
        else:
            return c



if __name__ == '__main__':
    #part1()
    part2()
