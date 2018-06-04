birds_of_prey_orders = ['Strigiformes', 'Cathartiformes', 'Accipitriformes', 'Falconiformes']

class NamedBird:
    def __init__(self, full_name, species, order, family):
        self.full_name = full_name
        full_name = full_name.split()
        self.main_name = full_name[1]

        if len(full_name) >= 1:
            self.mod_name = full_name[0]

        self.species = species
        self.order = order
        self.family = family

    def is_bop(self):
        return self.order in birds_of_prey_orders or self.order.lower() in [f.lower() for f in birds_of_prey_orders]

    def __eq__(self, other):
        return self.full_name == other.full_name

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return ', '.join([self.full_name, self.species, self.order, self.family])


def main():
    barn_owl = NamedBird('Barn Owl', 'Tyto alba', 'Strigiformes', 'Tytonidae')
    print('Full name: ', barn_owl.full_name)
    print('Main name: ', barn_owl.main_name)
    print('Modifying name: ', barn_owl.mod_name)
    print('Species name: ', barn_owl.species)
    print('Order: ', barn_owl.order)
    print('Family: ', barn_owl.family)
    print('Is a bird of prey?: ', barn_owl.is_bop())
    print('String format: ', str(barn_owl))
    print('Representation: ', repr(barn_owl))


if __name__ == '__main__':
    main()