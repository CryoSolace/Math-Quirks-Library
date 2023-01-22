from isEven import isEven

def isOdd(n):
    """Checks whether a number is odd or not by testing calling the isEven function and returning the opposite of it.

    Keyword arguments:
    n -- int, The number to test for oddness (no default)
    
    Returns:
    True / False -- bool, Whether or not the number given is odd

    Dependencies: 
    from isEven import isEven
    """

    if not isEven(n):
        print("Yes")
    else:
        print("No")

    return not isEven(n)