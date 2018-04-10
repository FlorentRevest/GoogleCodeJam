#!/usr/bin/python3

def isEmpty(lst):
    for i in lst:
        if i != 0:
            return False
    return True

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    partiesNb = int(input())
    members = [int(n) for n in input().split()]
    outcome = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    while not isEmpty(members):
        maximum = max(members)

        if members.count(maximum)%2==0:
            firstIndex = members.index(maximum)
            secondIndex = (members[firstIndex+1:]).index(maximum)+firstIndex+1
            outcome.append("".join([letters[firstIndex], letters[secondIndex]]))
            members[firstIndex] -= 1
            members[secondIndex] -= 1
        else:
            firstIndex = members.index(maximum)
            outcome.append(letters[firstIndex]);
            members[firstIndex] -= 1

    print("Case #" + str(test) + ": " + " ".join(outcome))
