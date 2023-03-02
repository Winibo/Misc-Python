import re


def baumsweetsequence(maximum):
    baumvalue = [1]
    zerostrings = []
    sequence = [bin(x)[2:] for x in range(1, maximum+1)]
    for x in sequence:
        zerostrings.append(re.findall('0+', x))
    for x in zerostrings:
        if not x:
            baumvalue.append(1)
        else:
            oddcheck = 1
            for y in x:
                if len(y) % 2 != 0:
                    oddcheck = 0
                    break
            baumvalue.append(oddcheck)
    return baumvalue


print(baumsweetsequence(20))
