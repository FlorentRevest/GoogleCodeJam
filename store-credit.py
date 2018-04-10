#!/usr/bin/python3
testsNb = int(input())
for test in range(0, testsNb):
    availableMoney = int(input())
    itemsNb = int(input())
    itemsList = [int(n) for n in input().split()]
    for i in range(len(itemsList)): # For each item of the list
        for j in range(i+1, len(itemsList)): # For each item of the sub-list
            if itemsList[i] + itemsList[j] ==  availableMoney:
                print("Case #" + str(test+1) + ": " + str(i+1) + " " + str(j+1))
                break
        else:
            continue
        break
