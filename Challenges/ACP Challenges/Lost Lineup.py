people = int(input())
lineup = [0]*(people)
lineup[0] = 1
infront = 0
if people > 1:
    infront = [int(x) for x in input().split(" ")]
for x in range(2, people+1):
    ahead = infront[x-2]
    lineup[ahead+1] = x
printable = ""
for x in lineup:
    printable = printable + str(x) + " "
print(printable)
