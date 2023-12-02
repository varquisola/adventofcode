def split_in_half(list):
    dups = []
    for elem in list:
        # split in half
        compare_str = elem[0:len(elem) // 2]
        for i in range(len(elem) // 2, len(elem)):
            if elem[i] in compare_str:
                dups.append(elem[i])
                break

    return dups


def sum_chars(list):
    vals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g':7, 'h': 8, 'i':9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
    char_sum = 0
    for elem in list:
        char_sum += vals.get(elem)

    return char_sum


def find_badge_in_group(list):
    badges = []
    for i in range(0, len(list), 3):
        magic_elem = set(list[i]).intersection(set(list[i + 1])).intersection(set(list[i + 2]))
        print(magic_elem)
        badges.append(min(magic_elem))
    return sum_chars(badges)
