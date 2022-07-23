import random
import csv
import string 
import os
from sys import flags

import pandas as pd
import dataset_options as options

DIMENSIONS_DIR = 'dimensions/'
NOISE_DIR = 'generators/datasets_generator/noise/'

# Define dimensions dictionary from 'dimensions/' folder
dimensions = {}
dimension_files = [f for f in os.listdir(DIMENSIONS_DIR) if os.path.isfile(os.path.join(DIMENSIONS_DIR, f))]
for dimension in dimension_files:
    with open(DIMENSIONS_DIR + dimension, 'r', encoding='UTF8') as f:
        dimensions[dimension] = f.readlines()

# Create a random entry in the dataset
def random_row():
    row = []
    for i in options.COLUMNS:
        row.append(random.choice(dimensions[i])[:-1])
    return row

def get_random_row(): 
    length = 10
    letters = string.ascii_lowercase 
    result_str_a = ''.join(random.choice(letters) for i in range(length)) 
    result_str_b = ''.join(random.choice(letters) for i in range(length)) 
    return [result_str_a, result_str_b]

with open(options.FILENAME, 'r', encoding='UTF8') as f:
        list = f.readlines()
def get_parent_row():
    return random.choice(list)[:-1].split(",")

with open(options.CHILD_FILENAME, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    random_rows = []
    inherited_rows = int(options.NUM_ROWS_CHILD * options.inherited_rows_percentage/100)
    for i in range(inherited_rows):
        random_rows.append(get_parent_row())
    for i in range(options.NUM_ROWS_CHILD - inherited_rows):
        random_rows.append(get_random_row())
    writer.writerows(random_rows)