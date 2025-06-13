import json

with open('cars_shop.json') as f:
    list_ = json.load(f)
    for dict_ in list_:
        print(dict_['title'])
        