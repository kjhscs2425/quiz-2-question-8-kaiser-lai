import random
"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""

# YOUR CODE HERE

first = ["c","t","b"]
second =["a","o"]
third = ["p","t","n"]
word = []
for f in first:
    for s in second:
        for t in third:
            word.append(f + s + t)

for word in (word):
    print(word)