import itertools
import collections

sixrolls = itertools.product([1, 2, 3, 4, 5, 6], repeat=6)
twelverolls = itertools.product([1, 2, 3, 4, 5, 6], repeat=12)
eightteenrolls = itertools.product([1, 2, 3, 4, 5, 6], repeat=18)
sixtotal = 0
twelvetotal = 0
eightteentotal = 0
sixhits = 0
twelvehits = 0
eightteenhits = 0
for x in sixrolls:
    if collections.Counter(x)[6] >= 1:
        sixhits += 1
    sixtotal += 1
print("A Odds: " + str(sixhits/sixtotal))
for x in twelverolls:
    if collections.Counter(x)[6] >= 2:
        twelvehits += 1
    twelvetotal += 1
print("B Odds: " + str(twelvehits/twelvetotal))
for x in eightteenrolls:
    if collections.Counter(x)[6] >= 3:
        eightteenhits += 1
    eightteentotal += 1
print("C Odds: " + str(eightteenhits/eightteentotal))
