#READ
# file = open("test.txt", "r")

# # print(file.writable())
# # print(file.readable())

# # print(file.read())
# # file.seek(0)
# # print(file.read())

# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())

# # print(file.readlines())
# # file.seek(0)
# # print(file.readlines())

# file.close()
# file.closed


#WRITE
# file = open("new_file.txt", "w")

# # print(file.readable())
# # print(file.writable())

# file.write("- Hello, Temirlan!")
# file.seek(0)
# file.write("\n- Darou, Python")
# file.writelines(("\nMon\n","Tue\n","Wed"))
# file.close()
# # print(file.closed)


#APEND
# file = open("new_file.txt", "a")
# file.write("BBB\n")
# file.close()


#КОНСТРУКТНЫЙ МЕНЕДЖЕР
# with open("test.txt") as f:
#     print(f.read())
# print(f.closed)



#2
# with open("hello.txt") as f:
#     print(f.read())

#3
# lines = ["Первая строка\n", "Вторая строка\n", "Третья строка"]
# with open("lines.txt", "w") as f:
#     f.writelines(lines)

# #4
# with open("lines.txt") as f:
#     print(f.read())

# 5
# with open("nums.txt","w") as f:
#     for num in range(1,11):
#         f.write(f"{num}\n")
   
# with open("nums.txt","r") as f:
#     total = 0
#     for line in f:
#         total += int(line.strip())
    
# print("Результат:",total)

#6
# with open("text.txt") as file:
#     text = file.read()
#     print(text.count("Python"))

#7
# with open("input.txt") as file, open("output.txt", "w") as f:
#     for line in file:
#         inted = int(line.strip())
#         multed = inted * 2
#         print(multed)
#         f.write(f"{multed}\n")

    

   
        



    

    
    
