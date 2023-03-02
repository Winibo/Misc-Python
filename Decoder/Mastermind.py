import itertools
from multiset import Multiset


# Gives all the possible "scores" that a valid guess could have
def possible_scores(length):
    # Take all the possibilities from 0 - length of guess (default of 0-4)
    guess_possibilities = [x for x in range(0, length+1)]
    possibilities = itertools.product(guess_possibilities, repeat=2)

    # For all possibilities, only keep possibilities whose sum is less than or equal to length
    # i.e for guess length of 4, remove possibilities such as (4,4) or (3,2)
    # Since they could never be valid results for a guess
    possibilities = [x for x in possibilities if sum(x) <= length]

    # remove the second to last option (for 4 length, that would be (3,1))
    possibilities.remove(possibilities[-2])
    return possibilities


# given a guess, and an answer, calculate the score that guess would return in form (hits, misses)
# See find_remaining for slightly better comments
def guess_score(guess, answer):
    exact_matches = 0
    # Find the # of exact matches
    for x in range(len(guess)):
        if guess[x] == answer[x]:
            exact_matches += 1
    # Find the # of misses/close matches
    combos = Multiset(guess) & Multiset(answer)
    near_matches = len(combos) - exact_matches
    # Return the score of that guess
    score = (exact_matches, near_matches)
    return score


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


# Given a the list of all possibilities, the remaining possibilities, and the list of previous guesses,
# Calculates the best possibility to guess next
# The best possibility is the one that would remove the most possible options in the worst case scenario
# So a guess that removes 5 at worst, but can't be possible is better than
# an guess that could be possible that removes 3 at worst but is possible
# but is worse than a guess that removes 5 at worst and is possible
def mini_max(possibilities, remaining_possibilities, previous_guesses):
    guess_worst = []

    # Get all possible results for a score (in form of hits, misses)
    all_possible = possible_scores(len(possibilities[0]))

    # for all possibilities that have not been guessed
    for x in possibilities:
        print(x)
        if x not in previous_guesses:

            # create an array of all 0's equal to the length of all possible guesses
            scores = [0] * len(all_possible)

            # for all remaining possibilities, calculate what score it would receive if the current possibility was
            # the correct answer, and add 1 to that score on the list
            for y in remaining_possibilities:
                value = guess_score(y, x)
                scores[all_possible.index(value)] += 1
            # Every value in the scores array is the # of valid options that would
            # remain if we were to get that result from our guess
            # a 0 in the array means that if we were to get the corresponding score from the guess,
            # we would be able to remove every possibility from the list of remaining possibilities

            # Append the worst score to the list of all worst scores
            # The highest value in this array is the worst case scenario,
            # where we would have the most options we would not be able to remove from our remaining
            # thus, the "inverse" of this is the max # we could remove in the worst case
            guess_worst.append(len(remaining_possibilities)-max(scores))
        else:
            # if the value was a previous guess, append -1 to the list of worst scores instead
            guess_worst.append(-1)

    # Combine the list of worst scores, and the list of possibilities into a dictionary
    # (i.e an array where each item another array containing a possibility and it's worst score)
    remaining_and_scores = dict(zip(possibilities, guess_worst))

    # Find the best score from the list of worst scores
    best_score = max(guess_worst)

    # Since multiple guesses may contain the best score, find the first score that is a valid guess and
    # has the best score, and return it
    for x in remaining_and_scores:
        if x in remaining_possibilities and remaining_and_scores[x] == best_score:
            return x
    # If we cannot find a guess that has the best score and is a valid guess, return the first guess
    # that has the best score instead
    for x in remaining_and_scores:
        if remaining_and_scores[x] == best_score:
            return x


# Works, all that's left is to extend to arbitrary number of pegs(i.e calculate first guess algorithmically)
pegs = 9

guess_length = 4

# Take all possible guesses (0000,0001,0002 ... , xxxx)
guess_values = [x for x in range(1, int(pegs)+1)]
all_possibilities = itertools.product(guess_values, repeat=int(guess_length))

# Move the list of all possible into 2 separate arrays
current_possibilities = list(all_possibilities)

# Calculate Best possible first guess (4,6 pegs defaults to 1,1,2,2 10,3 is 1,2,3 and 4,9 is 1,2,3,4)
previous_guess = []
print("Calculating best guess, this may take awhile for a large guess:")
current_guess = mini_max(current_possibilities, current_possibilities, previous_guess)


# Remove the first guess from the possibilities (if it's right the game would end anyways)
current_possibilities.remove(current_guess)

# Until Found right guess (Guaranteed in 5 for 6 pegs)
while True:
    # Print the current possibility to guess
    print("Guess: " + str(current_guess))
    # Add that guess to the list of previous guesses
    previous_guess.append(current_guess)
    # Store the current possibilities while doing things
    current_possibilities_storage = list(current_possibilities)
    # Get number of hits from user (correct position and color)
    guess_hits = input("Input number of hits: ")
    # End if guess is correct
    if int(guess_hits) == 4:
        break
    # Input number of close misses (correct color wrong position)
    misses = input("Input number of misses: ")

    # Remove all impossible Guesses
    current_possibilities = find_remaining(current_guess, int(guess_hits), int(misses), current_possibilities_storage)

    # Find Best option to guess next
    current_guess = mini_max(list(all_possibilities), current_possibilities, previous_guess)

