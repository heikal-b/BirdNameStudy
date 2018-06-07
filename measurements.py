import re
from namedbird import NamedBird
import nltk


def participle_adj(name):
    """
    Tell if a word is a participle adjective
    :param name: The target word
    :return: True if the word is a participle adjective
    """
    return re.search('-?.*(ed)+$', name) is not None


def has_apostrophe(name):
    """
    Tell if a word contains an apostrophe
    :param name: The target word
    :return: True if the word contains an apostrophe
    """
    return re.search("('s|s')+$", name) is not None


def num_mods(name):
    """
    Return the number of words in a string
    :param name: The target string
    :return: Number of words in a string
    """
    return len(name.split())


def mod_pos(name):
    """
    Return the list of POS in a name
    :param name: The target name
    :return: List of POS tags
    """
    name = name.lower()
    tup_list = nltk.pos_tag(name.split())
    return [p[1] for p in tup_list]


def embeddedness(target_list, compared_list):
    """
    Measure the embedddedness of one list within another; embeddedness of A in B = #(A int B)/#A
    :param target_list: The target list
    :param compared_list: The list to be compared with
    :return: Embeddedness score
    """
    intersection = [e for e in target_list if e in compared_list]
    return len(intersection)/len(target_list)


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
    print(mod_pos(gb_heron.full_name))

    list1 = ['Blue', 'Mississippi', 'Atlantic', 'Common', 'Northern']
    list2 = ['Common', 'Northern', 'Bald']
    print(embeddedness(list2, list1))


if __name__ == '__main__':
    main()