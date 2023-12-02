import re
acceptedVals = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
num1 = ""
num2 = ""
with open("inputs/1") as f:
    for i in f.readlines():
        indexes = []
        for c, spelledNum in enumerate(acceptedVals):
            matches = re.finditer(spelledNum, i)
            # https://www.google.com/search?q=find+the+index+of+all+findall+results+regex+python&oq=find+the+index+of+all+findall+results+regex+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQIRgWGB0YHtIBCTMzMDMzajBqOagCALACAA&sourceid=chrome&ie=UTF-8
            # finditr help from google ai
            for match in matches:
                pos = match.start()
                indexes.append({"index": pos+1, "num": acceptedVals.index(spelledNum)+1})

        for count, char in enumerate(i):
            if char.isdigit():
                indexes.append({"index": count+1, "num": int(char)})
        indexes.sort(key=lambda x: x["index"])
        print(indexes)

        num1 = indexes[0]["num"]
        num2 = indexes[-1]["num"]
        total += (int(str(num1) + str(num2)))
print(total)