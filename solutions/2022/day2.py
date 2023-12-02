def parse_rps_strings_part_one(rps_list):
    # A = rock, B = paper, C = scissors
    # X = rock (1), Y = paper (2), Z = scissors (3)
    # Loss = 0, Draw = 3, Win = 6
    total_score = 0
    for elem in rps_list:
        opponent_pick = elem[0]
        my_pick = elem[2]

        if my_pick == 'X':
            total_score += 1

            if opponent_pick == 'A':
                total_score += 3
            elif opponent_pick == 'C':
                total_score += 6

        elif my_pick == 'Y':
            total_score += 2

            if opponent_pick == 'B':
                total_score += 3
            elif opponent_pick == 'A':
                total_score += 6

        elif my_pick == 'Z':
            total_score += 3

            if opponent_pick == 'C':
                total_score += 3
            elif opponent_pick == 'B':
                total_score += 6

    return total_score


def parse_rps_strings_part_two(rps_list):
    # A = rock, B = paper, C = scissors
    # X = lose, Y = draw, Z = win
    # Loss = 0, Draw = 3, Win = 6
    total_score = 0
    for elem in rps_list:
        opponent_pick = elem[0]
        desired_result = elem[2]

        if opponent_pick == 'A':
            if desired_result == 'X':
                total_score += 3
            elif desired_result == 'Y':
                total_score += 4
            elif desired_result == 'Z':
                total_score += 8

        elif opponent_pick == 'B':
            if desired_result == 'X':
                total_score += 1
            elif desired_result == 'Y':
                total_score += 5
            elif desired_result == 'Z':
                total_score += 9

        elif opponent_pick == 'C':
            if desired_result == 'X':
                total_score += 2
            elif desired_result == 'Y':
                total_score += 6
            elif desired_result == 'Z':
                total_score += 7

    return total_score
