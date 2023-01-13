from math import sqrt

def primeToRoot(n,showSteps = False):
    step = 1
    while step < sqrt(n):
        step += 1
        if n % step == 0:
            print("Not Prime.")
            return False
    print("Prime.")
    return True
    
primeToRoot(2)