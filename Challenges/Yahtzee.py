import collections
import time
Yahtzee = open(r"C:\Users\14038\Desktop\Yahtzeelist.txt").read().splitlines()

start = time.time()


def highest_score(numbers):
    totalscores = []
    sortedscore = dict(collections.Counter(numbers))
    for k, v in sortedscore.items():
        totalscores.append(int(k)*v)
    return max(totalscores)


print(highest_score(Yahtzee))
print("Time Taken:")
print(time.time() - start)
