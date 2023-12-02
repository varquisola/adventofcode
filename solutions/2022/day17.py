with open('../../inputs/2022/testcase.txt') as f:
    data = f.read().strip()


def get_piece(t, y):
    if t == 0:
        return set([(2, y), (3, y), (4, y), (5, y)])
    elif t == 1:
        return set([(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)])
    elif t == 2:
        return set([(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)])
    elif t == 3:
        return set([(2, y), (2, y + 1), (2, y + 2), (2, y + 3)])
    elif t == 4:
        return set([(2, y), (2, y + 1), (3, y), (3, y + 1)])


def move_left(piece):
    if any([x == 0 for (x, y) in piece]):
        return piece
    return set([(x - 1, y) for (x, y) in piece])


def move_right(piece):
    if any([x == 6 for (x, y) in piece]):
        return piece
    return set([(x + 1, y) for (x, y) in piece])


def move_down(piece):
    return set([(x, y - 1) for (x, y) in piece])


def move_up(piece):
    return set([(x, y + 1) for (x, y) in piece])


def show(R):
    maxY = max([y for (x, y) in R])
    for y in range(maxY, 0, -1):
        row = ''
        for x in range(7):
            if (x, y) in R:
                row += '#'
            else:
                row += '.'
        print(row)
    print()


def solve():
    rock_count = 0
    top = 0
    i = 0
    R = set([(x, 0) for x in range(7)])

    # We only need to care about bottom left corner of blocks.
    # Each rock gets up to 3 downward moves
    # Rocks repeat '-', '+', 'backwards L', 'l', 'square'
    # Column is 7 units long (0-6)
    # Rock starts with left edge at 2

    while rock_count < 10:
        piece = get_piece(rock_count%5, top+4)
        print(rock_count)
        while True:
            if data[i] == '>':
                # Move rock to the right if rock isn't touching right edge already
                piece = move_right(piece)
                print(piece)
                if piece & R:
                    piece = move_left(piece)
                    print(piece)
            else:
                # Move rock to the left if rock isn't touching left edge already
                piece = move_left(piece)
                print(piece)
                if piece & R:
                    piece = move_right(piece)
                    print(piece)
            i = (i + 1) % len(data)
            piece = move_down(piece)
            print("Move down: ", show(R))
            if piece & R:
                piece = move_up(piece)
                print("Move back up: ", show(R))
                R |= piece
                show(R)
                top = max([y for (x, y) in R])
                break
        rock_count += 1
    print("Top: ", top)


if __name__ == '__main__':
    solve()