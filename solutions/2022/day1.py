def read_input_file(file_name):
    with open(file_name) as f:
        lines = f.read()
    lines = lines.split('\n\n')
    elf_cals = []
    for elf_str in lines:
        elf_cals.append(elf_str.split('\n'))
    return elf_cals


def find_max_elf(elf_cals):
    max_ind = 0
    max_sum = 0
    second_max_ind = 0
    second_max_sum = 0
    third_max_ind = 0
    third_max_sum = 0
    for i, elf_cal in enumerate(elf_cals):
        # First convert to ints
        current_candidate = []
        for elem in elf_cal:
            current_candidate.append(int(elem))

        candidate_sum = sum(current_candidate)

        if candidate_sum > max_sum:
            prev_ind = max_ind
            prev_sum = max_sum
            max_ind = i
            max_sum = candidate_sum

            prev_second_ind = second_max_ind
            prev_second_sum = second_max_sum
            second_max_ind = prev_ind
            second_max_sum = prev_sum

            third_max_ind = prev_second_ind
            third_max_sum = prev_second_sum

        elif candidate_sum > second_max_sum:
            prev_second_ind = second_max_ind
            prev_second_sum = second_max_sum
            second_max_ind = i
            second_max_sum = candidate_sum

            third_max_ind = prev_second_ind
            third_max_sum = prev_second_sum

        elif candidate_sum > third_max_sum:
            third_max_ind = i
            third_max_sum = candidate_sum

    return max_ind, max_sum, second_max_ind, second_max_sum, third_max_ind, third_max_sum


def check_elf_with_most_cals():
    elf_cals = read_input_file('inputs/day1.txt')
    print(find_max_elf(elf_cals))
    max_ind, max_sum, second_max_ind, second_max_sum, third_max_ind, third_max_sum = find_max_elf(elf_cals)
    print(max_sum + second_max_sum + third_max_sum)
