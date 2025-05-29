# # def glushitel(func):
# #     def wrapper(*args,**kwargs):
# #         print("тихо")
# #         func()
# #     return wrapper
    

# # @glushitel
# # def pistolet():
# #     print("shoot")

# # def decorator(func):
# #     def wrapper():
# #         print("hello")
# #         func()
# #     return wrapper

# # @decorator
# # def func():
# #     print("hi")

# # func()


# # 1
# def log_decorator(say_hello):
#     def wrapper():
#         print("Выполнение функции...")
#         say_hello()
#         print("Завершение функции.")
#     return wrapper

# @log_decorator
# def say_hello():
#     print("Hello!")
# say_hello()

# # 2
# def count_calls(greet):
#     count = 0
#     def wrapper():
#         nonlocal count
#         count += 1
#         print(f"Функция была вызвана {count} раз(а)")
#         greet()
#     return wrapper

# @count_calls
# def greet():
#     print("Hi!")

# greet()
# greet()
# greet()

# # 3
# def timing_decorator(slow_function):
#     def wrapper():
#         slow_function()
#         print(f"Время выполнения: 1.00сек.")
#     return wrapper

# @timing_decorator
# def slow_function():
#     import time
#     time.sleep(1)
#     print("Готово!")
# slow_function()

# # 4
# def greeter(name):

#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             print(f"Привет {name}")
#             func(*args,**kwargs)
#         return wrapper
#     return decorator

# @greeter("Темирлан")
# def do_something():
#     print("Работаю...")
# do_something()

# # 5
# def type_check(func):
#     def wrapper(*args,**kwargs):
#         try:
#             func(*args, **kwargs)
#         except TypeError:
#             print("Ошибка. Аргумент должен быть числом.")
#     return wrapper

# @type_check
# def square(n):
#     print(n * n)
# square(5)
# square("fn")

# # 6
# def cache_dec(func):
#     cache = {}

#     def wrapper(*args):
#         if args in cache:
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result

#     return wrapper
# @cache_dec
# def multiply(a, b):
#     print("Выполняю вычисление...")
#     return a * b
# print(multiply(2,5))
# print(multiply(2,5))

# # 7
# def admin_required(func):
#     def wrapper(user,*args,**kwargs):
#         if user.get("is_admin"):
#             return func(user,*args,**kwargs)
#         else:
#             print("Доступ запрещен.")
#     return wrapper

# @admin_required
# def delete_user(user):
#     print(f"Пользователь {user['name']} удален.")
# delete_user({"name": "Tema", "is_admin": False})

import time

def timing

def slow_func():
    time.sleep(1)
    print("Готово.")
