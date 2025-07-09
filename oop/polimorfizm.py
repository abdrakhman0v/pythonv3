#==================Полиморфизм=================
"""
Это принцип ООП в котором есть методы которые называются одинаково
но с разной реализацией
"""

class Dog:
    def voice(self):
        print('Woof')

class Cat:
    def voice(self):
        print('Meow')

class Frog:
    def voice(self):
        print('Ribbbit')

objects = [Dog(), Cat(), Frog()]
for object in objects:
    object.voice()