#1
# list1 = ['apple', 'banana', 'kiwi']
# lenth = list(map(len, list1))
# print(lenth)

#2
# list1 = [1, 2, 3, 4]
# double = list(map(lambda x: x * 2, list1))
# print(double)

#3
# list1 = ['hello', 'world']
# upper = list(map(lambda x: x.upper(),list1))
# print(upper)

#4
# list1 = [1.2, 2.5, 3.8]
# rounded = list(map(round,list1))
# print(rounded)

#5
# list1 = [2, 3, 4]
# square = list(map(lambda x: x ** 2, list1))
# print(square)


#1
# list1 = [1, 2, 3, 4, 5]
# even = list(filter(lambda x: x % 2 == 0, list1))
# print(even)

#2
# list1 = ['cat', 'parrot', 'dog', 'elephant']
# filtered = list(filter(lambda x: len(x) > 4, list1))
# print(filtered)

#3
# list1 = [-2, 0, 1, 5, -1]
# filtered = list(filter(lambda x: x > 0, list1))
# print(filtered)

#4 
# list1 = ['apple', 'kiwi', 'banana']
# filtered = list(filter(lambda x: "a" in x, list1))
# print(filtered)

#5
# list1 = [1, 3, 4, 6, 9]
# filtered = list(filter(lambda x: x % 3 == 0, list1))
# print(filtered)


# from functools import reduce

#1
# list1 = [1, 2, 3, 4]
# reduced = reduce(lambda x,y: x + y, list1)
# print(reduced)

#2
# list1 = [1, 2, 3, 4]
# reduced = reduce(lambda x,y: x * y, list1)
# print(reduced)

#3
# list1 = [3, 7, 2, 9, 4]
# reduced = reduce(max, list1)
# print(reduced)

#4
# list1 = ['hello', ' ', 'world']
# reduced = reduce(lambda a,b: a + "" + b, list1)
# print(reduced)

#5
# list1 = [10, 2, 1]
# reduced = reduce(lambda x, y: x - y, list1)
# print(reduced)


#1
# list1 = ['a', 'b', 'c']
# for index, value in enumerate(list1):
#     print(index, value)

#2
# list1 = ['line1', 'line2']
# for index, value in enumerate(list1, 1):
#     print(index,value)

#3
# list1 = [10, 20, 30]
# for index, value in enumerate(list1):
#     print(f"{value} + {index} = {value + index}")

#4
# list1 = ['apple', 'banana']
# dicted = dict(enumerate(list1))
# print(dicted)

#5
# list1 = ['a', 'b', 'c', 'd']
# filtered = [x for i, x in enumerate(list1) if i % 2 == 0]
# print(filtered)

# list1 = [-12, 4, 0, -3, 12]
# filtered = list(filter(lambda x: x < 0, list1))
# print(filtered)
