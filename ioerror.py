#!/usr/bin/python3

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    bytesNumber = int(input())
    binaryString = input()
    finalString = ""

    for chrNumber in range(bytesNumber):
        beginByte = (chrNumber)*8
        number = 0
        for bit in range(8):
            if binaryString[beginByte + bit] == 'I':
                number += 2**(7-bit)

        finalString += chr(number)

    print("Case #" + str(test) + ": " + finalString)
