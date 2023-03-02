tests = input()

for x in range(int(tests)):
    cities = set()
    numberoftrips = input()
    for x in range(int(numberoftrips)):
        cities.add(input())
    print(len(cities))
