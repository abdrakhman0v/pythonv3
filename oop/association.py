#============Ассоциация=============
"""
Это принцип ООП, в котором 2 класса связаны друг с другом.

Агрегация - слабая связь.
Композиция - сильная связь.
"""

class Battery:
    _power = 100

    def charge(self):
        if self._power < 100:
            self._power = 100

class Iphone:
    def __init__(self, color):
        self.color = color
        self.batery = Battery()

iphone = Iphone('Red')
del iphone


class Nokia:
    def __init__(self,color,battery):
        self.color = color
        self.battery = battery

battery_for_nokia= Battery()
nokia = Nokia('green',battery_for_nokia)
del nokia