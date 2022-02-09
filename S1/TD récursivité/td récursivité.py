"""
@author: Thomas PREVOST (FISE24) @ ENSTA B
"""


def fact(n):
    if n == 1:
        return 1
    f = n * fact(n - 1)
    return f


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    f = fibonacci(n - 1) + fibonacci(n - 2)
    return f


def fibo(n, a=0, b=1):
    if n == 2:
        return a + b
    elif n == 0:
        return a
    elif n == 1:
        return b
    f = fibo(n - 1, b, a + b)
    return f


def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


def pgcd(a, b):
    if a < b:
        return pgcd(b, a)
    elif b == 0 or a == b:
        return a
    c = a % b
    res = pgcd(b, c)
    return res


def sumsq(n, mem):
    if n == 0:
        return mem
    for k in range(1, int(pow(n, .5)) + 1):
        if k not in mem:
            mem.add(k)
            tmp = sumsq(n-pow(k, 2), mem)
            if len(tmp) > 0:  # on a gagné !
                return tmp
            else:  # on a raté
                mem.remove(k)
    return set()


if __name__ == "__main__":
    # print(fact(10))
    # print(fibonacci(33))
    # print(fibo(92))
    # print(ack(2, 2))
    # print(pgcd(477865542, 717173730))
    d = sumsq(42, set())
    print(d)
