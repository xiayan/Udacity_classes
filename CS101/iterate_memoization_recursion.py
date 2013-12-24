#!/usr/bin/python

#Rabbits Multiplying

#A (slightly) more realistic model of rabbit multiplication than the Fibonacci
#model, would assume that rabbits eventually die. For this question, some
#rabbits die from month 6 onwards.
#
#Thus, we can model the number of rabbits as:
#
#rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
#rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
#For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
#rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
#For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
#rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
#This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
#Define a procedure rabbits that takes as input a number n, and returns a
#number that is the value of the nth number in the rabbit sequence.
#For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)
import time

def rabbits(n):
    result = [0, 1, 1, 2, 3]
    if n <= 4:
        return result[n]
    for _ in range(n - 4):
        result.append(result[-1] + result[-2] - result.pop(0))
    return result[-1]

def rab(n, rdict):
    if n in rdict:
        return rdict[n]
    if n < 1:
        rdict[n] = 0
        return 0
    else:
        if n == 1 or n == 2:
            rdict[n] = 1
            return 1
        else:
            rdict[n] = rab(n - 1, rdict) + rab(n - 2, rdict) - rab(n - 5, rdict)
            return rdict[n]
def rabb(n):
    if n < 1:
        return 0
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return rabb(n - 1) + rabb(n - 2) - rabb(n - 5)

def test():
    n = 25
    start1 = time.clock()
    rabbits(n)
    print time.clock() - start1

    start2 = time.clock()
    memodict = {}
    rab(n, memodict)
    print time.clock() - start2

    start3 = time.clock()
    rabb(n)
    print time.clock() - start3

test()

