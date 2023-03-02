from fractions import Fraction
systems, queries = input().split(" ")

unitsets = [[]]*int(systems)

for x in range(int(systems)):
    unitsets[x] = input().split(" ")

for x in range(int(queries)):
    system1, system2, value = input().split(" ")
    multi = (int(unitsets[int(system2) - 1][1]) - int(unitsets[int(system2) - 1][0]))
    divisor = (int(unitsets[int(system1)-1][1]) - int(unitsets[int(system1)-1][0]))
    Numerator = ((int(value) - int(unitsets[int(system1) - 1][0])) * multi) \
                + (int(unitsets[int(system2) - 1][0]) * divisor)
    system2fraction = Fraction(Numerator, divisor)
    if float(system2fraction).is_integer():
        print(str(system2fraction) + "/" + "1")
    else:
        print(system2fraction)

