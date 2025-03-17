#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element at specific position without modifying original list.

    Args:
        my_list: The original list
        idx: The index to replace element at
        element: The new element to insert

    Returns:
        A new list with the element replaced, or copy of original if idx invalid
    """
    # Create a copy of the original list
    new_list = my_list.copy()
    
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return new_list
    
    # Replace element at idx in the new list
    new_list[idx] = element
    return new_list
