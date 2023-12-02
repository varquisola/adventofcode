import numpy as np

moves = [el.split() for el in open('../../inputs/2022/day9.txt', 'r').readlines()]


def map_direction_to_vector(direction):
    if direction == "U":
        return [1, 0]
    elif direction == "D":
        return [-1, 0]
    elif direction == "R":
        return [0, 1]
    elif direction == "L":
        return [0, -1]


def update_head(vector, cur_head_position):
    cur_head_position[0] += vector[0]
    cur_head_position[1] += vector[1]
    return cur_head_position


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


def solve(move_list, n_links=2):
    current_positions = [[0, 0] for _ in range(n_links)]
    last_link_history = [(0, 0)]
    for move, i in move_list:
        for move_number in range(int(i)):
            vector = map_direction_to_vector(move)
            # By prev_tail_position, we mean the previous node before our current one
            prev_tail_position = tuple(current_positions[0])
            # current_positions[0] == head
            current_positions[0] = update_head(vector, current_positions[0])
            # n_links = 10 -> range(0, 9) -> 0, 1, 2, 3, 4, 5, 6, 7, 8
            for tail_num in range(n_links - 1):
                # Get a copy of the current node
                # 1, 2, 3, 4, 5, 6, 7, 8, 9
                next_prev_tail_position = tuple(current_positions[tail_num + 1])
                # Update the current node
                current_positions[tail_num + 1] = update_tail(current_positions[tail_num],
                                                              current_positions[tail_num + 1],
                                                              prev_tail_position)
                # Update the previous pointer to the copy
                prev_tail_position = next_prev_tail_position
                #

                # Tail_num is last in range:
                if tail_num == n_links - 2:
                    last_link_history.append(tuple(current_positions[n_links - 1]))
    return len(set(last_link_history))


print(solve(moves, 2))
print(solve(moves, 10))