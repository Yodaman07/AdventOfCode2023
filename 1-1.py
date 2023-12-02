# Passed!
with open("inputs/1") as f:
    total = 0
    num1 = ""
    num2 = ""
    for i in f.readlines():
        for char in i:
            if char.isdigit():
                num1 = str(char)
                break
        for char in reversed(i):
            if char.isdigit():
                num2 = str(char)
                break
        total += (int(num1 + num2))

print(total)