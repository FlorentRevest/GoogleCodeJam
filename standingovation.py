#!/usr/bin/python3

testsNb = int(input()) # Get input
for test in range(1,testsNb+1):
    infos = [n for n in input().split()]
    sMax = int(infos[0])
    shynessAudience = list(infos[1])
    friendsToInvite = 0
    stoodAudience = 0
    for i in range(len(shynessAudience)) :
        stoodAudience += int(shynessAudience[i])
        if stoodAudience < i+1 :
            friendsToInvite += i+1 - stoodAudience
            stoodAudience += i+1 - stoodAudience

    print("Case #" + str(test) + ": " + str(friendsToInvite))
