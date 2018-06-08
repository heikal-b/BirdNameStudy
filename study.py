import pickle
import nltk
import measurements as msr


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

    birds_pickle.close()


if __name__ == '__main__':
    main()
    exit(0)