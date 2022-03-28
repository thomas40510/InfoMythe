# defines an atom class

class Atom:
    def __init__(self, name, symbol, atomic_number, mass, valence_electrons, configuration, oxidation_state, radius, electronegativity):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.mass = mass
        self.valence_electrons = valence_electrons
        self.configuration = configuration
        self.oxidation_state = oxidation_state
        self.radius = radius
        self.electronegativity = electronegativity

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def bond_valence(self):
        return self.valence_electrons - self.oxidation_state

    def orbitals(self):
        return self.configuration.split()

    def config_string(self):
        return f"{self.configuration} ({self.oxidation_state})"


# main
if __name__ == "__main__":
    hydrogen = Atom("Hydrogen", "H", 1, 1.00794, 1, "1s1", 0, 0.31, 2.2)
    print(hydrogen)
    print(hydrogen.bond_valence())
    print(hydrogen.orbitals())
    print(hydrogen.config_string())

    carbon = Atom("Carbon", "C", 6, 12.0107, 4, "2s2 2p2", 2, 0.77, 2.55)
    print(carbon)
    print(carbon.bond_valence())
    print(carbon.orbitals())
    print(carbon.config_string())
