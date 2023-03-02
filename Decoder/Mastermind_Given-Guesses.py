import itertools
from multiset import Multiset


# Find all the remaining possibilities, given a guess, the list of possibilities,
# and the "score" (results) of that guess
def find_remaining(guess, hits, close, possibilities):
    new_possibilities = []
    for x in possibilities:
        exact_matches = 0
        # Find the number of hits/exact matches between the 2
        for y in range(len(x)):
            if guess[y] == x[y]:
                exact_matches += 1
        # Create a set that only contains the results that appear in both sets
        # Equivalent to taking the union of a mathematical set,
        # but these sets allow for a result to appear multiple times
        combos = Multiset(guess) & Multiset(x)
        # The number of misses is the length of this new set less all the exact matches
        # that appear in the set
        near_matches = len(combos) - exact_matches
        # If the possibility is valid, append it to the list of valid results
        if near_matches == close and exact_matches == hits:
            new_possibilities.append(x)
    return new_possibilities


pegs = input("Please Input number of numbers/colours: ")
if pegs == 10:
    print("Note: When entering guesses, 0=10 (so 1 5 0 should be input as 1 5 10)")
guess_length = input("Please input the length of each guess: ")
guess_values = [x for x in range(1, int(pegs)+1)]
current_possibilities = itertools.product(guess_values, repeat=int(guess_length))
while True:
    temp = list(current_possibilities)
    current_guess = input("Please input the next guess, with each value separated by a space: ")
    current_guess = current_guess.split(" ")
    current_guess = [int(x) for x in current_guess]
    current_hits = input("Input the number of correct pegs in the right position: ")
    current_close = input("Input the number of correct pegs in the wrong position: ")
    current_possibilities = find_remaining(current_guess, int(current_hits), int(current_close), temp)
    print("The remaining possibilities are:")
    print(list(current_possibilities))
    if len(current_possibilities) == 1:
        break
