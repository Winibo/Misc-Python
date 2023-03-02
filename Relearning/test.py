Enable1 = open(r"C:\Users\14038\Desktop\Enable1.txt").read().splitlines()

for word in Enable1:
    if len(word) == 5:
        if word[0] == 's':
            if word[1] == 't':
                if word[2] == 'a':
                    print(word)
