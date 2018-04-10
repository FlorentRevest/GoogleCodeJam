#!/usr/bin/python3

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    result = 0
    words1 = []
    words2 = []

    nb = int(input())
    for i in range(0, nb):
        split = input().split()
        if split[0] in words1 and split[1] in words2:
            result += 1
        else:
            words1.append(split[0])
            words2.append(split[1])

    print("Case #" + str(test) + ": " + str(result))
