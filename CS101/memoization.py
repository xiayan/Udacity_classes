#!/usr/bin/python
#[Double Gold Star] Memoization is a way to make code run faster by saving
#previously computed results.  Instead of needing to recompute the value of an
#expression, a memoized computation first looks for the value in a cache of pre-
#computed values.

#Define a procedure, cached_execution(cache, code), that takes in two inputs: a
#cache, which is a Dictionary that maps strings representing Python expressions
#to their previously computed values, and code, a string that is a Python
#expression.  Your procedure should return the value of code, but should only
#evaluate code if it has not been previously evaluated.

def cached_execution(cache,code):
    if code not in cache:
        cache[code] = eval(code)
    return cache[code]

#Here is an example showing the desired behavior of cached_execution:

def factorial(n):
    print "Running factorial:", n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


#Here is a more interesting example using cached_execution
#(do not worry if you do not understand this, though,
#it will be more clear after Unit 6):

def cached_fibo(cache, n):
    if n == 1 or n == 0:
        return n
    else:
        return cached_execution(cache, 'cached_fibo(cache, ' + str(n - 1) + ')') \
               + cached_execution(cache, 'cached_fibo(cache, ' + str(n - 2) + ')')

cache = {}

# do not try this at home...at least without a cache!
print cached_execution(cache, 'cached_fibo(cache, 200)')

#Hint: you will need to use the built-in eval function similarly to how we used
#it in time_execution.  The eval function takes a string as input, and returns
#the result of evaluating that string as a Python expression.
