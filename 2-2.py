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
        #https: // www.google.com / search?q = multiply + all + numbers + in +list + python & oq = multiply + all + numbers + in +list + & gs_lcrp = EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIICAIQABgWGB4yCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhge0gEIODc0M2owajGoAgCwAgA & sourceid = chrome & ie = UTF - 8
        # google ai help

        total += low
    # prints result from last file as well for some reason
    print(total)
