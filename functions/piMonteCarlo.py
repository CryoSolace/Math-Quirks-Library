from random import random
from math import sqrt

def piMonteCarlo(iterations = 10000, showIteration = False):
    """Uses the monte carlo method to approximate pi. See: https://en.wikipedia.org/wiki/Monte_Carlo_method#Overview

    Keyword arguments:
    iterations -- int, Specifies the amount of iterations (default 10000)
    showIteration -- bool, Whether or not to show the amount of iterations (default False)
    
    Returns:
    pi -- float, The final approximation after the iterations

    Dependencies: 
    from random import random
    from math import sqrt

    Notes:
    The random library used here uses the Mersenne Twister PRNG. 

    The wikipedia article for Mersenne Twister states the following: 
    Multiple instances that differ only in seed value (but not other parameters) are not \
    generally appropriate for Monte-Carlo simulations that require independent random number \
    generators, though there exists a method for choosing multiple sets of parameter values.
    """

    circlePoints = 0
    totalPoints = 0

    for i in range(1,iterations+1):
        if sqrt(random()**2 + random()**2) <= 1:
            circlePoints += 1

        totalPoints += 1 
        pi = (circlePoints*4)/totalPoints 

        if showIteration:
            print(str(i) + ": " + str(pi))
        else:
            print(pi)

    return pi

