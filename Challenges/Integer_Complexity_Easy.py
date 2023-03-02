import math


def smallest_factors(inputvalue):
    largest_factor = math.floor(math.sqrt(inputvalue))
    factors = [x for x in range(1, largest_factor+1) if inputvalue % x == 0]
    factorsums = sorted([inputvalue / x + x for x in factors])
    return factorsums[0]


print(smallest_factors(12345))
