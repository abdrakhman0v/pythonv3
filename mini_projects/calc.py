#----------------PROGRAMM CALC--------------------

while True:
    print("Choose an operation(1/2/3/4/5)")
    print("1.+\n2.-\n3.*\n4./\n5.Exit.")
    try:
        oper = int(input("Enter operation: "))
        if oper == 5:
            print("You're exiting programm, goodbye!")
            exit()
        if oper > 5:
            print("Wrong operation. Try again.\n")
            continue
        num1 = int(input("Enter 1 number: "))
        num2 = int(input("Enter 2 number: "))
            
    except ValueError:
        print("Wrong input. Try again")
        continue
    
    try:
        if oper == 4:   
            print(f"Result: {num1} / {num2} = {num1 / num2}\n") 
    except ZeroDivisionError:
        print("You can't divide by zero.\n")
        continue
        
    if oper == 1:
        print(f"Result: {num1} + {num2} = {num1 + num2}\n")
    elif oper == 2:
        print(f"Result: {num1} - {num2} = {num1 - num2}\n")
    elif oper == 3:
        print(f"Result: {num1} * {num2} = {num1 * num2}\n")
    continue






    



            
