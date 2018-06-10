import pickle
import measurements as msr

if __name__ == '__main__':
    """Get syllable counts of bird names"""
    # Load list of NamedBirds
    birds = pickle.load(open('built_birds.pickle', 'rb'))

    # Divide birds
    bop_names = [b.mod_name for b in birds if b.is_bop()]
    nbop_names = [b.mod_name for b in birds if not b.is_bop()]

    # List of rows of bird data
    rows = []

    # Count syllables and show progress
    syll_count = 0
    count = 1

    for n in bop_names:
        syll_count = msr.num_syll(n)
        print('{0}) {1} : {2} syllables'.format(count, n, syll_count))
        rows.append(['Bird of prey', n, syll_count])
        count += 1

    for n in nbop_names:
        syll_count = msr.num_syll(n)
        print('{0}) {1} : {2} syllables'.format(count, n, syll_count))
        rows.append(('Non bird of prey', n, syll_count))
        count += 1

    # cond_obs = [('Bird of prey', msr.num_syll(n)) for n in bop_names] \
    #           + [('Non bird of prey', msr.num_syll(n)) for n in nbop_names]

    # Save list of rows of bird data
    outfile = open('syll_count.pickle', 'wb')
    pickle.dump(rows, outfile)
    outfile.close()

    exit(0)
