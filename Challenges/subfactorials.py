import math


def subfactorial(n):
    subfact = []
    for x in n:
        if x != 0:
            subfact.append(round(math.factorial(x)/math.e))
        else:
            subfact.append(1)
    return subfact


print(subfactorial([0, 1, 2, 3]))
