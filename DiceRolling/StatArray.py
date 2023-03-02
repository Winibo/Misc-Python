import random


stats = [[], [], [], [], [], []]
for x in range(6):
    stats[x] = [random.randint(1, 6) for y in range(4)]
    stats[x].remove(min(stats[x]))

print(stats)
for x in stats:
    print(sum(x))
