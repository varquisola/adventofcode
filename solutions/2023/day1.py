from util import read_input_file


def solve(part):
    lines = read_input_file('../../inputs/2023/day1.txt')
    if part == 1:
        nums = []
        for line in lines:
            a = 0
            b = len(line) - 1
            while ord(line[a]) not in range(48, 58) and a < b:
                a += 1
            while ord(line[b]) not in range(48, 58) and b > a:
                b -= 1
            nums.append(line[a] + line[b])

        sumnum = 0
        for num in nums:
            sumnum += int(num)
        print(sumnum)

    if part == 2:
        nums = []
        wordDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for line in lines:
            theNum = ""
            # Find the digit indices
            a = 0
            b = len(line) - 1
            while ord(line[a]) not in range(48, 58) and a < b:
                a += 1
            while ord(line[b]) not in range(48, 58) and b > a:
                b -= 1

            # Find the word subsets
            lowWordDigit = ""
            highWordDigit = ""
            for wordDigit in wordDigits:
                lowWord = line.find(wordDigit)
                if lowWord != -1 and lowWord < a:
                    a = lowWord
                    lowWordDigit = wordDigit

            for wordDigit in wordDigits:
                highWord = line.rfind(wordDigit)
                if highWord != -1 and highWord > b:
                    b = highWord
                    highWordDigit = wordDigit

            if len(lowWordDigit) > 0:
                theNum += str(wordDigits.index(lowWordDigit) + 1)
            else:
                theNum += line[a]

            if len(highWordDigit) > 0:
                theNum += str(wordDigits.index(highWordDigit) + 1)
            else:
                theNum += line[b]
            nums.append(theNum)
        print(nums)
        sumnum = 0
        for num in nums:
            sumnum += int(num)
        print(sumnum)


if __name__ == '__main__':
    solve(2)