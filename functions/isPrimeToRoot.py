from math import sqrt

def primeToRoot(n):
    """Checks whether a number is prime by testing all numbers up to square root of the given number.

    Keyword arguments:
    n -- int, The number to test for primality (no default)
    
    Returns:
    True / False -- bool, Whether or not the number given is prime

    Dependencies: 
    from math import sqrt
    """

    numTested = 1
    while numTested < sqrt(n):
        numTested += 1
        if n % numTested == 0:
            print("Not Prime")
            return False
    print("Prime")
    return True