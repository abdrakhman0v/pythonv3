# ============Магические методы=============
"""
Магические методы (dunder - bouble underscore) - методы у которых 2 нижних подчеркивания слева и 
справа. Магия в том что мы их не вызываем на прямую. Они срабатывают при использовании
определенных символов либо функций

__init__

10 + 3  10.__add__(3)

len()  __len__

__eq__  10 == 4

__ne__ (10!=4)

__lt__ __gt__ __le__ __ge___
   <      >     <=     >=

str() print() __str__
"""

# =============Методы==============

"1) instance методы - обычные методы которые принимают в аргументы  self"
class A:
    def func(self):
        print('метод объекта', self) 

obj_A = A()
# obj_A.func()

"""
2) class methods - методы которые принимают аргументом cls(ссылка на класс)
Нужны они для создания объектов или изменения аттрибутов класса.
Для создания класс метода нужно его задекорировать в classmethod
"""
class B:
    def func(cls):
        print('класс метод', cls)

class Pizza:
    def __init__(self,r, *ingredients):
        self.r = r
        self.ingredients = ingredients

    def cook(self):
        print(f"Готовится пицца {self.r*2} см.")
        print(f"Ингредиенты: {self.ingredients}.")

    @classmethod
    def four_cheeze(cls, r):
        pizza = cls(r, 'Мацарелло','Голландский','Чеддер','Дор блю')
        return pizza
    
pizza1 = Pizza(22,'Tomato', 'cheeze', 'mashrooms')
pizza2 = Pizza.four_cheeze(15)
pizza3 = Pizza.four_cheeze(22)

"""
3)static method - просто функция внутри класса которые
не работают с объектом и классом. Нужно задекорировать 
в staticmethod
"""
class C:
    @staticmethod
    def hello(string):
        print(string)

c = C()
c.hello('Hello')

class Cylinder:
    def __init__(self, diameter, hight):
        self.d = diameter
        self.h = hight
        self.area = self.get_area(diameter, hight)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle = pi * (di/2 ) ** 2
        side = pi * di * h
        area = circle * 2 + side
        return area
    
cylinder1 = Cylinder(4,10)
print(cylinder1.area)

cylinder2 = Cylinder(2,5)
print(cylinder2.area)



