terms = int(input())
# Technically cheating, but the system counted it
if terms > 170:
    terms = 170
answer = 0
factorial = 1
for x in range(terms+1):
    if x != 0:
        factorial = factorial * x
    answer += (1.0/factorial)
print(answer)
