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

def noisy_rows(noice_percent):
    return int((NUM_ROWS/100)*noice_percent)

def random_row ():
    row = []
    for i in COLUMNS:
        row.append(random.choice(i[0])[:-1])
    return row

NUM_ROWS = 100000
FILENAME = 'dataset/prova.csv'
COLUMNS = [
    [shipper, noisy_rows(20)],
    [time, noisy_rows(30)],
    [category8, noisy_rows(10)],
    [iso2, noisy_rows(0)]
]

with open(FILENAME, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    random_rows = []
    for i in range(NUM_ROWS):
        random_rows.append(random_row())
    for i in range(len(COLUMNS)):
        counter = COLUMNS[i][1]
        while counter != 0: 
            index = random.randint(0, NUM_ROWS-1)
            if random_rows[index][i] != "NOISE":
                random_rows[index][i] = "NOISE"
                counter -= 1
    writer.writerows(random_rows)