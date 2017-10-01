def fib(n, k):
    x, y = 1, 1
    for i in range(2, n):
        x, y = y, k * x + y
    return y

data = ''

n, k = tuple([int(x) for x in data.split()])

print(fib(n, k))
