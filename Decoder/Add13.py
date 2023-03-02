ShiftAmount = -1
file1 = open(r"C:\Users\14038\Desktop\Decode.txt", "r+")
file2 = open(r"C:\Users\14038\Desktop\Decoded.txt", "w+")
words = []
decoded = []
for line in file1:
    words = line.split(" ")
for i in words:
    try:
        if int(i) != 0:
            i = int(i) + ShiftAmount
            if int(i) > 26:
                i = int(i)-26
            if int(i) < 0:
                i = int(i)+26
    except ValueError:
        i = i
    decoded.append(i)
for listitem in decoded:
    file2.write(str(listitem))
    file2.write(" ")
file1.close()
file2.close()
