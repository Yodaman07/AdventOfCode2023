import re


# Passed!

class Game:
    def __init__(self, line):
        self.line = line
        self.num = int(self.getNum())
        self.rounds = self.getRounds()
        self.roundData = self.getRoundData()

    def getNum(self):
        r = re.compile(r'(\d+):')
        result = r.search(self.line)
        return result.group(1)

    def getRounds(self):
        r = re.compile(r'(:|;)')
        result = r.findall(self.line)
        return len(result)

    def getRoundData(self):
        red = 0
        green = 0
        blue = 0
        final = []
        r = re.compile(r'(;? (\d+) (\w+))')
        result = r.findall(self.line)
        for c, i in enumerate(result):
            if i[2] == 'red':
                red += int(i[1])
            elif i[2] == 'green':
                green += int(i[1])
            elif i[2] == "blue":
                blue += int(i[1])

            if c + 1 < len(result):
                if result[c + 1][0][0] == ';':
                    final.append({'red': red, 'green': green, 'blue': blue})
                    red = 0
                    green = 0
                    blue = 0
            elif len(result) == c + 1:
                final.append({'red': red, 'green': green, 'blue': blue})

        return final


with open("inputs/2") as f:
    total = 0
    possible = True
    lines = f.readlines()
    for line in lines:
        g = Game(line)
        for r in g.roundData:
            if r['red'] > 12 or r['green'] > 13 or r['blue'] > 14:
                possible = False
                break

        if possible:
            total += g.num
        else:
            # reset default
            possible = True
    print(total)
