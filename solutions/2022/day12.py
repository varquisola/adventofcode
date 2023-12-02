from collections import defaultdict, deque
import heapq as heap

from util import read_input_file


def create_grid(lines):
    grid = []
    for line in lines:
        grid.append(line)
    return grid


def elevations(grid):
    R = len(grid)
    C = len(grid[0])
    # Determine elevations
    E = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                E[r][c] = 1
            elif grid[r][c] == 'E':
                print("End at: ", r, c)
                E[r][c] = 26
            else:
                E[r][c] = ord(grid[r][c]) - ord('a') + 1
    return E


def bfs(grid, part):
    R = len(grid)
    C = len(grid[0])
    Q = deque()
    E = elevations(grid)
    for r in range(R):
        for c in range(C):
            if E[r][c] == 1 and (part == 2 or grid[r][c] == 'S'):
                Q.append(((r, c), 0))
    # determine visited
    S = set()
    while Q:
        print(Q)
        (r,c),d = Q.popleft()
        print(r, c, d)
        if (r,c) in S:
            continue
        S.add((r,c))
        if grid[r][c] == 'E':
            return d
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and E[rr][cc] <= 1 + E[r][c]:
                Q.append(((rr, cc), d+1))


def solve():
    lines = read_input_file('inputs/testcase.txt')
    grid = create_grid(lines)
    # d = bfs(grid, 1)
    e = bfs(grid, 2)
    # print(d)
    print(e)