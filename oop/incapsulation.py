#===============Инкапсуляция===============
"""
Инкапсуляция - это прицип ООП у которого две трактовки (2 объяснения)
1) Сбор всех необходимых аттрибутов в 1 капсулу(класс)
2) Сокрытие данных (ограничение доступка к аттрибутом)
"""

# ----------- Виды доступа к аттрибутом ---------
"""
1) public 
2) protected - с одним underscore в начале
3) private - с двумя underscore в начале
"""

class A:
    attr1 = 'public'
    _attr2 = 'protected'
    __attr3 = 'private'


# print(A.attr1)
# print(A._attr2)
# print(A.__attr3) # - ошибка
# print(A._A__attr3) # - правильно


# =================Getters/Setters============
"""
Это функции при помощи которых можно получить изменить/значение аттрибута
"""
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self,new_age):
#         self.__age = new_age

# person = Person('Temirlan', 19)
# print(person.get_age())
# person.set_age(30)
# print(person.get_age())


class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    # @age.getter
    # def age(self):
    #     return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

person = Person('Temirlan', 19)
print(person.age)
person.age = 24
print(person.age)

class Kid(Person):
    ...

kid = Kid('Alisher', 18)
print(Kid.age)


