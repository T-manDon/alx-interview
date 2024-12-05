#!/usr/bin/python3
"""
This func will def island_perimeter which determines the island perimeter
of the water body
"""

bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """Func to find cells containing 4, 3, 2 or 1 within the  boundarythen add into
       appropriate set
       Args:
           grid (list): 2d list
           i (int): row number
           j (int): column number
    """
    boundaries = 0
    try:
        if i == 0:
            boundaries += 1
        elif grid[i-1][j] == 0:
            boundaries += 1
    except:
        boundaries += 1
    try:
        if grid[i+1][j] == 0:
            boundaries += 1
    except:
        boundaries += 1
    try:
        if grid[i][j+1] == 0:
            boundaries += 1
    except:
        boundaries += 1
    try:
        if j == 0:
            boundaries += 1
        elif grid[i][j-1] == 0:
            boundaries += 1
    except:
        boundaries += 1

    if boundaries == 1:
        bound_1.add((i, j))
    elif boundaries == 2:
        bound_2.add((i, j))
    elif boundaries == 3:
        bound_3.add((i, j))
    elif boundaries == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """
    func calc and gives the island perimeter inside the gride
    the grid comprise aa rectangular grid in which 0s stands for water and 1s for land
    the cells are squared with a side length of 1
    The island only one
    Args:
        grid [list] : 2d list of ints either 0 or 1
    Return:
       perimeter of island
    """
    if grid == []:
        return 0
    l = len(grid)
    w = len(grid[0])
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 1:
                boundary(grid, i, j)
                if len(bound_4) != 0:
                    return 4
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + (len(bound_1))
    return perimeter
