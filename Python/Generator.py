def DevisorsSum(k):
    sum = 0
    for i in range(1, k):
        if k % i == 0:
            sum += i
    return sum


def fn_generator(n):
    a = 1
    i = 0
    while i != n:
        for b in range(1, a):
            if (b == DevisorsSum(a)) & (a == DevisorsSum(b)):
                yield (b, a)
                i += 1
        a += 1