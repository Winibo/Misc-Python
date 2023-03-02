Alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
file1 = open(r"C:\Users\14038\Desktop\Decode.txt", "r+")
file2 = open(r"C:\Users\14038\Desktop\Decoded.txt", "w+")
words = []
decoded = ""
for line in file1:
    words = line.split(" ")
for i in words:
    try:
        decoded = decoded + Alphabet[int(i)]
    except ValueError:
        decoded = decoded + i
file2.write(decoded)
