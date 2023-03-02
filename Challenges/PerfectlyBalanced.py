def balanced(string):
    if string.lower().count("x") == string.lower().count("y"):
        return True
    return False


def balanced_bonus(string):
    split = list(string)
    if not split:
        return True
    testvalue = split[0]
    balancetest = string.lower().count(testvalue)
    split = [x for x in split if not x == testvalue]
    while split:
        testvalue = split[0]
        balancecount = string.lower().count(testvalue)
        if balancetest != balancecount:
            return False
        split = [x for x in split if not x == testvalue]
    return True


print(balanced_bonus(""))
