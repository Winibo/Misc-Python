import math
total = 0


def additivepersistance(number):
    global total
    if total == 0 and number < 10:
        return 0
    digits = []
    place = int(math.log10(number)+1)
    for i in range(int(math.log10(number)+1)):
        power = pow(10, place-1)
        remainder = number % power
        digits.append((number-remainder)/power)
        number = remainder
        place -= 1
    number = sum(digits)
    print(number)
    total += 1
    if number < 10:
        return total
    else:
        return additivepersistance(number)


print(additivepersistance(998))
