import itertools
import functools
import collections
Enable1 = open(r"C:\Users\14038\Desktop\Enable1.txt").read().splitlines()


def wordfunnel(word, substring):
    possibilities = list(itertools.combinations(word, len(word)-1))
    possibilities = [functools.reduce(lambda a, b: a + b, x) for x in possibilities]
    true = [x for x in possibilities if x == substring]
    if true:
        return True
    else:
        return False


def wordfunnelbonus(word):
    possibilities = list(itertools.combinations(word, len(word)-1))
    possibilities = [functools.reduce(lambda a, b: a + b, x) for x in possibilities]
    substrings = []
    for value in Enable1:
        for x in possibilities:
            if x == value:
                substrings.append(x)
    return list(set(substrings))


def wordfunnelsecondbonus():
    fivewords = []
    counts = collections.Counter([len(x) for x in Enable1])
    filtered = [x for x in Enable1 if counts[len(x)-1] >= 5]
    filtered = [x for x in filtered if len(x) >= 4]
    filtered.sort(key=len)
    for value in filtered:
        possibilities = [x for x in filtered if len(x) == len(value)-1]
        solutions = wordfunnelbonus(value)
        words = [[x for x in solutions if x == group] for group in possibilities]
        if len(words) == 5:
            fivewords.append(value)
            fivewords.append(":")
            fivewords.append(wordfunnelbonus(value))
            fivewords.append(";")
        if len(fivewords) == 28:
            return fivewords
        print(len(fivewords))
        print(value)


print(wordfunnel("skiff", "ski"))
print(wordfunnelbonus("boats"))
print(wordfunnelsecondbonus())
