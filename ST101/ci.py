from math import sqrt

def mean(L):
    N = len(L) + 0.0
    return sum(L)/N

def std(L):
    u = mean(L)
    return sqrt(sum([(a - u) ** 2 for a in L])/len(L))

def main():
    a = 1.96
    number_list = [0.79, 0.70, 0.73, 0.66, 0.65, 0.70, 0.74, 0.81, 0.71, 0.70]
    N = len(number_list)
    u = mean(number_list)
    v = std(number_list)
    ci = a * v / sqrt(N)
    print u, v, ci
    return (u - ci, u + ci)

print main()