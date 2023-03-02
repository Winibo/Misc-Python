import itertools

possibilities = list(itertools.product(range(1, 21), repeat=20))
total = 0
for x in possibilities:
    total = total + max(x)

print(total/len(possibilities))
