from util import read_input_file


def solve(part):
    lines = read_input_file('../../inputs/2023/day2.txt')
    if part == 1:
        # 12 red, 13 green, 14 blue
        out = 0
        for line in lines:
            strip = line.split(": ")
            gameResults = strip[1].split('; ')
            stillGood = True
            for gameResult in gameResults:
                categories = gameResult.split(', ')
                for category in categories:
                    category = category.split(' ')
                    if category[1] == 'blue':
                        if int(category[0]) > 14:
                            stillGood = False
                    elif category[1] == 'green':
                        if int(category[0]) > 13:
                            stillGood = False
                    elif category[1] == 'red':
                        if int(category[0]) > 12:
                            stillGood = False
            if stillGood:
                out += int(strip[0].split(' ')[1])
        return out

    if part == 2:
        out = 0
        for line in lines:
            strip = line.split(": ")
            gameResults = strip[1].split('; ')
            redMax = 0
            greenMax = 0
            blueMax = 0
            for gameResult in gameResults:
                categories = gameResult.split(', ')
                for category in categories:
                    category = category.split(' ')
                    if category[1] == 'blue':
                        if int(category[0]) > blueMax:
                            blueMax = int(category[0])
                    elif category[1] == 'green':
                        if int(category[0]) > greenMax:
                            greenMax = int(category[0])
                    elif category[1] == 'red':
                        if int(category[0]) > redMax:
                            redMax = int(category[0])

            out += (redMax * greenMax * blueMax)
        return out


if __name__ == '__main__':
    print(solve(2))
