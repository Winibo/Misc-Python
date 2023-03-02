import re
file1 = open(r"C:\Users\14038\Desktop\Decode.txt", "r+")
file2 = open(r"C:\Users\14038\Desktop\Decoded.txt", "w+")
everyxth = 2
message = file1.read()
pattern = re.compile(r'[.?!]')
file1.close()
FindSentenceEnd = re.split(pattern, message)
x = len(FindSentenceEnd)
for i in range(x):
    if i % everyxth == 0:
        file2.write(FindSentenceEnd[i] + '.')
file2.close()
