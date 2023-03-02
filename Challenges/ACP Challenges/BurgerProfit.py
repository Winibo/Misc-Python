def maxprofit(buns, patties, cutlets, burgprofit, cutprofit):
    if buns < 2:
        return 0
    if buns % 2 != 0:
        buns = buns - 1
    if buns / 2 >= patties + cutlets:
        return (burgprofit * patties) + (cutlets * cutprofit)
    profit = 0
    while (patties+cutlets) > 0 and buns > 0:
        if burgprofit >= cutprofit:
            if patties > 0:
                profit += burgprofit
                buns -= 2
                patties -= 1
                continue
            profit += cutprofit
            buns -= 2
            cutlets -= 1
        if burgprofit < cutprofit:
            if cutlets > 0:
                profit += cutprofit
                buns -= 2
                cutlets -= 1
                continue
            profit += burgprofit
            buns -= 2
            patties -= 1
    return profit


queries = input()
for x in range(int(queries)):
    b, p, c = input().split(" ")
    bp, cp = input().split(" ")
    print(maxprofit(int(b), int(p), int(c), int(bp), int(cp)))
