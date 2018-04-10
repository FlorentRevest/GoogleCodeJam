#!/usr/bin/python3

# Every cell of the grid has to be either the max of its column or of its row

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    infos = [int(n) for n in input().split()]
    width = infos[1]
    height = infos[0]
    grid = [input().split() for i in range(height)]
    gridPossible = True
    maxColumns = [-1 for i in range(width)]
    maxRows =    [-1 for i in range(height)]

    # Populate maxColumns
    for x in range(width):
        for y in range(height):
            if int(grid[y][x]) > maxColumns[x]:
                maxColumns[x] = int(grid[y][x])

    # Populate maxRows
    for y in range(height) :
        for x in range(width):
            if int(grid[y][x]) > maxRows[y]:
                maxRows[y] = int(grid[y][x])

    for x in range(width):
        for y in range(height):
            if int(grid[y][x]) != maxColumns[x] and int(grid[y][x]) != maxRows[y]:
                gridPossible = False
                break

    print("Case #" + str(test) + (": YES" if gridPossible else ": NO"))
