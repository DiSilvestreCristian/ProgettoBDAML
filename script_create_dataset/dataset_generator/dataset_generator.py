import random
import csv
import random 
import string 

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

def get_random_string(): 
    length = 8
    letters = string.ascii_lowercase 
    result_str = ''.join(random.choice(letters) for i in range(length)) 
    return result_str

NUM_ROWS = 50000
FILENAME = 'datasets/shipperAmazon.csv'
COLUMNS = [
    [shipper, noisy_rows(10)],
    [iso2, noisy_rows(5)]
]

with open(FILENAME, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    random_rows = []
    for i in range(NUM_ROWS):
        random_rows.append(random_row())
    for i in range(len(COLUMNS)):
        list_index = random.sample(range(NUM_ROWS), COLUMNS[i][1])
        for j in list_index:
            random_rows[j][i] = get_random_string()
    writer.writerows(random_rows)