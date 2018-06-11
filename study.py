import pickle
import nltk
import measurements as msr
import csv


def main():
    """
    Collect and present data on the names of North American birds (US + Canada)
    :return:
    """
    # Load list of NamedBirds
    birds_pickle = open('built_birds.pickle', 'rb')
    birds = pickle.load(birds_pickle)

    # Divide birds into birds of prey and nons
    bop_names = [b.mod_name for b in birds if b.is_bop()]
    nbop_names = [b.mod_name for b in birds if not b.is_bop()]

    # Frequency distribution
    cond_obs = [('Bird of prey', n) for n in bop_names] + [('Non bird of prey', n) for n in nbop_names]
    cfd = nltk.ConditionalFreqDist(cond_obs)

    # Collect data
    # --Embeddedness measure
    bop_embeddedness = msr.embeddedness(bop_names, nbop_names)
    bop_embeddedness = round(bop_embeddedness, 3)

    nbop_embeddedness = msr.embeddedness(nbop_names, bop_names)
    nbop_embeddedness = round(nbop_embeddedness, 3)

    # --Proportion with genitives
    bop_genitive = [n for n in bop_names if msr.has_apostrophe(n)]
    bop_genitive = len(bop_genitive) / len(bop_names)
    bop_genitive = round(bop_genitive, 3)

    nbop_genitive = [n for n in nbop_names if msr.has_apostrophe(n)]
    nbop_genitive = len(nbop_genitive) / len(nbop_names)
    nbop_genitive = round(nbop_genitive, 3)

    # --Proportion with participle adjectives
    bop_part_adj = [n for n in bop_names if msr.participle_adj(n)]
    bop_part_adj = len(bop_part_adj) / len(bop_names)
    bop_part_adj = round(bop_part_adj, 3)

    nbop_part_adj = [n for n in bop_names if msr.participle_adj(n)]
    nbop_part_adj = len(nbop_part_adj) / len(nbop_names)
    nbop_part_adj = round(nbop_part_adj, 3)

    # --Get syllable counts
    syll_csv = csv.reader(open('syll_count.csv'))
    syll_counts = [(r[0], r[1]) for r in syll_csv]
    syll_count_fd = nltk.ConditionalFreqDist(syll_counts)

    # --Syllable count proportion
    syll_count_prop_bop = [(k, round(syll_count_fd['Bird of prey'][k]/len(bop_names), 3))
                           for k in syll_count_fd['Bird of prey'].keys()]

    syll_count_prop_bop.sort()
    syll_count_prop_nbop = [(k, round(syll_count_fd['Non bird of prey'][k]/len(nbop_names), 3))
                            for k in syll_count_fd['Non bird of prey'].keys()]
    syll_count_prop_nbop.sort()

    # Display results
    print('Number of birds of prey:', len(bop_names))
    print('Number of non-birds of prey:', len(nbop_names))
    print('\n')

    print('Frequency distribution: birds of prey:')
    cfd['Bird of prey'].tabulate()
    print('\n')
    print('Frequency distribution: non-birds of prey:')
    cfd['Non bird of prey'].tabulate()
    print('\n')

    print('Bird of prey embeddedness:', bop_embeddedness)
    print('Non bird of prey embeddedness:', nbop_embeddedness)
    print('\n')

    print('Proportion with genitive (birds of prey):', bop_genitive)
    print('Proportion with genitive (non-birds of prey):', nbop_genitive)
    print('\n')

    print('Proportion with participle adjective (birds of prey):', bop_part_adj)
    print('Proportion with participle adjective (non-birds of prey):', nbop_part_adj)
    print('\n')

    print('Frequency distribution: syllable count:')
    syll_count_fd.tabulate()
    print('\n')

    print('Syllable count proportion (birds of prey):')
    for i in syll_count_prop_bop:
        print('{0}: {1}'.format(i[0], i[1]))
    print('\n')

    print('Syllable count proportion (non-birds of prey):')
    for i in syll_count_prop_nbop:
        print('{0}: {1}'.format(i[0], i[1]))

    birds_pickle.close()


if __name__ == '__main__':
    main()
    exit(0)