def light_on(times):
    ranges = []
    editedranges = []
    for x in times:
        ranges.append(set(range(x[0], x[1]+1)))
    while True:
        edited = False
        xedited = False
        delete = []
        for x in ranges:
            ranges[ranges.index(x)] = [-1, -1]
            for y in ranges:
                if min(x) in y or (min(y) in x and y):
                    editedranges.append(x.union(y))
                    edited = True
                    xedited = True
                    delete.append(y)
            if not xedited:
                editedranges.append(x)
            xedited = False
        for x in delete:
            try:
                editedranges.remove(x)
            except ValueError:
                pass
        if not edited or len(editedranges) == 1:
            break
        ranges = editedranges
        editedranges = []
    timelist = [sorted(x) for x in editedranges]
    if len(timelist) == 1:
        return max(max(timelist)) - min(min(timelist))
    else:
        timelist.sort(key=lambda z: z[0])
        subtractor = [(timelist[x+1][0] - timelist[x][-1]) for x in range(0, len(timelist)-1)]
        return max(max(timelist)) - min(min(timelist)) - sum(subtractor)


print(light_on([[1, 3], [2, 3], [4, 5]]))
print(light_on([[2, 4], [3, 6], [1, 3], [6, 8]]))
print(light_on([[6, 8], [5, 8], [8, 9], [5, 7], [4, 7]]))
print(light_on([[15, 18], [13, 16], [9, 12], [3, 4], [17, 20], [9, 11], [17, 18], [4, 5], [5, 6], [4, 5], [5, 6], [13, 16], [2, 3], [15, 17], [13, 14]]))
