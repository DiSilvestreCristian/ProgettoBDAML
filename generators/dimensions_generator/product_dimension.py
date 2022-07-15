import pandas as pd

df = pd.read_excel('generators/dimensions_generator/product_dimension.xls')

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

words_dict = {
    "category_1": [],
    "category_2": [],
    "category_3": [],
    "category_4": [],
    "category_5": [],
    "category_6": [],
    "category_7": [],
    "category_8": []
}

for elem in new_list1:
    words = elem.split('/')
    if (len(words) >= 1): words_dict['category_1'].append(words[0])
    if (len(words) >= 2): words_dict['category_2'].append(words[1])
    if (len(words) >= 3): words_dict['category_3'].append(words[2])
    if (len(words) >= 4): words_dict['category_4'].append(words[3])
    if (len(words) >= 5): words_dict['category_5'].append(words[4])
    if (len(words) >= 6): words_dict['category_6'].append(words[5])
    if (len(words) >= 7): words_dict['category_7'].append(words[6])
    if (len(words) >= 8): words_dict['category_8'].append(words[7])

for key, value in words_dict.items():
    with open('dimensions/Product.' + key, "a+") as f:
        value = list(set(value))
        for elem in value:
            f.write(elem + '\n')