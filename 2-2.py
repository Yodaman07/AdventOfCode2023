# Passed !
from two_one import Game

colors = ['red', 'green', 'blue']
with open("inputs/2") as f:
    total = 0
    possible = True
    lines = f.readlines()
    for line in lines:
        low = 1
        lowest = [0, 0, 0]
        game = Game(line)

        for c, i in enumerate(colors):
            if lowest[c] == 0:
                for r in game.roundData:
                    if int(r[i]) > 0:
                        lowest[c] = int(r[i])
                        break

            for r in game.roundData:
                if int(r[i]) > lowest[c] and int(r[i]) != 0:
                    lowest[c] = int(r[i])
        for num in lowest:
            low *= num

        total += low
    # prints result from last file as well for some reason
    print(total)
