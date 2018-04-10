#!/usr/bin/python3
from math import sqrt,ceil,floor

def palindrome(x):
    x = str(x)
    for i in range(int(len(x)/2)) :
        if x[i] != x[len(x)-i-1]:
            return False
    return True

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    infos = [int(n) for n in input().split()]
    min = infos[0]
    max = infos[1]
    result = 0
    print(ceil(sqrt(min)), floor(sqrt(max))+1)

    for i in range(ceil(sqrt(min)), floor(sqrt(max))+1):
        if palindrome(i**2) and palindrome(i):
            print("-----------------------------------------")
            print(i,i**2)
            result += 1

    print("Case #" + str(test) + ": " + str(result))
