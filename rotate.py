#!/usr/bin/python3

# Clockwide rotation + gravity
def rotate(grid):
    width = len(grid)
    # Rotation
    newGrid = [[grid[y][x] for y in reversed(range(width))] for x in range(width)]

    # Gravity
    for x in range(width): # Browse every column
        newColumn = []
        # Adds every letter of the column to a new buffer
        for y in reversed(range(width)):
            if newGrid[y][x] != '.': 
                newColumn.append(newGrid[y][x])

        # Complete the column with dots
        for j in range(len(newColumn), width):
            newColumn.append('.')

        # Paste the new column into the grid
        for y in range(width):
            newGrid[y][x] = newColumn[width-(y+1)]
    return newGrid

# Searches for 'length' long chain of 'letter' characters in the 'grid' grid
def combinationSearch(grid, letter, length):
    width = len(grid)

    # Navigate every row
    for y in reversed(range(width)):
        counter = 0
        for x in range (width):
            if grid[y][x] == letter:
                counter+=1
                if counter >= length:
                    return True 
            else:
                counter=0

    # Navigate every column
    for x in range (width):
        counter =0
        for y in reversed(range(width)):
            if grid[y][x] == letter:
                counter+=1
                if counter >= length:
                    return True 
#            if grid[y][x] == '.':
#               break 
            else:
                counter=0

    # Navigate every \
    for firstcase in range(width):
        yAboveTriangle=0
        xAboveTriangle=firstcase

        counter1=0
        while yAboveTriangle < width and xAboveTriangle < width:
            if grid[yAboveTriangle][xAboveTriangle] == letter:
                counter1+=1
                if counter1 >= length:
                    return True
            else:
                counter1=0
            xAboveTriangle+=1
            yAboveTriangle+=1

        yBelowTriangle=firstcase
        xBelowTriangle=0
        counter2=0
        while yBelowTriangle < width and xBelowTriangle < width:
            if grid[yBelowTriangle][xBelowTriangle] == letter:
                counter2+=1
                if counter2 >= length:
                    return True
            else:
                counter2=0
            xBelowTriangle+=1
            yBelowTriangle+=1

    # Navigate every /
    for firstcase in reversed(range(width)):
        yAboveTriangle=0
        xAboveTriangle=firstcase

        counter1=0
        while yAboveTriangle < width and xAboveTriangle >= 0:
            if grid[yAboveTriangle][xAboveTriangle] == letter:
                counter1+=1
                if counter1 >= length:
                    return True
            else:
                counter1=0
            xAboveTriangle-=1
            yAboveTriangle+=1

        yBelowTriangle=firstcase
        xBelowTriangle=width-1
        counter2=0
        while yBelowTriangle < width and xBelowTriangle >= 0:
            if grid[yBelowTriangle][xBelowTriangle] == letter:
                counter2+=1
                if counter2 >= length:
                    return True
            else:
                counter2=0
            xBelowTriangle-=1
            yBelowTriangle+=1

    return False

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    infos=[int(n) for n in input().split()]
    gridWidth=infos[0]
    length=infos[1]
    grid = [[letter for letter in input()] for x in range(gridWidth)]
    grid = rotate(grid)

    redFound  = combinationSearch(grid, 'R', length)
    blueFound = combinationSearch(grid, 'B', length)

    if redFound and blueFound:
        print("Case #" + str(test) + ": Both")
    elif redFound:
        print("Case #" + str(test) + ": Red")
    elif blueFound:
        print("Case #" + str(test) + ": Blue")
    else:
        print("Case #" + str(test) + ": Neither")
