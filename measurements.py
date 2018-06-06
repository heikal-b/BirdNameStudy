import re
from namedbird import NamedBird
import nltk


def participle_adj(name):
    return re.search('-?.*(ed)+$', name) is not None


def has_apostrophe(name):
    return re.search("('s|s')+$", name) is not None


def num_mods(name):
    return len(name.split())


def mod_pos(name):
    return nltk.pos_tag(name.split())


def main():
    bc_chickadee = NamedBird('Black-capped Chickadee', 'Poecile atricapillus', 'Passeriformes', 'Paridae')
    mountain_chickadee = NamedBird('Mountain Chickadee', 'Poecile gambeli', 'Passeriformes', 'Paridae')
    print(participle_adj(bc_chickadee.mod_name))
    print(participle_adj(mountain_chickadee.mod_name))

    nuttalls_wp = NamedBird("Nuttall's Woodpecker", 'Picoides nuttallii', 'Piciformes', 'Picidae')
    downy_wp = NamedBird('Downy Woodpecker', 'Picoides pubescens', 'Piciformes', 'Picidae')
    print(has_apostrophe(nuttalls_wp.mod_name))
    print(has_apostrophe(downy_wp.mod_name))

    gb_heron = NamedBird('Great Blue Heron', 'Ardea herodias', 'Pelecaniformes', 'Ardeidae')
    print(mod_pos(gb_heron.mod_name))


if __name__ == '__main__':
    main()