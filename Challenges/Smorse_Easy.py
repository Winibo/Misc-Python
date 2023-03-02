import collections
import functools
import itertools
import more_itertools
import time
Enable1 = open(r"C:\Users\14038\Desktop\Enable1.txt").read().splitlines()
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


def most_common(count):
    testable_sequence = collections.Counter(smashed_morse(Enable1))
    return testable_sequence.most_common(count)


def dashes_in_a_row():
    testable_sequence = smashed_morse(Enable1)
    for word in testable_sequence:
        if len(word) < 15:
            Enable1.pop(testable_sequence.index(word))
            testable_sequence.remove(word)
        m = [x for x in testable_sequence if '---------------' in x]
        x = testable_sequence.index(m[0])
        plaintext = Enable1[x]
        word = m[0] + " " + plaintext
        return word


def perfectly_balanced(character_count):
    filtered = [x for x in Enable1 if len(x) == character_count]
    morse_unfiltered = smashed_morse(filtered)
    morse_filtered = [x for x in morse_unfiltered if len(x) % 2 == 0]
    counted = [dict(collections.Counter(x)) for x in morse_filtered]
    perfect = [counted.index(x) for x in counted if x.get("-") == x.get(".")]
    perfect_morse = [morse_filtered[x] for x in perfect]
    perfect_index = [morse_unfiltered.index(x) for x in perfect_morse]
    perfect_english = [filtered[x] for x in perfect_index]
    perfect_combined = [perfect_morse[x]+" "+perfect_english[x] for x in range(2)]
    return perfect_combined


def palindrome(character_count):
    filtered_english = [x for x in Enable1 if len(x) == character_count]
    morse_filtered = smashed_morse(filtered_english)
    morse_reversed = [x[::-1] for x in morse_filtered]
    palindrome_morse = [x for x in morse_filtered if x == morse_reversed[morse_filtered.index(x)]]
    palindrome_complete = [x+" "+filtered_english[morse_filtered.index(x)] for x in palindrome_morse]
    return palindrome_complete


def unique_permutations(length):
    unique_perms = []
    for x in range(length+1):
        if x > 0:
            dots = list(itertools.product(".", repeat=x))
        else:
            dots = ""
        if x < 13:
            dashes = list(itertools.product("-", repeat=13-x))
        else:
            dashes = ""
        if dots:
            dots = functools.reduce(lambda a, b: a + b, functools.reduce(lambda a, b: a + b, dots))
        if dashes:
            dashes = functools.reduce(lambda a, b: a + b, functools.reduce(lambda a, b: a + b, dashes))
        end_string = dots + dashes
        unique_perms += list(more_itertools.distinct_permutations(end_string))
    unique_perms = [functools.reduce(lambda a, b: a + b, x) for x in unique_perms]
    return unique_perms


def non_existent(character_count):
    # Really Really Slow
    morse_unfiltered = smashed_morse(Enable1)
    permutations = unique_permutations(13)
    morse_filtered = set([x for x in morse_unfiltered if len(x) >= character_count])
    # The Culprit
    used = [[x for x in permutations if x in group] for group in morse_filtered]
    used = set(itertools.chain.from_iterable(used))
    permutations = set(permutations)
    unused = permutations.difference(used)
    return unused


start_time = time.time()
print("Morse List:")
print(smashed_morse(Enable1))
print("Most Common Sequence:")
print(most_common(1))
print("Most Dashes in a Row:")
print(dashes_in_a_row())
print("Perfectly Balanced 21 character string:")
print(perfectly_balanced(21))
print("13 character palindromes:")
print(palindrome(13))
print("13 length strings that don't appear:")
print(non_existent(13))
print("Time Taken:")
print(time.time() - start_time)
