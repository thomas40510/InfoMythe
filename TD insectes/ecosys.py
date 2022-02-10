import platform

from animals import *
from random import randint
import sys
import time


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
                self.append(Fourmi(randint(-10, 42), randint(-10, 42), cageSize=self.dim))
            else:
                self.append(Cigale(randint(-10, 42), randint(-10, 42), cageSize=self.dim))

    @property
    def dim(self):
        return self.__xmax, self.__ymax

    def unTour(self):
        for animal in self:
            animal.bouger()
            animal.manger()

    def simuler(self, showUpdates=False):
        """
        Exécution de la simulation complète
        :param showUpdates: affichage de la grille à chaque étape
        """
        for t in range(self.nbtour):
            self.unTour()
            if showUpdates:
                print(f"%%% Tour {t} / {self.nbtour} %%%")
                print(self, end="\r", flush=True)
                time.sleep(1)

    def strStd(self):
        """
        Affichage de la grille de manière standard (sans couleurs) dans la console
        """
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
                    res += 'X'
                else:
                    res += '.'
                T += f'{res} '
            R += f'{T} \n'
        return R

    def strColor(self):
        """
        Affichage de la grille dans la console, avec des couleurs
        """
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

    def __str__(self):
        """
        Affiche la grille, avec ou sans couleurs en fonction de l'OS
        """
        return self.strColor() if platform.system() in ('Darwin', 'Linux') else self.strStd()


if __name__ == '__main__':
    nbins = 60
    nbtour = 50
    ecosys = Ecosystem(nbins, nbtour, 10, 10)
    print(ecosys)
    ecosys.simuler(showUpdates=True)
    # print(ecosys)
