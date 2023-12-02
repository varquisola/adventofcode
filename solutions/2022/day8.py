def parse_input(lines):
    # Convert to grid of ints
    grid = []
    for line in lines:
        grid_row = []
        for char in line:
            # Make char int
            tree = int(char)
            grid_row.append(tree)
        grid.append(grid_row)
    print(grid)
    return grid


def determine_if_visible(grid):

    visible = [[False for i in range(len(grid))] for j in range(len(grid[0]))]

    # Setup edges
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or i == (len(grid) - 1) or j == 0 or j == len(grid[0]) - 1:
                visible[i][j] = True

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            # Check north tree(s)
            print("Checking tree at ", i, j)
            not_visible_north, not_visible_south, not_visible_west, not_visible_east = False, False, False, False

            print("Checking north")
            # Is there any tree bigger than current in x direction?
            for k in range(0, i):
                if grid[k][j] >= grid[i][j]:
                    print("Is not visible from north")
                    not_visible_north = True
                    break

            print("Checking south")
            for k in range(i+1, len(grid)):
                if grid[k][j] >= grid[i][j]:
                    print("Is not visible from south")
                    not_visible_south = True
                    break

            print("Checking west")
            for k in range(0, j):
                if grid[i][k] >= grid[i][j]:
                    print("Is not visible from west")
                    not_visible_west = True
                    break

            print("Checking east")
            for k in range(j+1, len(grid[0])):
                if grid[i][k] >= grid[i][j]:
                    print("Is not visible from east")
                    not_visible_east = True
                    break

            if not_visible_north and not_visible_south and not_visible_west and not_visible_east:
                visible[i][j] = False
            else:
                visible[i][j] = True

    count = count_trues(visible)
    print(count)
    return visible


def count_trues(visible):
    count = 0
    for i in range(len(visible)):
        for j in range(len(visible[0])):
            if visible[i][j]:
                count += 1
    return count


def obtain_max_scenic_score(grid):
    max_score = 0
    best_tree_x = -1
    best_tree_y = -1
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            print("Checking ", i, j)
            count_north, count_south, count_west, count_east = 0, 0, 0, 0
            print("Checking north")
            for k in range(i-1, -1, -1):
                print("K", k)
                print(grid[k][j])
                if grid[k][j] >= grid[i][j]:
                    print("Is not visible from north")
                    count_north += 1
                    break
                else:
                    print("Good tree north")
                    count_north += 1

            print("Checking south")
            for k in range(i+1, len(grid)):
                if grid[k][j] >= grid[i][j]:
                    print("Is not visible from south")
                    count_south += 1
                    break
                else:
                    print("Good tree south")
                    count_south += 1

            print("Checking west")
            for k in range(j-1, -1, -1):
                if grid[i][k] >= grid[i][j]:
                    print("Is not visible from west")
                    count_west += 1
                    break
                else:
                    print("Good tree west")
                    count_west += 1

            print("Checking east")
            for k in range(j+1, len(grid[0])):
                if grid[i][k] >= grid[i][j]:
                    print("Is not visible from east")
                    count_east += 1
                    break
                else:
                    print("Good tree east")
                    count_east += 1

            score = count_north * count_south * count_west * count_east

            if score > max_score:
                best_tree_x, best_tree_y = i, j
                max_score = score

    print(best_tree_x, best_tree_y)
    print("Max_score:", max_score)
    return max_score
