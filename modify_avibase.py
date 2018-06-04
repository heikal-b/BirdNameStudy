import csv

def is_order_family(listrow):
    return listrow[1] == ''

def get_family()

avibase = open('/Users/heikal/BirdNameStudy/clements_avibase_us_ca.csv', 'rb')
csv_reader = csv.reader(avibase)
avi_list = []
avi_list_new = []

for row in csv_reader:
    row[3] = ''
    avi_list.append(row)

for row in avi_list:
    print(row)

outfile = open('/Users/heikal/BirdNameStudy/avibase2.csv', 'wb')

for i in range(len(avi_list)):
    if is_order_family(avi_list[i]):
        curr_order_family = avi_list[0]

    if not is_order_family(avi_list[i]):



