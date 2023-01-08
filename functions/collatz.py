def collatz(n,showSteps=True):
    steps = 0
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
        print(n)

    if showSteps:
        print(f"Steps: {steps}")

