# ----------------
# User Instructions
#
# Modify the timedcalls(n, fn, *args) function so that it calls
# fn(*args) repeatedly. It should call fn n times if n is an integer
# and up to n seconds if n is a floating point number.

import itertools

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    print zebra_puzzle
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in cc(orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in cc(orderings)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in cc(orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in cc(orderings)
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in cc(orderings)
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

def instrument_fn(fn, *args):
    cc.starts, cc.items = 0, 0
    result = fn(*args)
    print '%s got %s with %5d iters over %7d items' % (fn.__name__, result, cc.starts, cc.items)

def cc(sequence):
    cc.starts += 1
    for item in sequence:
        cc.items += 1
        yield item

instrument_fn(zebra_puzzle)

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

#timedcall(zebra_puzzle)

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # Your code here.
    if isinstance(n, int):
        print zebra_puzzle.start
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)