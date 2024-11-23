#!/usr/bin/python3
"""
This module provides an algorithm to rotate a 2D matrix 90 degrees clockwise.
APPROACH:
    -> Flatten the 2D matrix into a 1D array by representing each
       row-column pair as a single index. Using this index, the
       corresponding row and column can be derived since the matrix
       is square (width equals height).
        -> Row index can be calculated as floor(flattened_index / width)
           e.g., if the flattened index is 20 and the width is 5,
           the row index is 4 (i.e., the 5th row, 0-based index).
        -> Column index can be calculated as flattened_index % width
           e.g., if the flattened index is 20 and the width is 5,
           the column index is 0 (i.e., the 1st column, 0-based index).
    -> Generate all possible indices (equal to width * height of the matrix).
    -> Create a mapping for each flattened index:
        -> The new index after rotation.
        -> The value corresponding to the current index.
    -> Iterate through the mapping and place each value in its updated position.
FUNCTIONS:
    rotate_2d_matrix -> Main function that combines all components to perform the rotation.
    build_map -> Creates a mapping for each flattened index to:
        -> Its updated index after rotation.
        -> The value at the current index.
        map_structure = {
            index: {
                'new_index': computed_new_index,
                'value': value at the current index
            }
        }
    get_new_index -> Determines the updated index after rotation.
        Parameters:
        index -> Index to calculate the new position for.
        width -> The width of the matrix.
        LOGIC:
            -> Derive the current column index.
            -> Derive the current row index.
            -> Calculate the updated column index as width - 1 - current_row_index.
               Example:
               Element 4 starts at column index 0, row index 1.
               After rotation, its new column index is 1, which equals:
               (3 - 1 - 1), where 3 is the width.
                Before Rotation [           After Rotation [
                        [1, 2, 3],              [7, 4, 1],
                        [4, 5, 6],              [8, 5, 2],
                        [7, 8, 9]               [9, 6, 3],
                ]                       ]
            -> Updated row index becomes the current column index.
               Example:
               Element 6 starts at row index 1, column index 2.
               After rotation, its new row index is 2, which equals the current column index.
                Before Rotation [           After Rotation [
                        [1, 2, 3],              [7, 4, 1],
                        [4, 5, 6],              [8, 5, 2],
                        [7, 8, 9]               [9, 6, 3],
                ]                       ]
            -> Compute the flattened index for the new position and return it.
    get_value -> Retrieves the value from the original matrix using the flattened index.
    compute_row_and_index -> Converts a flattened index into row and column indices.
"""

def rotate_2d_matrix(m):
    """Main function to rotate a 2D matrix 90 degrees clockwise."""
    width = len(m[0])
    height = len(m)
    total_items = width * height
    map_ = build_map(m, total_items, width)
    for index in map_:
        prev_index = index
        value = map_[prev_index]["value"]
        new_index = map_[prev_index]["new_index"]
        row, col = compute_row_and_index(new_index, width)
        m[row][col] = value

def build_map(m, length, width):
    """Creates a mapping of each index to its new position and value."""
    return {
        i: {
            "new_index": get_new_index(i, width),
            "value": get_value(m, i, width)
        }
        for i in range(length)
    }

def get_new_index(i, width):
    """Calculates the new index after rotation."""
    current_col = i % width
    current_row = i // width
    next_col = width - 1 - current_row
    next_row = current_col
    return next_row * width + next_col

def get_value(m, i, width):
    """Retrieves the value from the matrix using the flattened index."""
    current_col = i % width
    current_row = i // width
    return m[current_row][current_col]

def compute_row_and_index(flat_index, width):
    """Converts a flattened index back into row and column indices."""
    row = flat_index // width
    col = flat_index % width
    return row, col

def printx(lst):
    """Custom function to neatly display a 2D matrix."""
    print("[")
    for row in lst:
        print("  ", str(row) + ",")
    print("]")

def build_matrix(n):
    """Generates an n x n matrix filled with consecutive integers."""
    matrix = []
    value = 1
    for _ in range(n):
        row = []
        for x in range(value, n * n + 1):
            row.append(x)
            if x % n == 0:
                value = x + 1
                break
        matrix.append(row)
    return matrix

if __name__ == "__main__":
    matrix = build_matrix(3)
    rotate_2d_matrix(matrix)
    printx(matrix)
    print()
    matrix = build_matrix(5)
    rotate_2d_matrix(matrix)
    printx(matrix)
