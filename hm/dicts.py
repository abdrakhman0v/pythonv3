# 1
a = {"name":"Temirlan", "age":19, "profession":"dev"}
print(a.get("profession"))

# 2
product = {"name": "phone", "price": 1000}
product["price"] = 1200
product["brand"] = "Samsung"
print(product)

# 3
s = "p y t h o n"
s = s.split()
dict_ = dict.fromkeys(s,0)
print(dict_)

# 4
user = {"name":"Alice", "age":25}
popped = user.pop("age")
print(popped)

# 5
info = {"city": "Paris", "population": 2148327}
if "city" in info:
    print("Ключ найден.")
else:
    print("Ключ не найден.")

# 6
numbers = [1, 2, 2, 3, 4, 4, 5, 1]
print(set(numbers))

# 7
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.intersection(set2))

# 8
grades = {"John": 85, "Jane": 92, "Dave": 58}
upper80 = {}
for name, grade in grades.items():
    if grade > 80:
        upper80[name] = grade
print(upper80)

# 9
nums = [4, 5, 2, 9, 1, 0, 4, 2, 9, 1]
dict1 = {}
for i in nums:
    count = nums.count(i)
    if count == 1 or count == 2:
        dict1[i] = count
print(dict1)