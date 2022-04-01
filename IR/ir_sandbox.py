# mass of electron
e_mass = 9.1e-31
p_mass = 1.67e-27
e = 1.6e-19


class Atom:
    def __init__(self, name, symbol, radius, Z: float, A: float, mass=.0):
        self.name = name
        self.symbol = symbol
        self.radius = radius
        self.mass = mass if mass > .0 else Z * e_mass + (A - Z) * p_mass
        self.Z = Z
        self.A = A

    def orbitals(self):
        orbs = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "3f", "4d", "5p"]
        popu = [2, 2, 6, 2, 6, 2, 10, 6, 2, 14, 10, 6]
        res = ""
        z = self.Z
        print(z)
        i = 0
        while z > 0:
            p = popu[i]
            o = orbs[i]
            if z - p >= 0:
                print(z-p)
                z -= p
                res += o + str(p) + " "
            elif z - p < 0:
                z = p - z
                res += o + str(z) + " "
                z = 0
            i += 1
        return res

    def __str__(self):
        return f"Atom of {self.name} {self.symbol} (R = {self.radius} m, Z = {self.Z}, A = {self.A}, " \
               f"mass = {self.mass} kg)"


a = Atom("hydrogen", "H", 1e-12, 1, 1)
b = Atom("Iodine", "I", 133e-2, 53, 100)
print(a)
print(a.orbitals())
print(b)
print(b.orbitals())
