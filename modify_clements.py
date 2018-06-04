"""
Modify the list of North American birds (US + Canada) obtained from Avibase
"""
import csv


def is_empty_row(listrow):
    """
    Check if a CSV row is empty
    :param listrow: CSV row
    :return: True if the row is empty
    """
    return len([c for c in listrow if c != '']) == 0


def is_order_family(listrow):
    """
    Check if a CSV row contains only the order and family data
    :param listrow: CSV row
    :return: True if the row contains only the order and family data
    """
    assert type(listrow) is list
    return listrow[1] == ''


def get_order_family(order_family):
    """
    Separate the order and family data
    :param order_family: the order and family in a single string
    :return: order-family pair
    """
    assert type(order_family) is str
    order_family = order_family.split()
    return order_family[0].capitalize()[:-1], order_family[1].capitalize()


# Clements list obtained from Avibase
clements_csv = open('/Users/heikal/BirdNameStudy/Clements_usca.csv')
# Read the CSV document
csv_reader = csv.reader(clements_csv)
# Copy non-empty csv rows to a list
clements_list = [[r[0], r[1], r[2], ''] for r in csv_reader if not is_empty_row(r)]
clements_csv.close()

# Create columns for the order and family data
for row in clements_list:
    if is_order_family(row):
        curr_order_family = get_order_family(row[0])
    else:
        row[2] = curr_order_family[0]
        row[3] = curr_order_family[1]

# Remove non-bird rows
clements_list = [row for row in clements_list if not is_order_family(row)]

# Write new data set to a new file
outfile = open('/Users/heikal/BirdNameStudy/Clements_usca_mod.csv', 'w')
outwriter = csv.writer(outfile)
outwriter.writerows(clements_list)
outfile.close()