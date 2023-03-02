import functools
import itertools
morse = [" ", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

Alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def smashed_morse(word_list):
    char_list = list(map(list, word_list))
    index_number = [[Alphabet.index(x) for x in group] for group in char_list]
    char_morse = [[morse[x] for x in group] for group in index_number]
    if isinstance(word_list, list):
        morse_decoded = [functools.reduce(lambda a, b: a + b, x) for x in char_morse]
    else:
        morse_decoded = functools.reduce(lambda a, b: a + b, functools.reduce(lambda a, b: a + b, char_morse))
    return morse_decoded

def alphabetpermute(morsepermutation):
    alphabetpermutations = itertools.permutations("abcdefghijklmnopqrstuvwxyz")
    while True:
        currentalphabetpermutation = next(alphabetpermutations)
        if morsepermutation == smashed_morse(currentalphabetpermutation):
            return currentalphabetpermutation


print(alphabetpermute(".----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-"))
