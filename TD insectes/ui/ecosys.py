import platform

from animals import *
from random import randint
import sys
import time


class Ecosystem(list):
    """
    Constitue un écosystème et le peuple d'insectes
    """

    def __init__(self, nbins: int, nbsim: int, width: int, height: int, nbNour=6):
        """ Création de l'écosystème

        :param nbins: nombre d'insectes à créer
        :param nbsim: nombre de tours de simulation
        :param width: largeur du plateau
        :param height: hauteur du plateau
        :param nbNour: quantité de nourriture à générer
        """
        super().__init__()
        self.nbtour = nbsim
        self.__xmax = width
        self.__ymax = height
        if nbNour > width * height:
            raise ValueError
        plateau = self.genNour(nbNour)
        self.__plateau = plateau
        for insect in range(nbins):
            if randint(0, 2) == 0:
                self.append(Fourmi(randint(0, width - 1), randint(0, height - 1), cageSize=self.dim, ecosysteme=self))
            else:
                self.append(Cigale(randint(0, width - 1), randint(0, height - 1), cageSize=self.dim, ecosysteme=self))

    @property
    def dim(self):
        """Dimensions (xmax, ymax) du plateau de jeu

        :return : longueur et hauteur maximales du plateau
        """
        return self.__xmax, self.__ymax

    def genNour(self, nbNour):
        """Génère la nourriture aléatoirement sur le plateau de jeu

        :param nbNour: quantité de nourriture à générer
        :return : plateau de jeu contenant la nourriture
        """
        x, y = self.dim
        plateau = []
        for i in range(x):
            tmp = []
            for j in range(y):
                tmp.append(0)
            plateau.append(tmp)
        for n in range(nbNour):
            (nourX, nourY) = (randint(0, x - 1), randint(0, y - 1))
            while plateau[nourX][nourY] == 1:
                (nourX, nourY) = (randint(0, x - 1), randint(0, y - 1))
            plateau[nourX][nourY] = 1
        return plateau

    def case(self, x: int, y: int):
        """Donne le contenu (nourriture ou non) d'une case donnée

        :param x: abscisse de la case à inspecter
        :param y: ordonnée de la case à instecter
        :return : 0 (pas de nourriture) ou 1 (nourriture)
        """
        return self.__plateau[x][y]

    def vue(self, x: int, y: int, r: int):
        """Détecte les cases situées à une certaine distance d'une case donnée

        :param x: abscisse de la case d'origine
        :param y: ordonnée de la case d'origine
        :param r: distance maximale
        :return : liste contenant les cases trouvées, et leur contenu (nourriture ou non)
        """
        l = []
        X, Y = self.dim
        for a in range(X):
            for b in range(Y):
                dist = pow(pow(x - a, 2) + pow(y - b, 2), .5)
                if dist <= r:
                    l.append([a, b, self.case(a, b)])
        return l

    def unTour(self):
        """Joue un tour de simulation"""
        for animal in self:
            animal.bouger()
            animal.manger()
        self.enterrer()

    def simuler(self, showUpdates=False):
        """Exécution de la simulation complète

        :param showUpdates: affichage de la grille à chaque étape
        """
        for time in range(self.nbtour + 1):
            self.unTour()
            if showUpdates:
                print(f"%%% Tour {time} / {self.nbtour} %%%")
                print(self, end="\r", flush=True)
                # time.sleep(1)

    def enterrer(self):
        """
        Identifie les cadavres et les enterre
        """
        dead = []
        for i in range(len(self) - 1, -1, -1):
            if self[i].sante == 0:
                dead.append(i)
        for j in dead:
            self.pop(j)
        # print(f'//// Removed {len(dead)} cadaver(s) from ecosys ////')

    def strStd(self):
        """Affichage de la grille de manière standard (sans couleurs) dans la console

        :return : la grille textuelle
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
        """Affichage de la grille dans la console, avec des couleurs

        :return : la grille en couleur
        """
        x, y = self.dim
        tmpcoord = []
        tmpcar = []
        R = ''
        for animal in self:
            tmpcoord.append(animal.coords)
            tmpcar.append(animal.car())
        for i in range(x):
            T = ''
            for j in range(y):
                if (i, j) in tmpcoord:
                    res = tmpcar[tmpcoord.index((i, j))]
                else:
                    res = '.'
                # if i % 5 == 0 and j % 5 == 0:
                if self.case(i, j) == 1:
                    res = u'\x1b[102;31m' + res + u'\x1b[0m'
                else:
                    res = u'\x1b[43;31m' + res + u'\x1b[0m'
                T += f'{res} '
            R += f'{T} \n'
        return R

    def __str__(self):
        """Affiche la grille, avec ou sans couleurs en fonction de l'OS

        :return: un plateau coloré sous Linux et MacOS, un plateau textuel sinon
        """
        return self.strColor() if platform.system() in ('Darwin', 'Linux') else self.strStd()


if __name__ == '__main__':
    nbins = 60
    nbtour = 50
    ecosys = Ecosystem(nbins, nbtour, 10, 10, 7)
    print(ecosys)
    ecosys.simuler(showUpdates=True)
    # print(ecosys)
