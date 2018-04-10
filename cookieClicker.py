#!/usr/bin/python3

#def timeTaken(farmPrice, farmExtraCookies, winNumber, farmsNumber):

testNb = int(input())
for test in range (1, testNb+1) :
    info = [float(n) for n in input().split()]
    farmPrice = info[0]        # C
    farmExtraCookies = info[1] # F
    winNumber = info[2]        # X


    spentCookie = 0.0
    cookiePerSeconds = 2.0
    while winNumber /  :
        spentCookie += farmPrice / cookiePerSeconds
        cookiePerSeconds += farmExtraCookies

    time = (winNumber / cookiePerSeconds) + spentCookie

    # For each number of farms we can make, find the minimal
    # time taken to have the desired cookies number.
    #farmsNumber = 96000
    #time = timeTaken(farmPrice, farmExtraCookies, winNumber, 0)
    #previousTime = time+1 # just to get started in the loop
    
    #while time <= previousTime:
     #   previousTime = time
      #  time = timeTaken(farmPrice, farmExtraCookies, winNumber, farmsNumber)
       # farmsNumber += 1
       # print (time)

    #time = previousTime
    print("Case #" + str(test) + ": " + str(round(time, 7)))
