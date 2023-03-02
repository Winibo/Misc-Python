def addition(a, b):
    return a+b


def multiplication(a, b):
    c = 0
    for x in range(0, abs(b)):
        c += abs(a)
    if (a >= 0 and b >= 0) or (a <= 0 and b <= 0):
        return c
    else:
        return -c


def subtraction(a, b):
    c = 0
    while True:
        if b+c == a:
            return c
        if b > a:
            c += -1
        else:
            c += 1


def division(a, b):
    if a == 0 and b == 0:
        return "Undefined Error"
    incr = 0
    signcheck = a
    while True:
        if a == 0:
            if (signcheck >= 0 and b >= 0) or (signcheck <= 0 and b <= 0):
                return incr
            else:
                return -incr
        if a < 0:
            return "Non-Integer Error"
        a = subtraction(abs(a), abs(b))
        incr += 1


def exponentiation(a, b):
    if b < 0:
        return "Non-integer Error"
    if b == 0:
        return 1
    c = a
    while True:
        b += -1
        if b == 0:
            return a
        a = multiplication(a, c)


user_input = input("Input operation:")
split = user_input.split(" ")
if split[1] == "+":
    print(addition(int(split[0]), int(split[2])))
elif split[1] == "*":
    print(multiplication(int(split[0]), int(split[2])))
elif split[1] == "-":
    print(subtraction(int(split[0]), int(split[2])))
elif split[1] == "/":
    print(division(int(split[0]), int(split[2])))
elif split[1] == "^":
    print(exponentiation(int(split[0]), int(split[2])))
