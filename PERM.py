def factorial(n):
    sm = 1
    for i in range(1, n+1):
        sm *= i
    return sm


def permute(a, k=0):
    if k == len(a):
        print(' '.join([str(x) for x in a]))
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            permute(a, k+1)
            a[k], a[i] = a[i], a[k]

data = 6
print(factorial(data))
permute(list(range(1, data+1)))
