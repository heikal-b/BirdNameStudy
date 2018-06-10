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


def num_syll(name):
    """
    Return the number of syllable in a name
    :param name: the name
    :return: number of syllables

    """
    if name == '<No modifier name>':
        return 0

    if '-' in name:
        name = name.split('-')
    else:
        name = name.split()

    # Pronouncing dictionary
    prondict = nltk.corpus.cmudict.dict()

    # Count vowels in arpabet transcription
    syllables = 0

    for n in name:
        try:
            phone = prondict[n.lower()]
            syllables += len([ph for ph in phone[0] if not ph.isalpha()])
        except KeyError:
            syllables += 1000

    return syllables

    # Try to find the word in the pronouncing dictionary

    """
    try:
        phone = prondict[name.lower()]
        phone = phone[0]
        return len([ph for ph in phone if not ph.isalpha()])
    except KeyError:
        return 0
    """


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

    print(num_syll(mountain_chickadee.mod_name))


if __name__ == '__main__':
    main()