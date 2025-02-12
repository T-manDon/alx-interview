#!/usr/bin/python3
"""
Determines whether all boxes in a list of lists can be opened 
using keys stored within the boxes.
"""

def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each index represents a box,
    and the contents are keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    position = 0  # Represents the current box index
    unlocked = {}  # Dictionary to track unlocked boxes

    for box in boxes:
        # The first box is always unlocked, or an empty box is considered unlocked
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        
        # Add keys found in the box to the unlocked dictionary
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        
        # If the number of unlocked boxes matches the total boxes, return True
        if len(unlocked) == len(boxes):
            return True
        
        position += 1  # Move to the next box

    return False  # If not all boxes are unlocked, return False

