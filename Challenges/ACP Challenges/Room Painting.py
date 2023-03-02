sizes, colours = [int(x) for x in input().split(" ")]
sizelist = []
for x in range(sizes):
    sizelist.append(int(input()))
sizelist.sort()
waste = 0
for x in range(colours):
    amount = int(input())
    for y in sizelist:
        if amount <= y:
            waste += y-amount
            break
print(waste)
