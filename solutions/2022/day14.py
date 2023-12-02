from util import read_input_file


def draw_rocks(lines, part):
    blockage_coords = []
    for line in lines:
        blockage = line.split(' -> ')
        current_blockage = []
        for coord in blockage:
            x, y = coord.split(',')
            current_blockage.append((int(x), int(y)))
        blockage_coords.append(current_blockage)

    res = []
    for i in blockage_coords:
        res.extend(i)

    buffer = 500
    min_col = min(res, key=lambda tup: tup[0])[0] - 1
    max_col = max(res, key=lambda tup: tup[0])[0] + 1

    if part == 'part1':
        max_row = max(res, key=lambda tup: tup[1])[1]
    else:
        max_row = max(res, key=lambda tup: tup[1])[1] + 2

    # Add column on either side
    grid = [['.' for _ in range(0, max_col + 2 - min_col + buffer)] for _ in range(max_row + 1)]
    if part == 'part2':
        for i in range(max_col - min_col + 2 + buffer):
            grid[max_row][i] = '#'

    print_grid(grid)
    sand_coord = (0, 500 - min_col)
    grid[0][500 - min_col] = '+'

    for blockage in blockage_coords:
        for i in range(len(blockage) - 1):
            row_change = False
            col_change = False
            if blockage[i][0] == blockage[i+1][0]:
                row_change = True
                col_constant = blockage[i][0] - min_col
                draw_range = range(min(blockage[i][1], blockage[i + 1][1]), max(blockage[i + 1][1], blockage[i][1]) + 1)
            elif blockage[i][1] == blockage[i+1][1]:
                col_change = True
                row_constant = blockage[i][1]
                draw_range = range(min(blockage[i][0], blockage[i + 1][0]) - min_col, max(blockage[i + 1][0], blockage[i][0]) + 1 - min_col)

            for k in draw_range:
                if col_change:
                    grid[row_constant][k] = '#'
                elif row_change:
                    grid[k][col_constant] = '#'

    return grid, sand_coord


def calculate_falling_sand(grid, start_coords, part):
    count = 0
    while True:
        count += 1
        sand = [start_coords[0], start_coords[1]]
        if sand_behavior(grid, sand, start_coords, part) == 'X':
            return count


def sand_behavior(grid, sand, start_coords, part):
    print("Sand at: ", sand)
    if part == 'part1' and grid[sand[0]][sand[1]] == '.' and sand[0] + 1 == len(grid):
        grid[sand[0]][sand[1]] = 'X'
        return 'X'
    elif sand[0] == start_coords[0] and sand[1] == start_coords[1] and \
            grid[sand[0] + 1][sand[1]] == 'O' and \
            grid[sand[0] + 1][sand[1] - 1] == 'O' and \
            grid[sand[0] + 1][sand[1] + 1] == 'O':
        return 'X'
    elif grid[sand[0] + 1][sand[1]] == '.':
        sand[0] += 1
        return sand_behavior(grid, sand, start_coords, part)
    elif grid[sand[0] + 1][sand[1]] == 'O' or grid[sand[0] + 1][sand[1]] == '#':
        # Check left of grain of sand
        if grid[sand[0] + 1][sand[1] - 1] == '.':
            sand[0] += 1
            sand[1] -= 1
            return sand_behavior(grid, sand, start_coords, part)
        elif (grid[sand[0] + 1][sand[1] - 1] == 'O' or grid[sand[0] + 1][sand[1] - 1] == '#') and \
                grid[sand[0] + 1][sand[1] + 1] == '.':
            sand[0] += 1
            sand[1] += 1
            return sand_behavior(grid, sand, start_coords, part)
        elif (grid[sand[0] + 1][sand[1] - 1] == 'O' or grid[sand[0] + 1][sand[1] - 1] == '#') and \
                (grid[sand[0] + 1][sand[1] + 1] == 'O' or grid[sand[0] + 1][sand[1] + 1] == '#'):
            grid[sand[0]][sand[1]] = 'O'
            return 'O'


def print_grid(grid):
    for row in grid:
        print(*row, sep='')


def solve(part='part2'):
    lines = read_input_file('inputs/day14.txt')
    grid, start_coord = draw_rocks(lines, part)
    res = calculate_falling_sand(grid, start_coord, part)
    print(res)
    print_grid(grid)

