import itertools

dicenum = 5
possibilities = 20**dicenum

total = 0
numberofvalidcombos = [0] * 20


def test(x):
    numberofvalidcombos[max(x)-1] += 1


iterable = map(test, itertools.product(range(1, 21), repeat=dicenum))

for x in iterable:
    pass

for x in range(20):
    print(str(x+1) + ": " + str(numberofvalidcombos[x]/possibilities))
