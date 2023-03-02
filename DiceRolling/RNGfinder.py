import random

x = 0

while True:
    random.seed(x)
    rolls = [random.randint(1, 20) for x in range(2)]
    print(rolls)
    if rolls == [20, 1]:
        break
    x += 1

print(x)
