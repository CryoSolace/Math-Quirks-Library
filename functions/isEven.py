def isEven(n):
    """Checks whether a number is even or not by testing whether the number modulo two is equal to zero.

    Keyword arguments:
    n -- int, The number to test for evenness (no default)
    
    Returns:
    True / False -- bool, Whether or not the number given is even

    Dependencies: 
    None
    """

    if n % 2 == 0:
        print("Yes")
        return True
    else:
        print("No")
        return False