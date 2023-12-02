import re


def check_in_range(section_list):
    count = 0
    for pairs in section_list:
        test = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", pairs)

        # 46-79,6-78 2 > 0, 3 < 1
        if int(test.groups()[0]) <= int(test.groups()[2]) and int(test.groups()[1]) >= int(test.groups()[3]) or \
                int(test.groups()[2]) <= int(test.groups()[0]) and int(test.groups()[3]) >= int(test.groups()[1]):
            count += 1
    return count


def check_overlap(section_list):
    count = 0
    for pairs in section_list:
        test = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", pairs)

        # 5-20, 16-19 | 16-19, 5-20 | 5-7, 6-9 | 6-9, 5-7 | 2-6, 4-8 | 4-8, 2-6 |
        if (int(test.groups()[0]) <= int(test.groups()[2]) and int(test.groups()[1]) >= int(test.groups()[3])) or \
                int(test.groups()[2]) <= int(test.groups()[0]) and int(test.groups()[3]) >= int(test.groups()[1]) or \
                int(test.groups()[0]) <= int(test.groups()[1]) and int(test.groups()[2]) <= int(test.groups()[3]) and int(test.groups()[1]) >= int(test.groups()[2]) and int(test.groups()[0]) <= int(test.groups()[3]) or \
                int(test.groups()[0]) <= int(test.groups()[1]) and int(test.groups()[2]) <= int(test.groups()[3]) and int(test.groups()[0]) <= int(test.groups()[3]) and int(test.groups()[1]) >= int(test.groups()[2]) or \
                int(test.groups()[2]) >= int(test.groups()[0]) and int(test.groups()[3]) >= int(test.groups()[1]) and int(test.groups()[1]) >= int(test.groups()[2]) or \
                int(test.groups()[0]) >= int(test.groups()[2]) and int(test.groups()[1]) >= int(test.groups()[3]) and int(test.groups()[2]) >= int(test.groups()[1]):
            print(pairs)
            count += 1
    return count


def check_set_overlap_completely(section_list):
    count = 0
    for pairs in section_list:
        p = re.compile(r'\d+')
        nums = p.findall(pairs)
        l1, l2, r1, r2 = int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])
        if set(range(l1, l2 + 1)).issubset(range(r1, r2 + 1)) or set(range(r1, r2 + 1)).issubset(range(l1, l2 + 1)):
            print(nums)
            count += 1
    return count

def check_set_overlap_partly(section_list):
    count = 0
    for pairs in section_list:
        p = re.compile(r'\d+')
        nums = p.findall(pairs)
        l1, l2, r1, r2 = int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])
        if len(set(range(l1, l2 + 1)).intersection(range(r1, r2 + 1))) > 0:
            print(nums)
            count += 1
    return count
