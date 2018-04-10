#!/usr/bin/python3

def open(chestToOpen, availableKeys, openChests, chests):
    availableKeys.remove((chests[chestToOpen])[0])
    openChests.append(chestToOpen)
    print(openChests)
    if len(openChests) == len(chests):
        return True

    availableKeys += chests[chestToOpen][1]

    for key in list(set(availableKeys)):
        for chestNb in range(len(chests)):
            if chests[chestNb][0] == key and not (chestNb in openChests):
                if(open(chestNb, availableKeys, openChests, chests)): return True

    # Unstack
    availableKeys.append(chests[chestToOpen][0])
    openChests.remove(chestToOpen)
    return False

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    infos = [int(n) for n in input().split()]
    chests = [(0, []) for n in range(infos[1])] # chests[i] gives a tuple with (the type of key needed to open, [the keys inside])
    openChests = []
    availableKeys = [int(n) for n in input().split()] # list of types of keys available atm
    found = False

    for i in range(len(chests)):
        chestInfos = [int(n) for n in input().split()]
        chests[i] = (chestInfos[0], [] if chestInfos[1] == 0 else chestInfos[2::])

    for key in list(set(availableKeys)):
        for chestNb in range(len(chests)):
            if chests[chestNb][0] == key and not found:
                found = open(chestNb, availableKeys, openChests, chests)

    if found:
        print("Case #" + str(test) + ": " + ' '.join([str(n+1) for n in openChests]))
    else:
        print("Case #" + str(test) + ": IMPOSSIBLE")
