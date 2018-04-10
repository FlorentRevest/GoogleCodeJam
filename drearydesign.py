#!/usr/bin/python3

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    infos = [int(n) for n in input().split()]
    maxValue = infos[0]
    maxDiff = infos[1]

    # For each red component we define a "block" as the set containing G and B
    # values in the range of the maximumDifference.
    # e.g: for r=0 with maxDiff=1 we study the set of G and B = 0 or 1
    #      for r=1 with maxDiff=1 we study the set of G and B = 0 or 1 or 2
    # The number of bland colors is the sum of the number of bland colors for
    # each red component. And for each red component the number of bland colors
    # that are associated is the length of the "block" define earlier squared.
    numberOfColors = 0
    for r in range(maxValue):
        blockSize = 1+2*maxDiff
        if r < maxDiff:
            blockSize -= maxDiff - r
        if r > maxValue - maxDiff
            blockSize -= # ?????
        numberOfColors += blockSize**2

    print("Case #" + str(test) + ": " + str(numberOfColors))
