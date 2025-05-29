# 1
# compr = [i**2 for i in range(1,11)]
# print(compr)

# 2
# even_compr = [p for p in compr if p % 2 == 0]
# print(even_compr)

# compr = [1,2,3,4,5,6,7,8,9,10]
# even = [p for p in compr if p % 2 == 0]
# print(even)

# 3
# list1 = ["temirlan", "basketball", "dev"]
# compr = [len(word) for word in list1]
# print(compr)

#4
# list1 = [-5, 2, 21, -3, 1, -5, 6, -12]
# compr = [0 if i < 0 else i for i in list1]
# print(compr)

# 5
# list1 = ["temirlan", "basketball", "dev"]
# compr = [i.upper() for i in list1]
# print(compr)

# try-except
#1
# try:
#     user = int(input("Введите число: "))
#     devide = 10 / user
#     print(devide)
# except ZeroDivisionError:
#     print("Нельзя делить на 0")

# 2
# try:
#     user = int(input("Введите число: "))
#     print(user)
# except ValueError:
#     print("Вы ввели не число")

#3


#4

# try:
#     list_ = [1,54,23,True,"hi"]
    
#     print(list_[int(input("Введите индекс списка: "))])
   
# except IndexError:
#     print("Введен не верный индекс.")

# 5
# try:
#     num1 = int(input("Введите 1 число: "))
#     num2 = int(input("Введите 2 число: "))
#     print(f"{num1} + {num2} = {num1 + num2}")
# except ValueError:
#     print("Введите число!")


       
    







