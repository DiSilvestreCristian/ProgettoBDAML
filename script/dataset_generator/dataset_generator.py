import random
import csv

with open('dimensions/Shipper.society') as f:
    shipper = f.readlines()
with open('dimensions/Time.day') as f:
    time = f.readlines()
with open('dimensions/Product.category8') as f:
    category8 = f.readlines()
with open('dimensions/Geo.country_iso2') as f:
    iso2 = f.readlines()

NUM_ROWS = 1000000
FILENAME = 'dataset/prova.csv'

#[type of column, noise]
COLUMNS = [
    [shipper, 20]
    [category8, 10]
]

def random_row ():
    row = []
    for i in COLUMNS:
        row.append(random.choice(i)[:-2])
    return row

with open(FILENAME, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for i in range(NUM_ROWS):
        writer.writerow(random_row())
