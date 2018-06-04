"""
Modify the list of North American birds (US + Canada) obtained from Avibase
"""
import csv

def is_empty_row(listrow):
    return len([c for c in listrow if c !='']) == 0

def is_order_family(listrow):
    assert type(listrow) is list
    return listrow[1] == ''

def get_order_family(order_family):
    assert type(order_family) is str

    order_family = order_family.split()
    return (order_family[0].capitalize()[:-1], order_family[1].capitalize())

# Clements list obtained from Avibase
avibase = open('/Users/heikal/BirdNameStudy/clements_avibase_us_ca.csv')
# Read the CSV document
csv_reader = csv.reader(avibase)
# Move CSV data to a list
avi_list = []

# Copy non-empty csv rows to a list
for row in csv_reader:
    if not is_empty_row(row):
        # Delete conservation status data
        row[3] = ''
        if len(row) > 0:
            avi_list.append(row)

#outfile = open('/Users/heikal/BirdNameStudy/avibase2.csv', 'wb')

for r in avi_list:
    if is_order_family(r):
        curr_order_family = get_order_family(r[0])
    else:
        r[2] = curr_order_family[0]
        r[3] = curr_order_family[1]

for r in avi_list:

for row in avi_list:
    print(row)



