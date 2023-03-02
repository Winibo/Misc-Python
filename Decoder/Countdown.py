from multiset import Multiset

Enable1 = open(r"C:\Users\14038\Desktop\Enable1.txt").read().splitlines()
best = ""
s1 = Multiset("srkduaewn")
for i in Enable1:
    e1 = Multiset(i)
    common_char = s1 & e1
    if common_char == e1:
        if len(e1) == len(best):
            print(i)
            # print(len(i))
        if len(e1) > len(best):
            best = i

print(best)
# print(len(best))
