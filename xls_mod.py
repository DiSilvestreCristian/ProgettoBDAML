import pandas as pd

df = pd.read_excel('/Users/giordano/Downloads/ProgettoBigData/uk_categories.xls')

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
    match len(words):
        case 1:
            words0.append(words[0])
        case 2: 
            words0.append(words[0])
            words1.append(words[1])
        case 3: 
            words0.append(words[0])
            words1.append(words[1])
            words2.append(words[2])
        case 4: 
            words0.append(words[0])
            words1.append(words[1])
            words2.append(words[2])
            words3.append(words[3])
        case 5: 
            words0.append(words[0])
            words1.append(words[1])
            words2.append(words[2])
            words3.append(words[3])
            words4.append(words[4])
        case 6: 
            words0.append(words[0])
            words1.append(words[1])
            words2.append(words[2])
            words3.append(words[3])
            words4.append(words[4])
            words5.append(words[5])
        case 7: 
            words0.append(words[0])
            words1.append(words[1])
            words2.append(words[2])
            words3.append(words[3])
            words4.append(words[4])
            words5.append(words[5])
            words6.append(words[6])
        case 8: 
            words0.append(words[0])
            words1.append(words[1])
            words2.append(words[2])
            words3.append(words[3])
            words4.append(words[4])
            words5.append(words[5])
            words6.append(words[6])
            words7.append(words[7])
        

with open('Product.categorie1', "a+") as f:
    words0 = list(set(words0))
    for elem in words0:
        f.write(elem + '\n')

with open('Product.categorie2', "a+") as f:
    words1 = list(set(words1))
    for elem in words1:
        f.write(elem + '\n')

with open('Product.categorie3', "a+") as f:
    words2 = list(set(words2))
    for elem in words2:
        f.write(elem + '\n')

with open('Product.categorie4', "a+") as f:
    words3 = list(set(words3))
    for elem in words3:
        f.write(elem + '\n')

with open('Product.categorie5', "a+") as f:
    words4 = list(set(words4))
    for elem in words4:
        f.write(elem + '\n')

with open('Product.categorie6', "a+") as f:
    words5 = list(set(words5))
    for elem in words5:
        f.write(elem + '\n')

with open('Product.categorie7', "a+") as f:
    words6 = list(set(words6))
    for elem in words6:
        f.write(elem + '\n')

with open('Product.categorie8', "a+") as f:
    words7 = list(set(words7))
    for elem in words7:
        f.write(elem + '\n')