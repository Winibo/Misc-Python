def fit1(leng, wid, x, y):
    length = leng / x
    width = wid / y
    return int(length)*int(width)


def fit2(leng, wid, x, y):
    if fit1(leng, wid, x, y) > fit1(leng, wid, y, x):
        return fit1(leng, wid, x, y)
    else:
        return fit1(leng, wid, y, x)


def fit3(length, width, height, x, y, z):
    if length % x == 0:
        if fit1(height, width, z, y) > fit1(height, width, y, z):
            return fit1(height, width, z, y) * length/x
        else:
            return fit1(height, width, y, z) * length/x
    elif length % y == 0:
        if fit1(height, width, z, y) > fit1(height, width, y, z):
            return fit1(height, width, z, y) * length/x
        else:
            return fit1(height, width, y, z) * length/x
# TODO: fit3 and fitn
