import re

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse_input():
    with open('../../inputs/2022/testcase.txt') as f:
        grid = f.read().replace(' ', 'x').splitlines()
        return grid

def find_max_length_row(grid):
    max_row_length = 0
    for row in grid:
        if len(row) > max_row_length:
            max_row_length = len(row)
    return max_row_length

# JUST USE NUMPY
def find_max_length_col(grid):
    grid_t = [zip(line) for line in grid]
    print(grid_t)
    max_col_length = 0
    for row in grid:
        if len(row) > max_row_length:
            max_row_length = len(row)
    return max_row_length


def parse_directions(directions):
    # Number alternate with letter
    p = re.compile(r'\d+')
    q = re.compile(r'[A-Z]')
    nums = p.findall(directions)
    dirs = q.findall(directions)
    return nums, dirs


def move(nums, dirs, grid, start):
    curr_direction = 1
    # Want len(dirs) since it's smaller. Will execute one last nums move at end.
    for i in range(len(dirs)):
        # Num first, then direction
        for j in range(nums[i]):
            if start + directions[curr_direction] == '#':
                break
            # elif start + directions[curr_direction] == '\n':


        if dirs[i] == 'L':
            curr_direction = (curr_direction - 1) % len(directions)
        else:
            curr_direction = (curr_direction + 1) % len(directions)



def solve():
    grid = parse_input()
    print(len(grid))
    print(len(grid[0]))
    # Remove last two lines
    directions = grid[-1]
    nums, dirs = parse_directions(directions)
    grid = grid[:len(grid)-2:]
    show_grid(grid)
    find_max_length_col(grid)

    top_row = grid[0]
    first_dot_coord = 0
    for i in range(len(top_row)):
        if top_row[i] == '.':
            first_dot_coord = i
            break

    start = (0, first_dot_coord)



def show_grid(grid):
    for line in grid:
        print(line, sep="")

if __name__ == '__main__':
    solve()