#!/usr/bin/python3
testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    coordNb=input()
    coord1=[int(n) for n in input().split()]
    coord2=[int(n) for n in input().split()]
    coord1.sort()
    coord2.sort(reverse=True)
    scalarProduct = 0
    for i in range(len(coord1)):
        scalarProduct += coord1[i]*coord2[i]
    print("Case #" + str(test) + ": " + str(scalarProduct))
