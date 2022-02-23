from numpy.random import randint
import sys
from ecosys import *
from abc import *


class Animal:
    """
    Un animal quelconque
    """

    def __init__(self, x, y, capacity=20, ecosysteme=None, thinkOutLoud=False, cageSize=(30, 20)):
        """
        :type x: int
        :type y: int
        :type capacity: int
        :type ecosysteme: Ecosystem
        :type cageSize: (int, int)
        :type thinkOutLoud: bool
        :param x: abscisse de départ
        :param y: ordonnée de départ
        :param capacity: santé maximale
        :param ecosysteme: écosystème de rattachement de l'insecte
        :param thinkOutLoud: L'insecte dit ce qu'il pense
        :param cageSize: Taille de la cage (défini par l'écosystème)
        """
        self._max = capacity
        self._sante = randint(capacity // 2, capacity)
        self.__coords = (x, y)
        if ecosysteme is not None:
            self._boundaries = ecosysteme.dim()
        else:
            self._boundaries = cageSize
        self._sayThoughts = thinkOutLoud

    @property
    def coords(self):
        """ Lecture des coordonnées
        :return : le tuple (x, y) des coordonnées de l'animal
        """
        return self.__coords

    @coords.setter
    def coords(self, val):
        """ Écriture des coordonnées
        :param val: tuple (x, y) des coordonnées à écrire.
        """
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

    @abstractmethod
    def bouger(self):
        # self.coords = (self.coords[0] + randint(-3, 4), self.coords[1] + randint(-3, 4))
        pass

    def moveRnd(self):
        self.coords = (self.coords[0] + randint(-3, 4), self.coords[1] + randint(-3, 4))

    def think(self, val: str):
        """ Pensées de l'insecte. Ne parle que si on lit dans ses pensées.
        :param val: Contenu de la pensée
        """
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
    """ Un animal de type fourmi
    :param x: abscisse initiale
    :param y: ordonnée initiale
    """

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, 20)

    def car(self):
        """Définit le type de l'animal
        :return 'F': l'animal est une fourmi, son type est 'F'
        """
        return 'F'

    # def manger(self):
    #     self.sante -= 1
    #     if self.sante < 4:
    #         self.sante = 20
    def bouger(self):
        """Déplacement de la fourmi
        """
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
    def __init__(self, x, y, cap=20, **kwargs):
        super().__init__(x, y, 20, **kwargs)
        self.sante = cap

    def car(self):
        return 'C'

    def bouger(self, alea=False):
        if alea:
            self.moveRnd()
        else:
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
