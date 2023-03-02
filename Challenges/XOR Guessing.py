import sys
# set up for question


input1 = list(range(0, 100))
guess1 = "? "
for x in input1:
    guess1 = guess1 + str(x) + " "
guess1 = guess1 + "\n"
print(guess1)
sys.stdout.flush()

result1 = input()

possibilities = [x ^ int(result1) for x in input1]

input2 = []
for x in range(100):
    input2.append(2**7+(x*(2**7)))
guess2 = "? "
for x in input2:
    guess2 = guess2 + str(x) + " "
guess2 = guess2 + "\n"
print(guess2)
sys.stdout.flush()
result2 = input()

possibilities = list(set(possibilities) & set([x ^ int(result2) for x in input2]))

print("! " + str(possibilities[0]) + "\n")
sys.stdout.flush()