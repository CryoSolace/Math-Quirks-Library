from math import sqrt

def primeBy6k(n,showSteps = False):
    step = 1
    while n % 6*step - 1 < sqrt(n): # looks broken, needs fixing, consult wikipedia
        if n % 6*step - 1 == 0:
            print(n)
        elif n % 6*step + 1 == 0:
            print(n)
        step += 1
primeBy6k(2)