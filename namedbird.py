# List of bird of prey orders
birds_of_prey_orders = ['Strigiformes', 'Cathartiformes', 'Accipitriformes', 'Falconiformes']


class NamedBird:
    """
    A NamedBird represents birds for accessing different parts of their names and other information
    """
    def __init__(self, full_name, species, order, family):
        """
        Initialze a NamedBird object with different aspects of taxonomic information
        :param full_name: (str) Full name of the bird
        :param species: (str) Species name /scientific name of the bird
        :param order: (str) The order of the bird
        :param family: (str) The family of the bird
        """
        self.full_name = full_name
        full_name = full_name.split()
        self.main_name = full_name[-1]

        # Some bird names are just a single word
        if len(full_name) > 1:
            self.mod_name = ' '.join(full_name[:-1])

        self.species = species
        self.order = order
        self.family = family

    def is_bop(self):
        """
        Tell if a given bird is a bird of prey
        :return: (bool) True if the bird is a bird of prey, if not return False
        """
        return self.order in birds_of_prey_orders or self.order.lower() in [f.lower() for f in birds_of_prey_orders]

    def __eq__(self, other):
        """
        Tell that two birds are equal if they have the same full name
        :param other: (NamedBird) The bird to be compared with
        :return: True if the two birds are equal
        """
        return self.full_name == other.full_name

    def __str__(self):
        """
        Represent the string of a NamedBird as it's full name
        :return:
        """
        return self.full_name

    def __repr__(self):
        """
        Represent a NamedBird as a sequence of its information
        :return:
        """
        return ', '.join([self.full_name, self.species, self.order, self.family])


def main():
    """
    Testing, testing ...
    :return:
    """
    barn_owl = NamedBird('Barn Owl', 'Tyto alba', 'Strigiformes', 'Tytonidae')
    barn_owl_2 = NamedBird('Barn Owl', 'Tyto alba', 'Strigiformes', 'Tytonidae')
    lincoln_sparrow = NamedBird('Lincoln\'s Sparrow', 'Melospiza lincolnii', 'Passeriformes', 'Passerellidae')

    print('Full name: ', barn_owl.full_name)
    print('Main name: ', barn_owl.main_name)
    print('Modifying name: ', barn_owl.mod_name)
    print('Species name: ', barn_owl.species)
    print('Order: ', barn_owl.order)
    print('Family: ', barn_owl.family)
    print('Is a bird of prey?: ', barn_owl.is_bop())
    print('String format: ', str(barn_owl))
    print('Representation: ', repr(barn_owl))

    print('\n')

    print('Full name: ', lincoln_sparrow.full_name)
    print('Main name: ', lincoln_sparrow.main_name)
    print('Modifying name: ', lincoln_sparrow.mod_name)
    print('Species name: ', lincoln_sparrow.species)
    print('Order: ', lincoln_sparrow.order)
    print('Family: ', lincoln_sparrow.family)
    print('Is a bird of prey?: ', lincoln_sparrow.is_bop())
    print('String format: ', str(lincoln_sparrow))
    print('Representation: ', repr(lincoln_sparrow))

    print('\n')
    
    gb_heron = NamedBird('Great Blue Heron', 'Ardea herodias', 'Pelecaniformes', 'Ardeidae')
    print('Full name: ', gb_heron.full_name)
    print('Main name: ', gb_heron.main_name)
    print('Modifying name: ', gb_heron.mod_name)
    print('Species name: ', gb_heron.species)
    print('Order: ', gb_heron.order)
    print('Family: ', gb_heron.family)
    print('Is a bird of prey?: ', gb_heron.is_bop())
    print('String format: ', str(gb_heron))
    print('Representation: ', repr(gb_heron))

    print('\n')
    
    print('Barn owl equals another barn owl?: ', barn_owl == barn_owl_2)
    print('Barn owl equals Lincoln sparrow?: ', (barn_owl == lincoln_sparrow))


if __name__ == '__main__':
    main()
