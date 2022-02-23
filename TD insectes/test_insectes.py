import unittest
from ecosys import *
from animals import *


class TestAnimal(unittest.TestCase):
    def test_init_animal(self):
        """Tests unitaires sur la classe Animal
        """
        x = 4
        y = 2
        cap = 30
        cage = (20, 50)
        anim = Animal(x, y, cap, cageSize=cage)
        self.assertEqual(anim.coords, (x, y))
        self.assertEqual(anim._boundaries, cage)
        self.assertTrue(cap//2 <= anim._sante <= cap)
        self.assertEqual(type(anim), Animal)

    def test_cigale(self):
        """Tests unitaires sur la cigale
        """
        x = 4
        y = 2
        cap = 20
        cage = (20, 50)
        cig = Cigale(x, y, cageSize=cage)
        self.assertEqual(cig.coords, (x, y))
        self.assertEqual(cig._max, cap)
        self.assertEqual(cig._sante, cap)
        self.assertEqual(cig._boundaries, cage)
        self.assertEqual(type(cig), Cigale)
        self.assertTrue(type(cig) != Animal and type(cig) != Fourmi)

    def test_coords(self):
        """Tests unitaires sur les coordonnées de deux insectes
        """
        x = 4
        y = 2
        cage = (20, 30)
        cig = Cigale(x, y, cageSize=cage)
        fourm = Fourmi(x, y, cageSize=cage)
        # coordonnées égales mais pas confondues
        self.assertEqual(cig.coords, fourm.coords)
        self.assertIsNot(cig.coords, fourm.coords)
        # on déplace, coordonnnées égales mais pas confondues
        cig.coords = cig.coords
        self.assertIsNot(cig.coords, fourm.coords)
        self.assertIsNot(cig.coords, (x, y))
        # on déplace d'une autre manière, coordonnées égales mais pas confondues
        cig.coords = (cig.x, cig.y)
        self.assertIsNot(cig.coords, fourm.coords)
        self.assertIsNot(cig.coords, (x, y))

    def test_ecosys(self):
        """Tests unitaires sur la classe Ecosystem
        """
        nbr = 20
        sim = 30
        w = 50
        h = 10
        eco = Ecosystem(nbr, sim, w, h)
        self.assertTrue(issubclass(type(eco), list))


