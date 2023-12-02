import numpy as np

def parse_directions_part_1(lines):
    tail_positions = set()
    head_position = (0, 0)
    tail_position = (0, 0)
    tail_positions.add(tail_position)

    # U, D, L, R
    directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    possible_touching_configs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    for line in lines:
        cmd = line.split(' ')
        direction, num = cmd[0], int(cmd[1])
        for i in range(num):
            head_position = add_tuple(head_position, directions[direction])

            # Calculate tail_position
            # Determine if tail moves:
            if subtract_tuple(head_position, tail_position) not in possible_touching_configs:
                # The tail moves in same direction of head
                if tail_position[0] == head_position[0] or tail_position[1] == head_position[1]:
                    tail_position = add_tuple(tail_position, directions[direction])
                else:
                    # Head and tail are in different columns or rows
                    if direction == 'U':
                        tail_position = (head_position[0], tail_position[1] + 1)
                    elif direction == 'D':
                        tail_position = (head_position[0], tail_position[1] - 1)
                    elif direction == 'L':
                        tail_position = (tail_position[0] - 1, head_position[1])
                    elif direction == 'R':
                        tail_position = (tail_position[0] + 1, head_position[1])
                tail_positions.add(tail_position)
    print(tail_positions)
    return len(tail_positions)


def parse_directions_part_2(lines):
    tail_positions = set()
    positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    tail_positions.add(positions[len(positions) - 1])

    # U, D, L, R
    directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    possible_touching_configs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    for line in lines:
        cmd = line.split(' ')
        direction, num = cmd[0], int(cmd[1])
        for i in range(num):
            prev_tail_position = tuple(positions[0])
            positions[0] = add_tuple(positions[0], directions[direction])
            for j in range(1, len(positions) - 1):
                # Calculate intermediate node positions and tail position
                # Determine if tail moves:
                next_prev_tail_position = tuple(positions[j])
                positions[j] = update_tail(positions[j - 1], positions[j], prev_tail_position)

                prev_tail_position = next_prev_tail_position
                #

                # Tail_num is last in range:
                if i == len(positions) - 2:
                    tail_positions.add(tuple(positions[len(positions) - 1]))
                tail_positions.add(positions[len(positions) - 1])
    print(tail_positions)
    return len(tail_positions)


def add_tuple(tuple1, tuple2):
    sum_tuple = tuple(map(lambda i, j: i + j, tuple1, tuple2))
    return sum_tuple


def subtract_tuple(tuple1, tuple2):
    diff_tuple = tuple(map(lambda i, j: i - j, tuple1, tuple2))
    return diff_tuple


def update_tail(cur_head_position, cur_tail_position, prev_head_position):
    delta_head = [cur_head_position[0] - prev_head_position[0], cur_head_position[1] - prev_head_position[1]]

    # if the distance between tail and head is greater than 1 in any direction
    if abs(cur_head_position[0] - cur_tail_position[0]) > 1 or abs(
            cur_head_position[1] - cur_tail_position[1]) > 1:

        # if they were touching before
        if (prev_head_position[0] == cur_tail_position[0]) or (prev_head_position[1] == cur_tail_position[1]):
            return [cur_tail_position[0] + delta_head[0], cur_tail_position[1] + delta_head[1]]  # move by delta of head

        # if they weren't touching before
        else:
            diff = [cur_head_position[0] - cur_tail_position[0], cur_head_position[1] - cur_tail_position[1]]

            return [cur_tail_position[0] + (np.sign(diff[0]) * min(abs(diff[0]), 1)),
                    cur_tail_position[1] + (np.sign(diff[1]) * min(abs(diff[1]), 1))]

    # if head didn't move away enough
    else:
        return list(cur_tail_position)