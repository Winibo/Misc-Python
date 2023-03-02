import matplotlib.pyplot as plt
import collections
import itertools
from scipy.stats import norm
from math import sqrt
import numpy as np

dice = input("Input number of dice:")
maxvalue = input("Input Highest Value for ONE die:")


def predict_odds_of_one(dice_number, maximum, goal):
    dice_rolls = [x for x in range(1, maximum + 1)]
    totals = collections.Counter(sum(x) for x in itertools.product(dice_rolls, repeat=dice_number))
    combination_number = totals[goal]
    return combination_number


def most_likely(dice_number, maximum):
    dice_rolls = [x for x in range(1, maximum+1)]
    totals = collections.Counter(sum(x) for x in itertools.product(dice_rolls, repeat=dice_number))
    totals = dict(totals)
    rolls = list(totals.keys())
    occurrences = list(totals.values())
    proportions = [x / (maximum ** dice_number) for x in occurrences]
    return rolls, occurrences, proportions

# Deprecated version only to be used for testing
# def deprecated_most_likely(dice_number, maximum):
#    x = range(dice_number, (maximum*dice_number)+1)
#    total = [[], []]
#    for x in x:
#        total[0].append(x+maximum)
#        total[1].append(predict_odds_of_one(dice_number, maximum, x))
#    return total

# Labels bars with their heights in a bar graph automatically
# def auto_label(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate(str(round(float('{}'.format(height)), 4)),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')


data = most_likely(int(dice), int(maxvalue))
# data2 = deprecated_most_likely(7, 8)
fig, ax = plt.subplots()
# rect0 = ax.bar(data2[0], data2[1])
rect1 = ax.hist(data[0], bins=len(data[1]), weights=data[2])
# auto_label(rect1)


# Calculate Mean and Standard Deviation, since the data is already binned
mu = sum([x*data[1][data[0].index(x)] for x in data[0]])/sum(data[1])
std = sqrt(sum([((x - mu)**2)*data[1][data[0].index(x)] for x in data[0]])/sum(data[1]))
# Plot the PDF. Taken from https://stackoverflow.com/questions/20011122/fitting-a-normal-distribution-to-1d-data
x_min, x_max = plt.xlim()
x = np.linspace(x_min, x_max, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)
plt.show()
print(data[1])
print(int(maxvalue) ** int(dice))
input("Hit enter to exit")
