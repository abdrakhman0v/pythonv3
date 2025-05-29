# 1
list1 = []
list1.extend([25,"Hello",True,[1,2,3]])
print(list1[-1][1])

# 2
list1 = ["Hi",25.5,True,22]
res = list1.pop(0)
print(res)

# 3
lst1 = ['hello', 42, True, 'world', False, 42]
lst1.remove(42)
print(lst1)

# 4
lst = ['simple', 'hard', 'advanced', 'basic']
lst.insert(2, 'medium')
print(lst)

# 5
first = [1,2]
second = [3,4]
first += second 
print(first)

# 6
mixed = ['cat', 3, 'python', 1.5, 'a', 'elephant']

string = []

for i in mixed:
    if type(i) == str:
        string.append(i)

string.sort(key = len)
print(string)

# 7
data = (True,21,'Hi',28.5,[1,2,3])
data[1] = 99
print(data)
# Кортеж нельзя изменять. Это неизменяемый тип данных. Кортеж имеет
# только 2 метода: index и count.