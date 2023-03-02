import itertools

groups = [["Mailman", "Mailbox", "Bootstrap"], ["Pigeons", "Advertisers", "Factories"],
          ["Corporate Offices", "Two Hands", "Breeder"]]
combo1 = itertools.combinations(groups[0], 2)
combo2 = itertools.combinations(groups[1], 2)
combo3 = itertools.combinations(groups[2], 2)

allcombos = itertools.product(combo1, combo2, combo3)

for x in allcombos:
    print(x)
