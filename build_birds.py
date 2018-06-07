import csv
from namedbird import NamedBird
import pickle

def main():
    """
    Build NamedBird objects
    :return:
    """
    # Read Clements list CSV data
    clements_csv = open('/Users/heikal/BirdNameStudy/clements_usca_mod.csv')
    csv_reader = csv.reader(clements_csv)
    # List for new NamedBirds
    built_birds = []

    # Build NamedBirds
    for r in csv_reader:
        new_bird = NamedBird(r[0], r[1], r[2], r[3])
        built_birds.append(new_bird)

    # Display sample NamedBirds
    for i in range(30):
        print(built_birds[i])

    # Save the list of new NamedBirds
    outfile = open('/Users/heikal/BirdNameStudy/built_birds.pickle', 'wb')
    pickle.dump(built_birds, outfile)

    # Fin
    clements_csv.close()
    outfile.close()


if __name__ == '__main__':
    main()