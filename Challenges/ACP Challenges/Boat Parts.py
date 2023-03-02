totalparts, days = input().split(" ")
exchangedparts = set()
for x in range(int(days)):
    exchangedparts.add(input())
    if len(exchangedparts) == int(totalparts):
        print(x+1)
        break
if len(exchangedparts) != int(totalparts):
    print("paradox avoided")
