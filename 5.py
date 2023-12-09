# Passed (Both)!
import re


class Conversions:
    def __init__(self, params):
        self.params = params

    def getSoil(self, seed):
        soilNum = None
        # Seed num is source while soil num is dest
        seed = int(seed)
        for i in self.params:
            source = i["source_s"]
            range_l = i["range_l"]
            dest = i["dest_s"]
            if (seed >= source) and (seed <= source + range_l - 1):
                soilNum = (seed - source) + dest
        if soilNum is None:
            soilNum = seed
        return soilNum

    def getSeedFromSoil(self, soilNum):
        seedNum = None
        for param in self.params:
            neededLength = soilNum - param["dest_s"]
            if param["range_l"] >= neededLength >= 0:
                seedNum = neededLength + param['source_s']

        if seedNum is None:
            seedNum = soilNum

        return seedNum


class GetData:
    def __init__(self, filePath):
        self.filePath = filePath

    def getAllData(self):
        section = []
        data = []

        pattern = re.compile(r"(\d+)")
        with open(self.filePath) as f:
            allLines = f.readlines()
            allLines.append('\n')
            allLines.append("a")

            # print(allLines)
            for count, line in enumerate(allLines):

                match = pattern.findall(line)
                # print(match, line)
                if count == 0:
                    data.append(match)
                elif match:
                    formated = {"dest_s": int(match[0]), "source_s": int(match[1]), "range_l": int(match[2])}
                    # print(formated)
                    section.append(formated)

                # print(match, allLines[count])
                if not match:
                    # print(section)
                    try:
                        if allLines[count + 1] and section:
                            data.append(section)
                            section = []
                    except IndexError:
                        pass

        return data


def checkIfSeedExists(seedList, possibleSeed):
    for count, seed in enumerate(seedList):
        if count % 2 == 0:
            if int(seed) <= int(possibleSeed) <= int(seed) + int(seedList[count + 1]) - 1:
                return {"result": True, "value": possibleSeed}
    return {"result": False}


# 5 - 1
# data = GetData("inputs/5")
# allData = data.getAllData()
# # print(allData)
#
# seeds = allData[0]
# allData.pop(0)
#
# a = []
# for seedIndex, seedNum in enumerate(seeds):
#     a.append([seedNum])
#     for paramCount, parameter in enumerate(allData):
#         c = Conversions(parameter)
#         index = a[seedIndex][paramCount]
#         a[seedIndex].append(c.getSoil(index))
#
#
# lowest = []
# for i in a:
#     lowest.append(i[-1])
#
# currentLowest = None
# lowest.sort()
# print(lowest[0])


# 5 - 2 (I actually don't know if it worked or I got stupidly lucky. Also its very inefficent)
# run map backwards <-- idea from advent of code subreddit
data = GetData("inputs/5")
allData = data.getAllData()

seeds = allData[0]
allData.pop(0)
allData.reverse()
# print(allData)
i = 0
startingNum = 0
possibleSeed = 0
while True:
    print(startingNum)
    for paramCount, parameters in enumerate(allData):
        if paramCount == 0:
            i = startingNum
        c = Conversions(parameters)
        possibleSeed = c.getSeedFromSoil(i)
        i = possibleSeed

    res = checkIfSeedExists(seeds, possibleSeed)
    if res["result"]:
        # print(res['value'])
        print("FOUND")
        break
    else:
        startingNum += 1
