"====================JSON================="
# JavaScript Object Notation - универсальный формат в котором мы можем хранить данные
# в типах данных понятных почти для всех яп

import json

# json_list = "[1,2,3,4,5]"
# print(type(json_list))

# python_list = json.loads(json_list)
# print(type(python_list))

#десериализация - перевод с json строки в пайтон объект
#loads для десериализации с  json СТРОКИ
#load для десериализации с  json ФАЙЛА

# with open("db.json") as file:
#     list_ = json.load(file)
    # print(list_)

#сериализация - это перевод пайтон объекта в json строку
#dumps - сериализация в json строк
#dump - сериализация в json file

python_list = [12,34,2,True,False,None]
# json_array = json.dumps(python_list)
# print(json_array)

with open("db.json", "w") as file:
    json.dump(python_list, file)