totalcost = 0
cost = input()
for x in range(int(input())):
    length, width = input().split(" ")
    totalcost = totalcost + (float(length) * float(width) * float(cost))
print(totalcost)
