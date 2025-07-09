#============Абстракция==============
"""
Это принцип ООП в котором создается класс пустышка где задаются названия
для методов и аттрибутов для того чтобы не забыть переопределить их
в дочернем классе
"""

from abc import ABC, abstractmethod

class AbstractAnimal(ABC):

    @abstractmethod
    def voice(self):
        ...

    @abstractmethod
    @property
    def legs(self):
        ...

class Dog(AbstractAnimal):
    legs = 4
    def voice(self):
        print('Woof')
    
obj = Dog()

class Cat(AbstractAnimal):
    legs = 4
    def voice(self):
        print('Meow')

    def hunt(self):
        print('Hunt')

