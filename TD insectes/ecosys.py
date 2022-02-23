import platform

from animals import *
from random import randint
import sys
import time


class Ecosystem(list):
    """
    Constitue un écosystème et le peuple d'insectes
    """

    def __init__(self, nbins, nbsim, width, height, nbNour=6):
        super().__init__()
        self.nbtour = nbsim
        self.__xmax = width
        self.__ymax = height
        if nbNour > width * height:
            raise ValueError
        plateau = self.genNour(nbNour)
        self.__plateau = plateau
        for i in range(nbins):
            if randint(0, 2) == 0:
                self.append(Fourmi(randint(-10, 42), randint(-10, 42), cageSize=self.dim))
            else:
                self.append(Cigale(randint(-10, 42), randint(-10, 42), cageSize=self.dim))

    @property
    def dim(self):
        return self.__xmax, self.__ymax

    def genNour(self, nbNour):
        x, y = self.dim
        plateau = x*[y*[0]]
        for n in range(nbNour):
            (nourX, nourY) = (randint(0, x-1), randint(0, y-1))
            while plateau[nourX][nourY] == 1:
                (nourX, nourY) = (randint(0, x - 1), randint(0, y - 1))
            plateau[nourX][nourY] = 1
        return plateau

    def case(self, x, y):
        return self.__plateau[x][y]

    def vue(self, x, y, r):
        l = []
        for (a, b) in self.dim:
            dist = pow(pow(x-a, 2) + pow(y-b, 2), .5)
            if dist <= r:
                l.append([a, b])
        return l

    def unTour(self):
        for animal in self:
            animal.bouger()
            animal.manger()
        self.enterrer()

    def simuler(self, showUpdates=False):
        """
        Exécution de la simulation complète
        :param showUpdates: affichage de la grille à chaque étape
        """
        for t in range(self.nbtour + 1):
            self.unTour()
            if showUpdates:
                print(f"%%% Tour {t} / {self.nbtour} %%%")
                print(self, end="\r", flush=True)
                # time.sleep(1)

    def enterrer(self):
        """Identifie les cadavres et les enterre
        """
        dead = []
        for i in range(len(self) - 1, -1, -1):
            if self[i].sante == 0:
                dead.append(i)
        for j in dead:
            self.pop(j)
        # print(f'//// Removed {len(dead)} cadaver(s) from ecosys ////')

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
