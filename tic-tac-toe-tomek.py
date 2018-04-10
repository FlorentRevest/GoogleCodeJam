#!/usr/bin/python3

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    grid = [input(), input(), input(), input()] # Array of strings

    xWon = False
    oWon = False
    # Lines X
    posY = 0
    while posY < 4 and xWon == False:
        posX = 0
        while posX < 4 and (grid[posY][posX] == 'X' or grid[posY][posX] == 'T'):
            posX+=1

        if posX == 4:
            xWon = True
        else:
            posY+=1;

    # Columns X
    posX, posY = (0,0)
    while posX < 4 and xWon == False :
        posY = 0
        while posY < 4 and (grid[posY][posX] == 'X' or grid[posY][posX]=='T'):
            posY += 1

        if posY == 4:
            xWon = True
        else:
            posX += 1

    # Diagonals
    posX = 0
    while posX < 4 and (grid[posX][posX] =='X' or grid[posX][posX] =='T') and xWon == False :
        posX += 1
    if posX == 4 :
        xWon = True

    posX = 3
    while posX > -1 and (grid[posX][3-posX] =='X' or grid[posX][3-posX]=='T') and xWon == False :
        posX -= 1
    if posX == -1 :
        xWon = True

    if xWon:
        print("Case #" + str(test) + ": " + str("X won"))
    else:
        # Lines O
        posY = 0
        while posY < 4 and oWon == False:
            posX = 0
            while posX < 4 and (grid[posY][posX] == 'O' or grid[posY][posX] == 'T'):
                posX+=1

            if posX == 4:
                oWon = True
            else:
                posY+=1;

        # Columns O
        posX, posY = (0,0)
        while posX < 4 and oWon == False :
            posY = 0
            while posY < 4 and (grid[posY][posX] == 'O' or grid[posY][posX]=='T'):
                posY += 1

            if posY == 4:
                oWon = True
            else:
                posX += 1

        # Diagonals
        posX = 0
        while posX < 4 and (grid[posX][posX] =='O' or grid[posX][posX] =='T') and oWon == False :
            posX += 1
        if posX == 4 :
            oWon = True

        posX = 3
        while posX > -1 and (grid[posX][3-posX] =='O' or grid[posX][3-posX]=='T') and oWon == False :
            posX -= 1
        if posX == -1 :
            oWon = True

    if oWon:
        print("Case #" + str(test) + ": " + str("O won"))

    if not xWon and not oWon:
        if '.' in grid[0] or '.' in grid[1] or '.' in grid[2] or '.' in grid[3]:
            print("Case #" + str(test) + ": " + str("Game has not completed"))
        else:
            print("Case #" + str(test) + ": " + str("Draw"))
    if test != testsNb:
        input() # Empty line
