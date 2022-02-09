from animals import *
from random import randint
import sys


class Ecosystem(list):
    """
    Constitue un écosystème et le peuple d'insectes
    """
    def __init__(self, nbins, nbsim, width, height):
        super().__init__()
        self.nbtour = nbsim
        self.__xmax = width
        self.__ymax = height
        for i in range(nbins):
            if randint(0, 2) == 0:
                self.append(Fourmi(randint(-10, 42), randint(-10, 42)))
            else:
                self.append(Cigale(randint(-10, 42), randint(-10, 42)))

    @property
    def dim(self):
        return self.__xmax, self.__ymax

    def unTour(self):
        for animal in self:
            animal.bouger()
            animal.manger()

    def simuler(self):
        for t in range(self.nbtour):
            self.unTour()

    # def __str__(self): # sans couleurs
    #     x, y = self.dim
    #     tmpcoord = []
    #     tmpcar = []
    #     R = ''
    #     for animal in ecosys:
    #         tmpcoord.append(animal.coords)
    #         tmpcar.append(animal.car())
    #     for i in range(x):
    #         T = ''
    #         for j in range(y):
    #             if (i, j) in tmpcoord:
    #                 res = tmpcar[tmpcoord.index((i, j))]
    #             else:
    #                 res = '.'
    #             if i % 5 == 0 and j % 5 == 0:
    #                 res += 'X'
    #             else:
    #                 res += '.'
    #             T += f'{res} '
    #         R += f'{T} \n'
    #     return R

    def __str__(self):  # coloré
        x, y = self.dim
        tmpcoord = []
        tmpcar = []
        R = ''
        for animal in ecosys:
            tmpcoord.append(animal.coords)
            tmpcar.append(animal.car())
        for i in range(x):
            T = ''
            for j in range(y):
                if (i, j) in tmpcoord:
                    res = tmpcar[tmpcoord.index((i, j))]
                else:
                    res = '.'
                if i % 5 == 0 and j % 5 == 0:
                    res = u'\x1b[102;31m' + res + u'\x1b[0m'
                else:
                    res = u'\x1b[43;31m' + res + u'\x1b[0m'
                T += f'{res} '
            R += f'{T} \n'
        return R


if __name__ == '__main__':
    nbins = 60
    nbtour = 50
    ecosys = Ecosystem(nbins, nbtour, 30, 20)
    print(ecosys)
    ecosys.simuler()
    print(ecosys)
