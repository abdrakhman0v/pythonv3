# 1
with open("test.txt",) as f:
    print(f.read())

# 2
login = input("Введите логин: ")
password = input("Введите пароль: ")
logpass = f"{login}\n{password}"

with open("users.txt", "w") as f:
    f.write(logpass)

# 3
with open("test.txt") as f:
    text = f.read()
    if "w" in text:
        print("Да, в тексте есть 'w'")
    else:
        print("Нет, в тексте нету 'w'")

# 4
with open('python.txt') as f:
    text = f.read()
    splitted = text.split()
    filtered = filter(lambda x: "o" in x, splitted)
    print(list(filtered))

# 5
with open("test.txt") as f:
    print(f.read()[::-1])

# 6
from functools import reduce
with open("text.txt") as f:
    text = f.read()
    repl = text.replace("aaa", "").replace("fxdya", "").replace(" ", "").replace("\n", "")
    list1 = list(repl)
    int_list =[int(x) for x in list1]
    reduced = reduce(lambda x, y: x+y,int_list)
    print(reduced)
