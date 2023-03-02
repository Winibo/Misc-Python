import itertools
from collections import Counter

possible = itertools.product([1, 3, 4, 5, 6, 7, 8, 9], repeat=3)

remaining = set(map(lambda x: tuple(sorted(x)), possible))
output = []
for x in remaining:
    if Counter(x).most_common(1)[0][1] <= 1:
        output.append(x)

for x in output:
    if sum(x) == 15:
        print(x)
