#!/usr/bin/python3

def minesField(width, height, minesNumber):
    array = [['.' for x in range(width)] for y in range(height)] # Create map

    if minesNumber == width*height-1:
        for i in range(len(array)):
            for y in range(len(array[i])):
                array[i][y] = '*'
        array[0][0] = 'c'
        return "\n".join([''.join(i) for i in array])
    elif width == 1:  return "\n".join(["c"]+["."]*(height-minesNumber-1)+["*"]*minesNumber)
    elif height == 1: return "*"*minesNumber + "."*(width-(minesNumber+1)) + "c"

    nbFilledWidth = int(minesNumber/width) # Fill complete lines
    for i in range(len(array)):
        if i >= height - nbFilledWidth :
            array[i] = ['*'] * width 

    N = width*height - minesNumber 
    if (N%2==0 and N >= 4) or (N%2==1 and N >= 9 and height >= 3 and width >= 3):
        remainingMines = int(minesNumber%width) # Fill the incomplete lines
        if (width-remainingMines) == 1 :
            # Move star to the previous line
            array[height-nbFilledWidth-1] = 2*['.'] + (width-2)*['*']
            array[height-nbFilledWidth-2] = (width-1)*['.'] + ['*']
        elif height-nbFilledWidth-1 == 0 :
            array[height-nbFilledWidth-1] = (width-2-remainingMines)*['.'] + (remainingMines+2)*['*']
            array[height-nbFilledWidth] = 2*['.'] + (width-2)*['*']
        else :
            array[height-nbFilledWidth-1] = ['.']*(width-remainingMines)+remainingMines*['*']
        array[0][0] = 'c'
        return "\n".join([''.join(i) for i in array])
    else:
        return "Impossible"

testNb = int(input())
for test in range (1, testNb+1) :
    height, width, minesNumber = [int(n) for n in input().split()]
    print("Case #" + str(test)+":")
    print(minesField(width, height, minesNumber))
