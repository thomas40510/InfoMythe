import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.stats as stats
import numpy.random as rnd

x = 1 - stats.expon(scale=2.).cdf(5)
print(x)


# pdf of exponential distribution
def pdf_exp(x, lam):
    return lam * np.exp(-lam * x)


# cdf of exponential distribution
def cdf_exp(x, mean):
    return 1 - np.exp(-x / mean)


y = 1 - cdf_exp(5, 2)
print(y)

B = rnd.exponential(1, size=(42000,))  # 42000 random numbers from an exponential distribution
Bm = B - np.mean(B)  # mean-free B
Bi = abs(Bm) > 3  # indices of values > 3 from the mean-free distribution
p = sum(Bi) / 42000  # probability of exceeding 3
print(p)


# pdf of normal distribution
def pdf_norm(x, mean, std):
    return 1 / (np.sqrt(2 * np.pi) * std) * np.exp(-0.5 * ((x - mean) / std) ** 2)


# cdf of normal distribution
def cdf_norm(x, mean, std):
    return sp.stats.norm.cdf(x, loc=mean, scale=std)


# 4  subplots of normal distribution pdf varying mean and std
# varying mean
x = np.linspace(-7, 7, 100)
plt.figure(figsize=(5, 5))
for i in range(4):
    # mean varies
    plt.subplot(4, 2, i + 1)
    plt.plot(x, pdf_norm(x, 0, 1), 'r--')
    plt.plot(x, pdf_norm(x, i, 1))
    plt.title('mean = ' + str(i))
    plt.xlabel('x')
    plt.ylabel('pdf')
for i in range(4):
    # std varies
    plt.subplot(4, 2, i + 5)
    plt.plot(x, pdf_norm(x, 0, 1), 'r--')
    plt.plot(x, pdf_norm(x, 0, i+1))
    plt.title('std = ' + str(i))
    plt.xlabel('x')
    plt.ylabel('pdf')
plt.show()


# pdf of binomial distribution
def pdf_bin(n, p, k):
    return stats.binom.pmf(k, n, p)


# cdf of binomial distribution
def cdf_bin(n, p, k):
    return stats.binom.cdf(k, n, p)


# plot of binomial distribution cdf varying p only
n = 50
x = np.arange(0, n)
plt.figure(figsize=(5, 5))
for i in range(8):
    # p varies
    plt.subplot(4, 2, i + 1)
    plt.plot(x, cdf_bin(n, i / 10, x), 'r--')
    plt.plot(x, cdf_bin(n, i / 10, x))
    plt.title('p = ' + str(i / 10))
    plt.xlabel('x')
    plt.ylabel('cdf')
plt.show()


# poisson distribution pdf
def pdf_poi(x, mean):
    return stats.poisson.pmf(x, mean)


# poisson distribution cdf
def cdf_poi(x, mean):
    return stats.poisson.cdf(x, mean)


# compare pdf of binom(50,.1) and poisson(5) on same graph
k = np.arange(0, 50)
plt.figure(figsize=(5, 5))
plt.plot(k, pdf_bin(50, .1, k), 'r--')
plt.plot(k, pdf_poi(k, 5))
plt.xlabel('k')
plt.ylabel('pdf')
plt.show()


z = np.arange(.01, 20, .01)
fX = pdf_exp(z, 1)
FX = cdf_exp(z, 1)
fZ = 3 * fX * (FX ** .5)

plt.plot(z, fZ)
plt.show()
