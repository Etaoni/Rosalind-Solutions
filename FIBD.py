def fibd(n, m):
    rabbit_count = [0, 1, 1]
    for i in range(3, n+2):
        s = 0
        for j in range(i - m, i - (1+1) + 1):
            if j > 0:
                s += rabbit_count[j]
        rabbit_count.append(s)
    return rabbit_count[-1]

print(fibd(99, 20))
