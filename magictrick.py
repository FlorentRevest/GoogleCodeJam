#!/usr/bin/python3

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):

    chosenNbRow1 = int(input())
    for i in range(1,5) :
        row1 = [int(n) for n in input().split()]
        if i == chosenNbRow1 :
            chosenRow1 = row1
            #print (chosenRow1)

    chosenNbRow2 = int(input())
    for j in range(1,5) :
        row2 = [int(m) for m in input().split()]
        if j == chosenNbRow2 :
            chosenRow2 = row2
            #print (chosenRow2)

    matchingElems = []
    for elem in chosenRow1:
        if elem in chosenRow2:
            matchingElems.append(elem)
    #print(matchingElems)

    if len(matchingElems) > 1:
        print("Case #" + str(test) + ": Bad magician!")
    elif len(matchingElems) == 1:
        print("Case #" + str(test) + ": " + str(matchingElems[0]))
    elif len(matchingElems) == 0:
        print("Case #" + str(test) + ": Volunteer cheated!")
