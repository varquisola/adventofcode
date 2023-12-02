def detect_four_different_chars(input_string):
    l = 0
    curr = ""
    for r in range(len(input_string)):
        while input_string[r] in curr:
            curr = curr[1:]
            l += 1
        curr = curr + input_string[r]

        if len(curr) == 14:
            print(curr)
            return r + 1

    return -1
