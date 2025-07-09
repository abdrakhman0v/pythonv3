# 1
class Person:
    name = 'Temirlan'

    def introduce(self):
        print(f'Привет! Я {self.name}')

# 2
class Student(Person):
    grade = 11

    def show_grade(self):
        print(f'{self.name} учится в {self.grade}-ом классе')

student = Student()
student.introduce()
student.show_grade() 


# 3
class Animal:
    def make_sound(self):
        print('Животное издает звук...')

class Dog(Animal):
    def make_sound(self):
        print('Гав!')

animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()


# 4
class Engine:
    def describe_engine(self):
        print('Двигатель V8')

class Wheels:
    def describe_wheels(self):
        print('Колеса с титановыми дисками')

class Car(Engine, Wheels):
    ...

car = Car()
car.describe_engine()
car.describe_wheels()


# 5
class A:
    def show_A(self):
        print('A')

class B(A):
    def show_B(self):
        print('B')

class C(B):
    def show_C(self):
        print('C')

c = C()
c.show_A()
c.show_B()
c.show_C()


# 6
class Animal:
    def sound(self):
        print('Животное издает звук...')

class Dog(Animal):
    def sound(self):
        print('Гав!')

class Cat(Animal):
    def sound(self):
        print('Мяу')

class Bird(Animal):
    def sound(self):
        print('Кар!')


# 7
class A:
    def A(self):
        print('Я родитель.')

class B(A):
    def B(self):
        print('Я дочерний класс Б, унаследовавший класс А')

class C(A):
    def C(self):
        print('Я дочерний класс С, унаследовавший класс А')

class D(B,C):
    def D(self):
        print('Я дочерний класс Д, унаследовавший классы Б и С')

d = D()
d.A()
d.B()
d.C()
d.D()


# 8
class A:
    def describe(self):
        print('Привет от А')

class B(A):
    def describe(self):
        super().describe()
        print('И привет от Б')

class C(B):
    def describe(self):
        super().describe()
        print('И привет от C')

# a = A()
# a.describe()
# b = B()
# b.describe()
c = C()
c.describe()


# 9
class Vehicle:
    def type(self):
        print('Транспортное средство')

class Car(Vehicle):
    def parent1(self):
        print('Машина')

class Boat(Vehicle):
    def parent2(self):
        print('Лодка')

class AmphibiousCar(Car, Boat):
    def result(self):
        print('Плавающая машина')

amphib_car = AmphibiousCar()
amphib_car.type()
amphib_car.parent1()
amphib_car.parent2()
amphib_car.result()


# 10

class Animal:
    def general(self):
        print('Животное')

class Mammal(Animal):
    def peculiarity(self):
        super().general()
        print('Вскормливание детенышей молоком\nНаличие волосяного покрова')

class Bird(Animal):
    def peculiarity(self):
        super().general()
        print('Клюв\nПерья\nСпособность летать(не у всех видов)')

class Bat(Mammal):
    def peculiarity(self):
        super().peculiarity()
        print('Эхолокация\nНочной образ жизни')

class Penguin(Bird):
    def peculiarity(self):
        super().peculiarity()
        print('Стойкость к холоду\nОтличное умение плавать')

mammal = Mammal()
# mammal.peculiarity()

bird = Bird()
# bird.peculiarity()

bat = Bat()
# bat.peculiarity()

penguin = Penguin()
penguin.peculiarity()
