import re

wordlist = open(r"C:\Users\14038\Desktop\dwylwordlist.txt").read().splitlines()

longest_words = []

wordlist.sort(key=len, reverse=True)
for x in wordlist:
    # Could also include IO and S. GKMQVWXZ CAN NEVER BE DISPLAYED ACCURATELY
    if re.findall("[gkmqvwxz]", x):
        continue
    if len(longest_words) == 0:
        longest_words.append(x)
        continue
    if len(x) < len(longest_words[0]):
        break
    longest_words.append(x)


print(longest_words)
