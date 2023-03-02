from decimal import *

for x in range(int(input())):
    r, b, m = [Decimal(x) for x in input().split(" ")]
    months = 0
    while True:
        prevb = b
        b = Decimal((b+(b/(100/r)))-m).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
        months += 1
        if prevb <= b or months == 1200:
            print("impossible")
            break
        if b <= 0:
            print(months)
            break
