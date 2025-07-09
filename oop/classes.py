#=====================OOP=====================
"""
OOP - Object-orientated programing
ООП - Объектно-ориентированное программирование (парадигма)
"""

class Person:
    #  Переменные внутри классов называются аттрибутами
    # (если переменная рядом с классом то их значения будут у всех объектов)
    arms = 2
    legs = 2
    # Функция внутри класса называется методом
    def __init__(self,n,a):
        # __init__ - это метод который добавляет в объект те аттрибуты
        # которые у объектов разные
        # self - это ссылка на объект который только что создался
        self.name = n
        self.age = a

    def fly(self):
        print(f'Я - {self.name}, могу летать!')

obj1 = Person("Temirlan", 19)
obj2 = Person("Temir", 18)

# print(obj1.arms, obj1.legs, obj1.name, obj1.age)
# print(obj2.arms, obj2.legs, obj2.name, obj2.age)

# obj1.fly()
# obj2.fly()


# =====================Объекты класса====================
""" 
Объект , экземпляр, instance класса - это конечный продукт созданный
по классу
"""

# ====================Аттрибуты и методы=====================
"""
Аттрибуты - это переменные внутри класса
Методы - это функции внутри класса
"""

class A:
    var = 'переменная класса'

    def __init__(self):
        var2 = 'переменная объекта'
    
    def func(self):
        return 'метод'
    
class House:
    smart_ = True
    class_ = 'comfort+'

    def __init__(self, color, count_room):
        self.color = color
        self.count_room = count_room

    def action(a):
        if a == '2 раза хлопнул':
            print('Свет включен')
        elif a == 'крикнул':
            print('Звонок в спец службы')

h1 = House('black', 7)
h2 = House('white', 10)

"""
__new__ = это метод, который создает пустой объект (оболочка)
__init__ = это метод, который после создания засунет туда переменные 
(этот процесс называется инициализацией)
"""

#================Принципы ООП=================
"""
1) Наследование
2) Инкапсуляция
3) Полиморфизм
4) Абстракция
5) Ассоциация 
  1.Композиция
  2.Агрегация
"""

class Calc:
    
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 + num2
    
    def sqrt(self, num):
        self.num = num
        return num ** 0.5
    
    def percent(self, num, percent):
        self.num = num
        self.percent = percent
        return percent / 100 * num
    
calc = Calc()
# print(calc.add(2,2))
# print(calc.sqrt(81))
# print(calc.percent(100,10))


# '-----------------Миксины------------------'
""" 
Миксины - это классы помошники, от них наследуются чтобы расширить функционал другого класса
От миксинов не создаются объекты
"""
class FlyMixin():
    def fly(self):
        print('Can fly')

class WalkMixin():
    def walk(self):
        print('Can walk')

class SwimMixin():
    def swim(self):
        print('Can swim')

class Cat(WalkMixin, SwimMixin):
    name = '- Cat'

    def hunt(self):
        print('Can hunt')

class Human(WalkMixin, SwimMixin):
    name = '- Human'

    def talk(self):
        print('Can talk')

class Duck(FlyMixin, WalkMixin, SwimMixin):
    name = '- Duck'

    def talk(self):
        print('Сan quack')

objects = [Cat(), Duck(), Human()]
for obj in objects:
    print(obj.name)
    attrs = ['fly', 'swim', 'walk', 'hunt', 'talk']
    for attr in attrs:
        if hasattr(obj,attr):
            method = getattr(obj,attr)
            method()