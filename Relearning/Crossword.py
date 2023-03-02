import copy
rows = 15
columns = 15

z = [['i', 's', 'i', 'g', 'n', 'a', 'd', 'e', 's', 't', 'n', 'e', 'd', 'r', 'a'],
     ['b', 'e', 'p', 'l', 'a', 'i', 'd', 'r', 'a', 'w', 'n', 'i', 'c', 't', 'c'],
     ['a', 'i', 'l', 'o', 't', 's', 'k', 's', 'a', 'x', 'o', 'h', 'h', 'n', 'l'],
     ['n', 'd', 'm', 'w', 'e', 'c', 'l', 'l', 'g', 'v', 'i', 'l', 'f', 'o', 'o'],
     ['c', 'a', 'o', 'e', 'f', 't', 'a', 'a', 'e', 'n', 'e', 's', 'l', 'r', 'a'],
     ['h', 'l', 'a', 'd', 'e', 'n', 's', 'n', 'd', 't', 'i', 'r', 'e', 'i', 'k'],
     ['f', 'f', 'u', 'p', 'o', 't', 'p', 'd', 'e', 'e', 'u', 's', 's', 'n', 'w'],
     ['d', 'l', 'e', 'h', 'i', 'g', 'n', 'i', 'r', 'i', 'p', 's', 'a', 'w', 'a'],
     ['e', 'm', 'o', 'r', 'd', 'c', 'n', 's', 'l', 'i', 'u', 't', 'e', 'o', 'h'],
     ['k', 'r', 's', 'n', 'u', 's', 'm', 'c', 't', 'e', 's', 'u', 'r', 'r', 'a'],
     ['s', 'n', 'o', 'i', 't', 'a', 'c', 'i', 'n', 'u', 'm', 'm', 'o', 'c', 's'],
     ['a', 'o', 'u', 'a', 's', 'l', 'w', 'a', 'd', 'e', 'c', 'b', 'n', 'y', 's'],
     ['m', 'i', 'l', 'h', 's', 'u', 'r', 'o', 't', 'f', 'o', 'l', 'o', 'r', 'e'],
     ['s', 'l', 'a', 'c', 'k', 't', 'x', 'a', 'r', 't', 'r', 'e', 'd', 'i', 't'],
     ['a', 's', 'u', 'i', 't', 'e', 'h', 't', 'e', 'b', 'e', 's', 's', 'a', 'y']]

remaining = copy.deepcopy(z)

wordlist = ["aged", "airy", "ardent", "asked", "asks", "aspiring", "asset", "athlete", "axis",
            "ban", "brow",
            "cdrom", "chain", "chin", "cloak", "communications", "core", "crow", "cuts",
            "disc", "donor", "dust",
            "earl", "edit", "enact", "essay", "exodus",
            "feta", "flow",
            "glowed", "hate", "hawk", "held", "hind",
            "install", "inward", "iron", "issue",
            "laden", "ladies", "laid", "lawn", "lion", "loft", "lots",
            "meet", "moon",
            "once",
            "pedal", "pile", "poet", "puff",
            "roast", "robot", "rush",
            "salute", "sedan", "self", "sign", "sings", "slack", "smash", "soul", "spit", "stirs", "studio", "stumbles", "suite",
            "tank", "tire",
            "users",
            "void",
            "wade", "willow", "wolf"]
# Asks is backwards at row 2, column 8
# Athlete is Down left at row 0, column 14
# chin is Down left at row 1, column 11
# communications is backwards at row 10, column 13
# cuts is up left at row 11, column 10
# edit is forwards at row 11, column 11
wordstore = ""
found = True
for word in wordlist:
    found = False
    wordstore = ''
    print("Testing word: " + word)
    for row in range(rows):
        for column in range(columns):
            # If a word is spelled in the forward direction
            if columns - column >= len(word):
                for x in range(len(word)):
                    wordstore = wordstore + z[row][column+x]
                if wordstore == word:
                    found = True
                    print("Found Forwards at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row][column+x] = ''
                wordstore = ''
            # If a word is spelled in the backwards direction
            if column >= len(word) - 1:
                for x in range(len(word)):
                    wordstore = wordstore + z[row][column-x]
                if wordstore == word:
                    found = True
                    print("Found Backwards at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row][column-x] = ''
                wordstore = ''
            # If a word is spelled vertically downwards
            if rows - row >= len(word):
                for x in range(len(word)):
                    wordstore = wordstore + z[row+x][column]
                if wordstore == word:
                    found = True
                    print("Found Downwards at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row+x][column] = ''
                wordstore = ''
            # If a word is spelled vertically upwards
            if row >= len(word) - 1:
                for x in range(len(word)):
                    wordstore = wordstore + z[row-x][column]
                if wordstore == word:
                    found = True
                    print("Found upwards at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row-x][column] = ''
                wordstore = ''
            # If a word is spelled diagonally down right
            if rows - row >= len(word) and columns - column >= len(word):
                for x in range(len(word)):
                    wordstore = wordstore + z[row+x][column+x]
                if wordstore == word:
                    found = True
                    print("Found down right at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row+x][column+x] = ''
                wordstore = ''
            # if a word is spelled diagonally down left
            if rows - row >= len(word) and column >= len(word)-1:
                for x in range(len(word)):
                    wordstore = wordstore + z[row+x][column-x]
                if wordstore == word:
                    found = True
                    print("Found down left at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row+x][column-x] = ''
                wordstore = ''
            # if a word is spelled diagonally up right
            if row >= len(word) - 1 and columns - column >= len(word):
                for x in range(len(word)):
                    wordstore = wordstore + z[row-x][column+x]
                if wordstore == word:
                    found = True
                    print("Found up right at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row-x][column+x] = ''
                wordstore = ''
            # if a word is spelled diagonally up left
            if row >= len(word) - 1 and column >= len(word) - 1:
                for x in range(len(word)):
                    wordstore = wordstore + z[row-x][column-x]
                if wordstore == word:
                    found = True
                    print("Found up left at row:" + str(row+1) + " Column:" + str(column+1))
                    for x in range(len(word)):
                        remaining[row-x][column-x] = ''
                wordstore = ''
    if found == False:
        print("could not find word: " + word)

print("The remaining letters are:")
for x in range(rows):
    for y in range(columns):
        if remaining[x][y] != '':
            print(remaining[x][y] + " at row:" + str(x+1) + " and column: " + str(y+1))
