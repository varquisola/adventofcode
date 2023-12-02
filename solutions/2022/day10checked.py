def part2checked(lines):
    X = 1
    pixel = [X-1,X,X+1]
    cycle = 0

    cycle_cost = {'addx': 2, 'noop': 1}

    for line in lines:
        instruction = line.split(' ')[0]
        for _ in range(cycle_cost[instruction]):
            # print(cycle, X)
            if cycle % 40 in pixel: print('#', end='')
            else: print('.', end='')
            cycle += 1
            if cycle % 40 == 0: print('')

        if instruction == 'addx':
            X += int(line.split(' ')[1])
            pixel = [X-1,X,X+1]