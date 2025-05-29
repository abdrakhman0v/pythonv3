import json

#1
# with open("data.json") as f:
#     python_obj = json.load(f)
#     print(python_obj)

#2
# data_user = {
#     "name":"Temirlan",
#     "age":19,
#     "email":"g1noma69@gmail.com"
# }

# with open("user.json", "w") as f:
#     json.dump(data_user, f, indent=4)

#3
# with open("string.json") as f:
#     python_dict = json.load(f)
#     print(python_dict["price"])

#4
# def read_product(id, file):
#     with open(file) as f:
#         products = json.load(f)
#         product = next((p for p in products if p["id"] == id), "Неверный id")
#         print(product)

# read_product(4,"products.json")

#5
# def update_config(key,new,file):
#     with open(file) as f:
#         config = json.load(f)
#         config[id] = new
#     with open(file, "w") as f:
#         json.dump(config, f)
#     print("Настройки обновлены.")
     
# update_config("volume",120,"config.json")
# update_config("theme","dark","config.json")

#6
# def top_students(file):
#     with open(file) as f:
#         python_list = json.load(f)
#     with open("top_students.json", "w") as f:
#         filtered = [s for s in python_list if s["score"]>80]
#         json.dump(filtered,f,indent=4)

# top_students("students.json")

#7
# with open("employees1.json") as f:
#     python_list1 = json.load(f)
# with open("employees2.json") as f:
#     python_list2 = json.load(f)
# with open("all_employees.json","w") as f:
#     all_empl = python_list1 + python_list2 
#     unique = []
#     for item in all_empl:
#         if item not in unique:
#             unique.append(item)
#     json.dump(unique,f,indent=4)
    
#8
from datetime import datetime
def log_event(event, user_id):
    with open("log.json") as f:
        python_list = json.load(f)
        now = datetime.now()
        new_json = event


        






