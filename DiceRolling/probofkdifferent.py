def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def probofkdiff(input):
    throws, sides, different = input.split(" ")
    sidelist = [x for x in range(1, int(sides) + 1)]
    possibilities = [set(x) for x in product(sidelist, repeat=int(throws))]
    validcombos = [x for x in possibilities if len(x) >= int(different)]
    return len(validcombos) / len(possibilities)


inputstring = input("Please input n,s,k:")
print(probofkdiff(inputstring))
input("Press any key to end")
