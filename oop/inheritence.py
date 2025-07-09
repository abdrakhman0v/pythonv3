"""
Наследование - прицнип ООП, в котором мы можем унаследовать, переопределить 
и использовать в дочернем классе все методы и аттрибуты родительского класса
"""

# Унаследование
# class A:
#     age = 18

#     def say_hello(self):
#         print("Привет")

# class B(A):
#     ...

# obj_a = A()
# obj_a.say_hello()

# obj_b = B()
# obj_b.say_hello()
# print(obj_b.age)


# Переопределение 
class Dog():
    def voice(self):
        print('Woof')

class Cat(Dog):
    def voice(self):
        print('Meow')

dog = Dog()
dog.voice()

cat = Cat()
cat.voice()


"""
Виды наследования:
1. Одиночное наследование - когда дочерний класс наследуется только от 1-го класса
2. Множественное наследование - когда дочерний класс может наследоваться от нескольких 
классов сразу
3. Многоуравневое наследование - когда мы наследуемся от класса у которого есть родитель
4. Иерархическое наследование - когда у одного родителя есть много дочерних классов
5. Гибридное наследование - когда мы можем использовать сразу несколько видов 
наследования
"""

# Множественное наследование
# class A:
#     ...

# class B:
#     ...

# class C:
#     ...

# class D:
#     ...

# class E(A,B,C,D):
#     ...


# Многоуравневое наследование
class A:
    ...

class B(A):
    ...

class C(B):
    ...


# Иерархическое наследование
class A:
    ...

class B(A):
    ...

class C(A):
    ...

class D(A):
    ...


# Гибридное наследование
class A:
    ...

class B(A):
    ...

class C(A): # Класс б и с - иерархическое наследование (наследованы от А)
    ...

class D(B,C): # - Множественное наследование (наследован от двух классов)
    ...


"""
Класс object - самый главный в иерархии класс от него наследуется любой класс
который вы создадите
"""

class Car:
    ...

car = Car()

print(dir(car))

class A:
    var = 1

class B:
    ...

class C(A,B):
    ...

c = C()
print(c.var)
print(C.mro())
#mro - metod resolution order (порядок поиска методов и аттрибутов)

'-----------Проблемы множественного наследования-----------'
# 1) преблема ромба (решена при промощи mro)

# class A:
#     ...

# class B:
#     ...

# class C(A,B):
#     ...

# c_obj = C()
# print(c_obj.var)

#2) проблема перекрестного наследования (не решенная)

# class A:
#     ...

# class B:
#     ...

# class D(A,B):
#     ...

# class E(B,A):
#     ...

# class F(D,E):
#     ...

# super() - функция для обращения к родительскому классу

# class A:
#     def describe(self):
#         print('Привет от А')

# class B(A):
#     def describe(self):
#         super().describe()
#         print('И привет от Б')

# class C(B):
#     def describe(self):
#         super().describe()
#         print('И привет от C')


# c = C()
# c.describe()



# class Animal:
#     def general(self):
#         print('Животное')

# class Mammal(Animal):
#     def peculiarity(self):
#         super().general()
#         print('Вскормливание детенышей молоком\nНаличие волосяного покрова')

# class Bird(Animal):
#     def peculiarity(self):
#         super().general()
#         print('Клюв\nПерья\nСпособность летать(не у всех видов)')

# class Bat(Mammal):
#     def peculiarity(self):
#         super().peculiarity()
#         print('Эхолокация\nНочной образ жизни')

# class Penguin(Bird):
#     def peculiarity(self):
#         super().peculiarity()
#         print('Стойкость к холоду\nОтличное умение плавать')

# mammal = Mammal()
# # mammal.peculiarity()

# bird = Bird()
# # bird.peculiarity()

# bat = Bat()
# # bat.peculiarity()

# penguin = Penguin()
# penguin.peculiarity()

