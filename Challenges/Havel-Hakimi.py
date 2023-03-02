def removezeros(args):
    arguments = []
    for i in range(len(args)):
        if args[i] != 0:
            arguments.append(args[i])
    return arguments


def bubblesort(arglist):
    sort = []
    for i in range(len(arglist)):
        largest = arglist[0]
        remove = 0
        for j in range(len(arglist)):
            if largest < arglist[j]:
                largest = arglist[j]
                remove = j
        sort.append(largest)
        arglist.pop(remove)
    return sort


def lengthcheck(length, arglist):
    if length > len(arglist):
        return True
    else:
        return False


def frontelim(length, arglist):
    for i in range(0, length):
        arglist[i] = arglist[i] - 1
    return arglist


def havelhakimi(suspects):
    zerosremoved = removezeros(suspects)
    if not zerosremoved:
        return True
    bubblesorted = bubblesort(zerosremoved)
    first = bubblesorted[0]
    bubblesorted.pop(0)
    if lengthcheck(first, bubblesorted):
        return False
    frontgone = frontelim(first, bubblesorted)
    return havelhakimi(frontgone)


print(havelhakimi([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
