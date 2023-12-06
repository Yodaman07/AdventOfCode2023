# Passed (Both) !
import re


class Card:
    def __init__(self, line, win_c, mynum_c):
        self.line = line
        self.win_c = win_c
        self.mynum_c = mynum_c
        self.myNumbers = self.findMyNumbers()
        self.winningNumbers = self.findWinningNumbers()

    def findMyNumbers(self):
        pattern = re.compile(r'(\d+)')
        m = pattern.findall(self.line)
        # left are winning numbers and right are your numbers
        return m[self.win_c + 1:]

    def findWinningNumbers(self):
        pattern = re.compile(r'(\d+)')
        m = pattern.findall(self.line)
        return m[1:self.win_c + 1]


# 4-1
with open("inputs/4") as f:
    total = 0
    for line in f.readlines():
        c = Card(line, 10, 25)
        matchingNum = 0
        for winningNum in c.winningNumbers:
            for myNum in c.myNumbers:
                if winningNum == myNum:
                    matchingNum += 1
                    break

        if matchingNum > 0:
            total += 2 ** (matchingNum - 1)

    print(total)

# 4-2 Takes a long time to run by speeds up and almost instantly finishes around the 40th line
with open("inputs/4") as f:
    total = 0
    allLines = f.readlines()
    allAttempts = [1] * len(allLines)

    for count, line in enumerate(allLines):
        c = Card(line, 10, 25)
        # print(count)
        for j in range(allAttempts[count]):
            # print(count, j)
            matches = 0
            for winningNum in c.winningNumbers:
                for myNum in c.myNumbers:
                    if winningNum == myNum:
                        matches += 1
                        break

            # print(count+2, matches+count+2)
            for i in range(count + 2, matches + count + 2):  # update loop
                allAttempts[i-1] += 1
            # print(allAttempts)

            # print("A")

    for num in allAttempts:
        total += num
    print(total)
