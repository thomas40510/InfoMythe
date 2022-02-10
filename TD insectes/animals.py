from numpy.random import randint
import sys
from ecosys import *


class Animal:
    """
    Un animal quelconque
    """

    def __init__(self, x, y, capacity=20, ecosysteme=Ecosystem, thinkOutLoud=False, cageSize=(30, 20)):
        self._max = capacity
        self._sante = randint(capacity // 2, capacity)
        self.__coords = (x, y)
        self._boundaries = cageSize
        self.eco = ecosysteme
        self._sayThoughts = thinkOutLoud

    @property
    def coords(self):  # lecture des coordonnées
        return self.__coords

    @coords.setter
    def coords(self, val):  # écriture des coordonnées
        maxX, maxY = self._boundaries
        x, y = val
        if x < 0:
            x = 0
        elif x > maxX:
            x = maxX
        if y < 0:
            y = 0
        elif y > maxY:
            y = maxY
        self.__coords = (x, y)

    pass

    @property
    def x(self):  # lecture de l'abscisse
        return self.__coords[0]

    @property
    def y(self):  # lecture de l'ordonnée
        return self.__coords[1]

    @property
    def sante(self):  # lecture de la santé
        return self._sante

    @sante.setter
    def sante(self, value):
        self._sante = value
        pass

    def car(self):
        return 'A'

    def manger(self):
        """
        Pour votre santé, pratiquez une activité physique régulière
        """
        self.sante -= 1
        if self.x % 5 == 0 and self.y % 5 == 0:
            self.sante = self._max
            self.think("Je mange...")
        elif self.sante <= 0:
            self.think("Je meurs de faim !")

    def bouger(self):
        self.coords = (self.coords[0] + randint(-3, 4), self.coords[1] + randint(-3, 4))

    def think(self, val: str):
        if self._sayThoughts:
            print(val)
        else:
            pass

    def __str__(self):
        return f"{self.car()} : pos {self.coords} state {self._sante} / {self._max}"

    def unTour(self):
        self.manger()
        self.bouger()


class Fourmi(Animal):
    """
    Un animal de type fourmi
    """

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, 20)

    def car(self):
        return 'F'

    # def manger(self):
    #     self.sante -= 1
    #     if self.sante < 4:
    #         self.sante = 20
    def bouger(self):
        s = self.sante
        x, y = self.coords
        if s >= 3:
            self.coords = (self.coords[0] + randint(-3, 4), self.coords[1] + randint(-3, 4))
        else:
            if x % 5 == 1:
                newx = x + 1
            elif x % 5 == 0:
                newx = x
            else:
                newx = x - 1

            if y % 5 == 1:
                newy = y + 1
            elif y % 5 == 0:
                newy = y
            else:
                newy = y - 1

            self.coords = (newx, newy)


class Cigale(Animal):
    """
    Un animal du type des cigale
    """
    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, 20)
        self.sante = 20

    def car(self):
        return 'C'

    def bouger(self):
        x, y = self.coords
        n = randint(0, 3)
        if n == 0:
            self.think("Je chante")
        elif n == 1:
            self.think("Je danse")
        elif n == 2:
            if x % 5 == 1:
                newx = x + 1
            elif x % 5 == 0:
                newx = x
            else:
                newx = x - 1

            if y % 5 == 1:
                newy = y + 1
            elif y % 5 == 0:
                newy = y
            else:
                newy = y - 1

            self.coords = (newx, newy)

    # def manger(self):
    #     n = randint(0, 3)
    #     self.sante -= 1
    #     if self.sante > 0:
    #         if self.sante <= 0:
    #             print("Je meurs de faim !")
    #         if n == 0:
    #             print("Je chante")
    #         elif n == 1:
    #             print("Je danse")
    #         elif n == 2:
    #             self.sante = 20


if __name__ == '__main__':
    ecosys = []
    nbins = int(sys.argv[1])
    nbtour = int(sys.argv[2])
    for i in range(nbins):
        if randint(0, 2) == 0:
            ecosys.append(Fourmi(randint(-10, 42), randint(-10, 42)))
        else:
            ecosys.append(Cigale(randint(-10, 42), randint(-10, 42)))
    for t in range(nbtour):
        print(f"### tour {t} ###")
        for ins in ecosys:
            ins.unTour()
            print(ins)
