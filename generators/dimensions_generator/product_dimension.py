import pandas as pd

df = pd.read_excel('script/product_dimension/product_dimension.xls')

list_df = list(df)

for i in list_df:
    column_values = df[i].tolist()
    break

new_list = [] 

for elem in column_values:
    new_list.append(elem.replace('/Categories/', ''))

new_list1 = [] 

for elem in new_list:
    new_list1.append(elem.replace('/Products/', ''))

words0 = []
words1 = []
words2 = []
words3 = []
words4 = []
words5 = []
words6 = []
words7 = []

for elem in new_list1:
    words = elem.split('/')
    if (len(words) >= 1): words0.append(words[0])
    if (len(words) >= 2): words1.append(words[1])
    if (len(words) >= 3): words2.append(words[2])
    if (len(words) >= 4): words3.append(words[3])
    if (len(words) >= 5): words4.append(words[4])
    if (len(words) >= 6): words5.append(words[5])
    if (len(words) >= 7): words6.append(words[6])
    if (len(words) >= 8): words7.append(words[7])

with open('dimensions/Product.category1', "a+") as f:
    words0 = list(set(words0))
    for elem in words0:
        f.write(elem + '\n')

with open('dimensions/Product.category2', "a+") as f:
    words1 = list(set(words1))
    for elem in words1:
        f.write(elem + '\n')

with open('dimensions/Product.category3', "a+") as f:
    words2 = list(set(words2))
    for elem in words2:
        f.write(elem + '\n')

with open('dimensions/Product.category4', "a+") as f:
    words3 = list(set(words3))
    for elem in words3:
        f.write(elem + '\n')

with open('dimensions/Product.category5', "a+") as f:
    words4 = list(set(words4))
    for elem in words4:
        f.write(elem + '\n')

with open('dimensions/Product.category6', "a+") as f:
    words5 = list(set(words5))
    for elem in words5:
        f.write(elem + '\n')

with open('dimensions/Product.category7', "a+") as f:
    words6 = list(set(words6))
    for elem in words6:
        f.write(elem + '\n')

with open('dimensions/Product.category8', "a+") as f:
    words7 = list(set(words7))
    for elem in words7:
        f.write(elem + '\n')