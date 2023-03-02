lookup = {0: [2, 2], 1: [2, 1], 2: [2, 1], 3: [2, 0], 4: [1, 2], 5: [1, 1], 6: [1, 1], 7: [1, 0], 8: [1, 2],
          9: [1, 1], 10: [1, 1], 11: [1, 0], 12: [0, 2], 13: [0, 1], 14: [0, 1], 15: [0, 0]}
broken = int(input())
tb, lr = 0, 0
for x in range(broken):
    t, l = [x for x in lookup[int(input(), 2)]]
    tb += t
    lr += l
tbmax = tb//2
lrmax = lr//2
totalswords = min(tbmax, lrmax)
tb = tb - 2*totalswords
lr = lr - 2*totalswords
print(str(totalswords) + " " + str(tb) + " " + str(lr))
