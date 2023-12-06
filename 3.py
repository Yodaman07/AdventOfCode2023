# Passed (Both) !
def is_symbol(val):
    if not val.isdigit() and (val != ".") and (val != ""):
        return True
    return False


def checkForDigit(pos, line_a, line, line_b):
    l = [
        [
            (line_a[pos - 1].isdigit(), pos - 1), (line_a[pos].isdigit(), pos), (line_a[pos + 1].isdigit(), pos + 1)
        ],

        [
            (line[pos - 1].isdigit(), pos - 1), (line[pos + 1].isdigit(), pos + 1)
        ],

        [
            (line_b[pos - 1].isdigit(), pos - 1), (line_b[pos].isdigit(), pos), (line_b[pos + 1].isdigit(), pos + 1)
        ]
    ]
    return l


def findAllNumbers(list, line_list, part):
    total = []
    trueTotal = 0
    for layerNum, layer in enumerate(list):
        for res in layer:
            if res[0]:  # if its a symbol
                fullNum = findFullNum(line_list[layerNum], res[1])
                if not total:
                    total.append(fullNum)
                    continue

                try:
                    if total[-1] != fullNum:
                        total.append(fullNum)
                except IndexError:
                    pass

    for val in total:
        trueTotal += val

    if part == "a":
        return trueTotal
    elif part == "b":
        return total


def findFullNum(line, pos):
    start_i = 0
    end_i = 0
    index = 1
    while True:
        if line[pos - index].isdigit():
            index += 1
        else:
            start_i = pos - index + 1
            index = 1
            break

    while True:
        if line[pos + index].isdigit():
            index += 1
        else:
            end_i = pos + index
            break
    return int(line[start_i:end_i])


# 3-1
with open("inputs/3") as f:
    total = 0
    allLines = f.readlines()
    for lineNum, line in enumerate(allLines):
        for pos, char in enumerate(line):
            if len(line) - 1 > pos:
                if is_symbol(char):
                    try:
                        list = checkForDigit(pos, allLines[lineNum - 1], line, allLines[lineNum + 1])
                        # print(list)
                        # print(line, char)
                        total += findAllNumbers(list, [allLines[lineNum - 1], line, allLines[lineNum + 1]], "a")
                    except IndexError:
                        pass

    print(total)

# 3-2
with open("inputs/3") as f:
    total = 0
    allLines = f.readlines()
    for lineNum, line in enumerate(allLines):
        for pos, char in enumerate(line):
            if len(line) - 1 > pos:
                if char == "*":
                    try:
                        list = checkForDigit(pos, allLines[lineNum - 1], line, allLines[lineNum + 1])
                        # print(list)
                        # print(line, char)
                        num = findAllNumbers(list, [allLines[lineNum - 1], line, allLines[lineNum + 1]], "b")
                        b = 1
                        if len(num) == 2:
                            for i in num:
                                b *= i
                            total += b
                    except IndexError:
                        pass

    print(total)
