file1 = open(r"C:\Users\14038\Desktop\Decode.txt", "r+")
words = []
decoded = ""
for line in file1:
    words = line.split(" ")
for x in words:
    decoded = decoded + chr(int(x))
print(decoded)
