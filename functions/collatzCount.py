def collatzCount(n, showSteps=True, showStepNum=True):
    """Prints the steps and the amount of steps for a number to reach 1 in the Collatz Conjecture. See: https://en.wikipedia.org/wiki/Collatz_conjecture

    Keyword arguments:
    n -- int, The number to test (no default)
    showSteps -- bool, Whether or not to show the steps taken (default True)
    showStepNum -- bool, Whether or not to show the amount of steps (default True)

    Returns:
    steps -- int, The number of steps taken for n to reach 1
    
    Dependencies: 
    None
    """

    steps = 0

    while n != 1:
        steps += 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1

    if showSteps:
        print(n)

    if showStepNum:
        print(f"Steps: {steps}")
        
    return steps
