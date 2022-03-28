from numpy.random import randint
import sys
from ecosys import *
from abc import *


class Animal:
    """
    Un animal quelconque
    """

    def __init__(self, x: int, y: int, capacity=20, ecosysteme=None, thinkOutLoud=False, cageSize=(30, 20)):
        """Naissance de l'animal

        :type ecosysteme: Ecosystem
        :param x: abscisse de départ
        :param y: ordonnée de départ
        :param capacity: santé maximale
        :param ecosysteme: écosystème de rattachement de l'insecte
        :param thinkOutLoud: L'insecte dit ce qu'il pense
        :param cageSize: Taille de la cage (deprecated, gardé pour compatibilité)
        """
        self._max = capacity
        self._sante = randint(capacity // 2, capacity)
        self.__coords = (x, y)
        self._boundaries = ecosysteme.dim
        self._ecosys = ecosysteme
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
    def x(self):
        """Lecture de l'abscisse"""
        return self.__coords[0]

    @property
    def y(self):
        """Lecture de l'ordonnée"""
        return self.__coords[1]

    @property
    def sante(self):
        """Lecture de la santé de l'animal"""
        return self._sante

    @sante.setter
    def sante(self, value):
        """Modification de la santé

        :param value: nouvelle valeur de santé de l'animal
        """
        self._sante = value
        pass

    def car(self):
        return 'A'

    def manger(self):
        """Pour votre santé, pratiquez une activité physique régulière

        https://www.mangerbouger.fr/
        """
        currX, currY = self.coords
        self.sante -= 1
        # if self.x % 5 == 0 and self.y % 5 == 0:
        if self._ecosys.case(currX, currY) == 1:
            self.sante = self._max
            self.think("Je mange...")
        elif self.sante <= 0:
            self.think("Je meurs de faim !")

    @abstractmethod
    def bouger(self):
        # self.coords = (self.coords[0] + randint(-3, 4), self.coords[1] + randint(-3, 4))
        pass

    def moveRnd(self):
        """Mouvement aléatoire"""
        oldXY = self.coords
        while self.x < 0 or self.y < 0:
            self.coords = (oldXY[0] + randint(-3, 4), oldXY[1] + randint(-3, 4))

    def moveNour(self):
        """Se déplace vers la nourriture la plus proche dans un rayon de 4"""
        prox = self._ecosys.vue(self.x, self.y, 4)
        mvX = 0
        mvY = 0
        for el in prox:
            if el[2] == 1:
                dX = el[0] - self.x
                dY = el[1] - self.y
                if dX != 0:
                    mvX = int(dX/abs(dX))
                if dY != 0:
                    mvY = int(dY/abs(dY))
        self.coords = (self.x + mvX, self.y + mvY)

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
        """Joue un tour de simulation"""
        self.manger()
        self.bouger()


class Fourmi(Animal):
    """
    Un animal de type fourmi
    """

    def __init__(self, x, y, **kwargs):
        """Naissance d'une fourmi

        :param x: abscisse de départ
        :param y: ordonnée de départ
        """
        super().__init__(x, y, 20, **kwargs)

    def car(self):
        """Définit le type de l'animal

        :return : l'animal est une fourmi, son type est 'F'
        """
        return 'F'

    def bouger(self):
        """Déplacement de la fourmi.

        Si elle a faim, elle se rapproche de la nourriture. Sinon, elle bouge aléatoirement.
        """
        s = self.sante
        # x, y = self.coords
        if s >= 3:
            self.moveRnd()
        else:
            self.moveNour()
            # if x % 5 == 1:
            #     newx = x + 1
            # elif x % 5 == 0:
            #     newx = x
            # else:
            #     newx = x - 1
            #
            # if y % 5 == 1:
            #     newy = y + 1
            # elif y % 5 == 0:
            #     newy = y
            # else:
            #     newy = y - 1

            # self.coords = (newx, newy)


class Cigale(Animal):
    """
    Un animal du type des cigales
    """
    def __init__(self, x, y, cap=20, **kwargs):
        """Naissance de la cigale

        :param x: abscisse d'origine
        :param y: ordonnée d'origine
        :param cap: santé maximale
        """
        super().__init__(x, y, 20, **kwargs)
        self.sante = cap

    def car(self):
        """Définit le type de l'insecte

        :return : c'est une cigale, son type est 'C'
        """
        return 'C'

    def bouger(self):
        """Déplacement de la cigale.

        Une chance sur trois de se déplacer. Sinon, soit elle chante soit elle danse.
        Si elle se déplace, elle se rapproche de la nourriture si elle a faim. Sinon, déplacement aléatoire.
        """
        x, y = self.coords
        n = randint(0, 3)
        if n == 0:
            self.think("Je chante")
        elif n == 1:
            self.think("Je danse")
        elif n == 2:
            if self.sante >= 7:
                self.moveRnd()
            else:
                self.moveNour()
            # if x % 5 == 1:
            #     newx = x + 1
            # elif x % 5 == 0:
            #     newx = x
            # else:
            #     newx = x - 1
            #
            # if y % 5 == 1:
            #     newy = y + 1
            # elif y % 5 == 0:
            #     newy = y
            # else:
            #     newy = y - 1

            # self.coords = (newx, newy)


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
