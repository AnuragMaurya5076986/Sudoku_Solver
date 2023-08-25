import time, copy

# Sudoku Solver
# Written by Anurag Maurya
# December 16, 2022

grid = []

# Prints out a formatted version of the current grid
def printGrid(grid):
    for row_index, row in enumerate(grid):
        rowString = ""
        if row_index % 3 == 0 and row_index != 0:
            print("------|-------|-------")
        for index, element in enumerate(row):
            if index % 3 == 0 and index != 0:
                rowString += "| "
            if element == 0:
                rowString += "_ "
            else:
                rowString += str(element) + " "
        print(rowString)

# Prints out a much larger version of the current grid
# (remaining code for printExpandedGrid...)

# This finds all possible values for a square by eliminating those in the box that...
# (remaining code for findPossible...)

# This returns all elements in a given box
# (remaining code for box...)

# This attempts to find the/a next move
# (remaining code for nextMove...)

# This checks if the grid is finished
def hasMoves(grid):
    return any(0 in row for row in grid)

# This attempts to complete the grid by continually calling nextMove until it gets stuck or succeeds
def complete(grid, depth=0):
    moved = True
    while hasMoves(grid) and moved:
        moved = nextMove(grid, True, depth, True)
    return not hasMoves(grid)

# Checks if it can find a solution given a grid, and then a row-column pair with...
# (remaining code for testPossible...)

def isValid(grid):
    # Check that all rows contain no repeats
    for row in grid:
        found = []
        for i in row:
            if i in found:
                return False
            if i != 0:
                found.append(i)

        # Check that all columns contain no repeats
        for c in range(0, 9):
            found = []
            for r in range(0, 9):
                i = grid[r][c]
                if i in found:
                    return False
                if i != 0:
                    found.append(i)

    return True

# The UI, with options for entering grids, finding next moves, printing the current grid...
if len(grid) == 0:
    tempGrid = []

    data = ""
    while len(data) != 81:
        tempGrid = []
        data = input("Type in the grid, going left to right row by row, 0 = empty: ")
        if len(data) != 81:
            print("Not 81 characters.")
        else:
            for row in range(0, 9):
                r = []
                for col in range(0, 9):
                    r.append(int(data[row * 9 + col]))
                tempGrid.append(r)
            if not isValid(tempGrid):
                data = ""
                print("Invalid grid.")
                printGrid(tempGrid)

    grid = tempGrid

# Initialize variables
time1 = 0

c = input("Controls:\n\t'Enter': Display the next move\n\t'p': Print the current grid (small)\n\t'g': Print the current grid (large)\n\t'c': Complete the grid (or attempt to)\n\t'(r,c)': Prints the possible options for that row, column\n")
while hasMoves(grid) and (len(c) == 0 or c == "p" or c == "c" or c == "g" or c[0] == "("):
    if c == "p":
        printGrid(grid)
    elif c == "g":
        printExpandedGrid(grid)
    elif c == "c":
        time1 = time.time()
        if not complete(grid):
            print("Failed to complete. Please improve algorithm. :)")
            # break
    elif len(c) > 0 and c[0] == "(":
        print(findPossible(int(c[1]) - 1, int(c[3]) - 1, grid))
    else:
        nextMove(grid)

    if hasMoves(grid):
        c = input("Controls:\n\t'Enter': Display the next move\n\t'p': Print the current grid (small)\n\t'g': Print the current grid (large)\n\t'c': Complete the grid (or attempt to)\n\t'(r,c)': Prints the possible options for that row, column\n")
    else:
        time2 = time.time()
        printGrid(grid)
        if time1 != 0:
            print("Solved in %0.2fs!" % (time2 - time1))
        else:
            print("Solved!")
