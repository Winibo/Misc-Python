file1 = open(r"C:\Users\14038\Desktop\Decode.txt", "r+")
file2 = open(r"C:\Users\14038\Desktop\Decoded.txt", "w+")
everyxth = 15
words = []
for line in file1:
    words = line.split(" ")
x = len(words)
for word in range(x):
    if word % everyxth == 0:
        file2.write(words[word])
        file2.write(" ")
