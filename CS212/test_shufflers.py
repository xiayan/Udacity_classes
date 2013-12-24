#!/usr/bin/python
from random import randrange
from collections import defaultdict

def shuffle2(deck):
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = randrange(N), randrange(N)
        swapped[i] = True
        swap(deck, i, j)

def shuffle3(deck):
    N = len(deck)
    for i in range(N):
        swap(deck, i, randrange(N))

def swap(deck, i, j):
        deck[i], deck[j] = deck[j], deck[i]

def test_shuffler(shuffler, deck = 'abcd', n = 20000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1

    e = n * 1.0 / factorial(len(deck))
    ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
    name = shuffler.__name__
    print '%s(%s) %s' %(name, deck, ('ok' if ok else '*** BAD ***'))
    print '     ',
    for item, count in sorted(counts.items()):
        print "%s:%4.1f" %(item, count*100./n),
    print

def test_shufflers(shufflers=[shuffle2, shuffle3], decks=['abcd', 'abc']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n * factorial(n - 1)

test_shufflers()