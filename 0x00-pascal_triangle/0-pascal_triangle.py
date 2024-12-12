#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """
    A function that returns a list
    of integers representing the
    Pascal triangle of n:
       . Returns an empty list if n <= 0
       . Assumes n will be always an integer
    """
    # Initialize an empty list to hold the rows of Pascal's Triangle
    pascal_tri = []

    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Loop through each row (i is the row index)
    for i in range(n):
        # If it's the first row, add [1] (the first row of Pascal's triangle)
        if i == 0:
            pascal_tri.append([1])
        else:
            # For subsequent rows, initialize an empty list for the current row
            cur_row = []
            # Loop through each element in the current row (j is the column index)
            for j in range(i + 1):
                # The first and last elements in each row are always 1
                if j == 0 or j == i:
                    cur_row.append(1)
                else:
                    # The value at position (i, j) is the sum of the two values
                    # from the previous row: (i-1, j-1) and (i-1, j)
                    cur_row.append(pascal_tri[i - 1][j - 1] + pascal_tri[i - 1][j])

            # Add the current row to the triangle
            pascal_tri.append(cur_row)

    # Return the complete Pascal's Triangle
    return pascal_tri
