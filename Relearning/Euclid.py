import math

x = int(input("Input The larger value"))
y = int(input("Input the smaller value"))

r = y % x
print("extended euclid = ")
while r != 0:
    y = x
    x = r
    r = y % x
    if r != 0:
        print(str(r) + '=' + str(y) + '-' + str(math.floor(y/x)) + '*' + str(x))
print("gcd = ")
print(x)
