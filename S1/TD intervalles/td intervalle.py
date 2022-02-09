import numpy as np


class Interval:
    def __init__(self, a=-np.inf, b=np.inf):
        if a <= b:
            self.inf, self.sup = a, b
        else:
            self.inf, self.sup = b, a

    def __add__(self, other):
        return Interval(self.inf + other.inf, self.sup + other.sup)

    def __sub__(self, other):
        return Interval(self.inf - other.inf, self.sup - other.sup)

    def __mul__(self, other):
        res = Interval()
        a, b = self.inf, self.sup
        c, d = other.inf, other.sup
        res.inf = min(a * c, a * d, b * c, b * d)
        res.sup = max(a * c, a * d, b * c, b * d)
        return res

    def __truediv__(self, other):
        c, d = other.inf, other.sup
        if 0 not in other:
            tmp = Interval(1 / d, 1 / c)
            return self * tmp
        else:
            raise ArithmeticError('Dividing by interval containing 0')

    def __pow__(self, power, modulo=None):
        if power > 0:
            return Interval(pow(self.inf, power), pow(self.sup, power))
        else:
            raise Exception('Applying negative power to interval')  # TODO : implémenter puissance négative

    def __neg__(self):
        return Interval(-self.sup, -self.inf)

    def __eq__(self, other):
        return self.inf == other.inf and self.sup == other.sup

    def __contains__(self, item):
        return self.inf <= item <= self.sup

    def __str__(self):
        return "[" + str(self.inf) + " ; " + str(self.sup) + "]"

    def __len__(self):
        return abs(self.sup - self.inf)

    def width(self):
        '''
        Evaluates width of the Interval
        :return:
        '''
        return len(self)

    def mid(self):
        '''
        Evaluates mean value of Interval
        :return:
        '''
        return .5 * (self.sup + self.inf)


def exp(x: Interval):
    '''
    Calculates the exponential of an Interval
    :param x: interval [a,b]
    :return: [exp(a), exp(b)]
    '''
    res = Interval(np.exp(x.inf), np.exp(x.sup))
    return res


def log(x: Interval):
    if x.inf > 0:
        res = Interval(np.log(x.inf), np.log(x.sup))
        return res
    else:
        raise ArithmeticError("Cannot apply log to negative numbers")


def sqrt(x: Interval):
    if x.inf >= 0:
        return x ** .5
    else:
        raise ArithmeticError('Cannot evaluate sqrt of negative number')


def branch_bound(I, f):
    L = [I]
    minf = np.inf
    while len(L) > 0:
        X = L.pop(0)
        a = f(X)
        if a.inf > minf - 1e-6:
            minX = X.inf
        else:
            z = Interval(X.mid(), X.mid())
            b = f(z).mid()
            if b < minf:
                minf = b
                minX = X.mid
            X1 = Interval(X.inf, X.mid())
            X2 = Interval(X.mid(), X.sup)
            L.append(X1)
            L.append(X2)
    return minf, minX


def branch_bound_2vars(I, J, f):  # TODO : MAKE IT WORK!!
    L = [I]
    M = [J]
    fmin = np.inf
    minX = L[0].inf
    minY = M[0].inf
    while len(L) != 0 or len(M) != 0:
        print(len(L), len(M))
        try:
            n = len(L[0])
        except:
            n = 0
        try:
            m = len(M[0])
        except:
            m = 0
        try:
            X = L[0]
        except:
            X = Interval(minX, minX)
        try:
            Y = M[0]
        except:
            Y = Interval(minY, minY)

        if n > m:
            X = L.pop(0)
            a = f(X, Y)
            if a.inf <= fmin - 1e-6:
                b = f(Interval(X.mid(), X.mid()), Interval(minY, minY)).mid()
                if b < fmin:
                    fmin = b
                    minX = X.mid()
                X1 = Interval(X.inf, X.mid())
                X2 = Interval(X.mid(), X.sup)
                L.append(X1)
                L.append(X2)
        else:
            Y = M.pop(0)
            a = f(X, Y)
            print("155: ",X,Y,a,fmin)
            if a.inf <= fmin - 1e-6:
                b = f(Interval(minX, minX), Interval(Y.mid(), Y.mid())).mid()
                print("158: ",b, fmin)
                if b < fmin:
                    fmin = b
                    minY = Y.mid()
                Y1 = Interval(Y.inf, Y.mid())
                Y2 = Interval(Y.mid(), Y.sup)
                M.append(Y1)
                M.append(Y2)
    return fmin, minX, minY


def f1(x: Interval):
    return x ** 5 + x + exp(x ** 2) - x * exp(x)


def f2(x: Interval, y: Interval):
    return (Interval(1, 1) - x) ** 2 + Interval(100, 100) * (y - x ** 2) ** 2


if __name__ == '__main__':
    x = Interval(2, 9)
    y = Interval(1, 5)
    # print(x, y)
    # print("+", x+y)
    # print("-", x-y)
    # print("*", x*y)
    # print("/", x/y)
    # print("exp", exp(x))
    # print("log", log(x))
    # print("\^n", pow(x,2))
    # print("sqrt", sqrt(x))
    I = Interval(0, 2)
    J = Interval(0, 2)
    # print(branch_bound(I, f1))
    print(branch_bound_2vars(I, J, f2))
