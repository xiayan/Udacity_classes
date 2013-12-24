def mean(L):
    N = len(L) + 0.0
    return sum(L)/N

def main():
    x = [0, 1, 2]
    y = [0, 2, 2]
    u_x = mean(x)
    u_y = mean(y)

    var_x, cov = 0.0, 0.0
    for i in range(len(x)):
        m = x[i] - u_x
        n = y[i] - u_y
        var_x += m ** 2
        cov += m * n

    b = cov / var_x
    a = u_y - b * u_x

    return a, b

print main()