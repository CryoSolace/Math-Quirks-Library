from random import random
from math import sqrt

def pimontecarlo(showIteration = False, iterations = 10000):
    circlePoints = 0
    totalPoints = 0
    for i in range(1,iterations+1):
        if sqrt(random()**2 + random()**2) <= 1:
            circlePoints += 1
        totalPoints += 1 

        if showIteration:
            print(str(i) + ": " + str((circlePoints*4)/totalPoints ))
        else:
            print((circlePoints*4)/totalPoints )

pimontecarlo(True)
#note randint uses mersenne twister which is not suitable for montecarlo sims