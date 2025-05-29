# # def func(a):
# #     if a > 0:
# #         return "Положительное"
# #     elif a == 0:
# #         return 0
# #     else:
# #         return "Отрицательное."

# # x = func(1)
# # y = func(-1)
# # z = func(0)

# # print(x, y, z)

# # def calc(x,y,z):
# #     if z == "+":
# #         res = x + y
# #     elif z == '-':
# #         res = x - y
# #     elif z == '*':
# #         res = x * y
# #     elif z == '/':
# #         res = x / y
# #     elif z == '**':
# #         res = x ** y
# #     elif z == '%':
# #         res = x % y
# #     return res
# # print(calc(10,5,'*'))



# "=====================HOME WORK==================="

# #1 
# def hw():
#     return "Привет, мир!"
# print(hw())


# #2
# def greet(name): 
#     return f"Привет, {name}"
# print(greet("Temirlan"))


# #3
# def add(num1, num2):
#     res = num1 + num2
#     return res
# print(add(12,5))


# #4
# def mult(num1 , num2):
#     res = num1 * num2
#     return res
# print(mult(20,2))

# #5
# def defult(name = 'Гость'):
#     return f"\nИмя пользователя: {name}"
# print(defult("Temirlan"))


# #6
# def info(name, age):
#     return f"\nИмя: {name}\nВозраст: {age}"
# print(info("Temirlan", 19))


# #7
# def exp(num):
#     return f"Квадрат: {num**2}\nКуб: {num**3} "
# print(exp(-2))

# # 8
# def exter():
#     def inter():
#         return "Вложено!"
#     return inter()
# print(f"Результат: {exter()}")

#9
# def adder(*num):
#     res = sum(num)
#     return res
# print(adder(1,5,6))


#10
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1

#     return num * factorial(num - 1)
# print(factorial(4))

#11
# list1 = [(1, 9), (3, 1), (2, 5)]
# sort = sorted(list1, key = lambda x:x[1])
# print(sort)

# "=================Области видимости============"
# # 1 
# num = 10
# def func():
#     return num
# print(func())


# # 2
# def func1():
#     num = 15
#     return num
# print(func1())


# # 3
# def func2():
#     num = 7
# print(num) # Мы не можем глобально взаимодействовать с локальной переменной
            

# # 4
# num = 2
# def func3():
#     global num
#     num = 5
#     return num
    
# print(f"Новое значение: {func3()}")


# # 5
# def func4():
#     list1 = [1,2,3]
#     def func5():
#         return f"Внешняя переменная {list1}"
#     return func5()
# print(func4())

# # 6
# def func4():
#     text = "original"
#     def func5():
#         nonlocal text
#         text = "changed"
#         return text
#     return func5()
# print(f"Новое значение: {func4()}")


# # 7
# num = 10
# def func6():
#     num = 5
#     return num
# print(num)
# print(func6())


# # 8
# for i in range(4):
#     num = 5
# print(f"Переменная доступна: {num}")


# # 9
# number = 10
# def func7(num):
#     num = 15
#     return num
# print(number)
# print(func7(number))


# # 10
# num = 5 
# def func8():
#     num = 10
#     return num
# print(f"Значение глобальной переменной не изменилось: {num}")
# Так как без ключевого слова "global" мы не можем изменять в локальной области
# глобальную переменную



