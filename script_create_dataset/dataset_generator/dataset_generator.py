import random
import csv
import random 
import string 

with open('dimensions/Geo.continent') as f:
    continent = f.readlines()
with open('dimensions/Geo.country') as f:
    country = f.readlines()
with open('dimensions/Geo.country_iso2') as f:
    iso2 = f.readlines()
with open('dimensions/Geo.country_iso3') as f:
    iso3 = f.readlines()
with open('dimensions/Geo.region') as f:
    region = f.readlines()
with open('dimensions/Geo.region_iso') as f:
    region_iso = f.readlines()
with open('dimensions/Payment.method') as f:
    payment_method = f.readlines()
with open('dimensions/Product.category1') as f:
    category1 = f.readlines()
with open('dimensions/Product.category2') as f:
    category2 = f.readlines()
with open('dimensions/Product.category3') as f:
    category3 = f.readlines()
with open('dimensions/Product.category4') as f:
    category4 = f.readlines()
with open('dimensions/Product.category5') as f:
    category5 = f.readlines()
with open('dimensions/Product.category6') as f:
    category6 = f.readlines()
with open('dimensions/Product.category7') as f:
    category7 = f.readlines()
with open('dimensions/Product.category8') as f:
    category8 = f.readlines()
with open('dimensions/Shipper.society') as f:
    shipper = f.readlines()
with open('dimensions/Time.day') as f:
    time = f.readlines()

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
FILENAME = 'datasets/amazon_completo.csv'
COLUMNS = [
    [continent, noisy_rows(10)],
    [country, noisy_rows(10)],
    [iso2, noisy_rows(10)],
    [iso3, noisy_rows(10)],
    [region, noisy_rows(10)],
    [region_iso, noisy_rows(10)],
    [payment_method, noisy_rows(10)],
    [category1, noisy_rows(10)],
    [category2, noisy_rows(10)],
    [category3, noisy_rows(10)],
    [category4, noisy_rows(10)],
    [category5, noisy_rows(10)],
    [category6, noisy_rows(10)],
    [category7, noisy_rows(10)],
    [category8, noisy_rows(10)],
    [shipper, noisy_rows(10)],
    [time, noisy_rows(10)]
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