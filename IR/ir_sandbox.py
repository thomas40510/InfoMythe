import numpy as np

# mass of electron
e_mass = 9.1e-31
p_mass = 1.67e-27
e = 1.6e-19


def atom_from_table(symbol):
    """
    Returns an atom object from the periodic table.
    """
    # AtomicNumber,Element,Symbol,AtomicMass,NumberofNeutrons,NumberofProtons,NumberofElectrons,
    # Period,Group,Phase,Radioactive,Natural,Metal,Nonmetal,Metalloid,Type,AtomicRadius,Electronegativity,
    # FirstIonization,Density,MeltingPoint,BoilingPoint,NumberOfIsotopes,Discoverer,Year,SpecificHeat,
    # NumberofShells,NumberofValence
    f = open('data/periodic_table.csv', 'r')
    lines = f.readlines()
    f.close()
    lines.pop(0)
    for line in lines:
        res = line.split(',')
        if res[2] == symbol:
            return res[1], float(res[3]), int(res[6]), float(res[16]), float(res[17]), int(res[-1])
    return None


class Atom:
    def __init__(self, symbol, from_table=True, **kwargs):
        if from_table:
            name, mass, Z, radius, electronegativity, valence = atom_from_table(symbol)
        else:
            name, mass, Z, radius, electronegativity, valence = kwargs.values()
        self.name = name
        self.symbol = symbol
        self.radius = radius
        self.mass = mass
        self.Z = Z
        self.e = electronegativity
        self.valence = valence

    # def orbitals(self):
    #     orbs = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "3f", "4d", "5p"]
    #     popu = [2, 2, 6, 2, 6, 2, 10, 6, 2, 14, 10, 6]
    #     res = ""
    #     z = self.Z
    #     print(z)
    #     i = 0
    #     while z > 0:
    #         p = popu[i]
    #         o = orbs[i]
    #         if z - p >= 0:
    #             print(z - p)
    #             z -= p
    #             res += o + str(p) + " "
    #         elif z - p < 0:
    #             z = p - z
    #             res += o + str(z) + " "
    #             z = 0
    #         i += 1
    #     return res

    def __str__(self):
        return f"Atom of {self.name} {self.symbol} (R = {self.radius} A, Z = {self.Z}, " \
               f"mass = {self.mass})"


class Molecule:
    def __init__(self, name, atoms=None, mass=.0):
        self.name = name
        self.atoms = []
        self.bonds = []

    def add_atom(self, atom):
        self.atoms.append(atom)

    def newBond(self, atom1, atom2, bond_type="single", bond_length=.0):
        self.bonds.append(Bond(atom1, atom2, bond_type, bond_length))

    @property
    def mass(self):
        mass = sum([atom.mass for atom in self.atoms])
        return mass

    def __str__(self):
        return f"Molecule of {self.name} with {len(self.atoms)} atoms and {len(self.bonds)} bonds"


class Bond:
    def __init__(self, atom1, atom2, bond_type="single", bond_length=.0):
        self.atom1 = atom1
        self.atom2 = atom2
        self.bond_type = bond_type
        self.bond_length = bond_length


# a = Atom("hydrogen", "H", 1e-12, 1, 1)
# b = Atom("Iodine", "I", 133e-2, 53, 100)
# print(a)
# print(a.orbitals())
# print(b)
# print(b.orbitals())
a = Atom("H")
b = Atom("I")
c = Atom("Se")

o = Atom("O")
m = Molecule("O2")
m.add_atom(o)
m.add_atom(o)
m.newBond(o, o, bond_type="double")
print(m)
print(m.mass)

print(a, b, c)
