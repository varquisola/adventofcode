def calculate_signal_strength(lines):
    X = 1
    cycle = 0
    checkpoints = [20, 60, 100, 140, 180, 220]
    outcomes = [1 for i in range(999)]
    outcomes[cycle] = 1

    for i, line in enumerate(lines):
        cmd = line.split(' ')
        if cmd[0] == 'addx':
            for j in range(2):
                outcomes[j] = outcomes[j - 1]
                cycle += 1
            X += int(cmd[1])
            outcomes[cycle] = X
        else:
            # cmd is noop
            cycle += 1
            outcomes[cycle] = outcomes[cycle - 1]

    sum_strengths = 0
    for i in range(len(outcomes)):
        if i in checkpoints:
            sum_strengths += (outcomes[i] * i)
    print(sum_strengths)

    return outcomes


def calculate_crt_pic(lines):
    X = 1
    cycle = 1

    num_cycles = 0
    for line in lines:
        cmd = line.split(' ')
        if cmd[0] == 'addx':
            num_cycles += 2
        else:
            num_cycles += 1

    drawing = ['.' for i in range(num_cycles)]
    x_locations = [1 for i in range(num_cycles + 3)]
    x_locations[0] = 1

    for i, line in enumerate(lines):
        cmd = line.split(' ')
        if cmd[0] == 'addx':
            for j in range(cycle + 1, cycle + 3):
                x_locations[j] = x_locations[j - 1]
            cycle += 2
            X += int(cmd[1])
            x_locations[cycle] = X
        else:
            # cmd is noop
            cycle += 1
            x_locations[cycle] = x_locations[cycle - 1]

    x_locations = x_locations[1:241]
    for i in range(len(x_locations)):
        if i % 40 == 0: print('')
        if x_locations[i] - 1 == i % 40 or x_locations[i] == i % 40 or x_locations[i] + 1 == i % 40:
            print('#', end='')
        else:
            print('.', end='')

    return drawing