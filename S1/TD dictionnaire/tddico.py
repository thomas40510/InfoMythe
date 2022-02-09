"""
@author: Thomas PREVOST (FISE24) @ ENSTA B
@date: 11/10/2021
"""
import time

import numpy as np
import matplotlib.pyplot as plt


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


global fiboTerms
fiboTerms = {0: 0, 1: 1}


def fiboDic(n):
    global fiboTerms
    try:
        return fiboTerms[n]
    except:
        for i in range(len(fiboTerms), n + 1):
            fiboTerms[i] = fibo(i)
        return fiboTerms[n]


if __name__ == "__main__":
    N = 30
    dt = []
    n = [i for i in range(N)]
    for i in n:
        fiboTerms.clear()
        t0 = time.perf_counter()
        fiboDic(i)
        dt.append(time.perf_counter() - t0)

    dt2 = []
    fiboTerms.clear()
    for i in n:
        t0 = time.perf_counter()
        fiboDic(i)
        dt2.append(time.perf_counter() - t0)

    dt3 = []
    for i in n:
        t0 = time.perf_counter()
        fibonacci(i)
        dt3.append(time.perf_counter() - t0)

    plt.scatter(np.asarray(n), np.log(np.asarray(dt)),
                label='dico avec clear')
    plt.scatter(np.asarray(n), np.log(np.asarray(dt2)), color='red',
                label='dico sans clear')
    plt.scatter(np.asarray(n), np.log(np.asarray(dt3)), color='green',
                label='récursif sans dico')

    plt.xlabel('$n$')
    plt.ylabel('$\log(\Delta t)$')
    plt.legend()
    plt.title('temps de calcul comparé')
    plt.show()

    # t0 = []
    # t1 = []
    # n = []
    # for i in range(30):
    #     n.append(i)
    #     t0.append(time.perf_counter())
    #     fibonacci(i)
    #     t1.append(time.perf_counter())
    # plt.scatter(np.asarray(n), np.log(np.asarray(t1)-np.asarray(t0)))
    # plt.show()
