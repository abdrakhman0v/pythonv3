#----------------PROGRAMM CALC--------------------

while True:
    print("Choose an operation (1/2/3/4/5/6/7/8)")
    print("1. +\n2. -\n3. *\n4. **\n5. /\n6. //\n7. %\n8. Exit.")
    try:
        oper = int(input("Enter operation: "))

        if oper == 8:
            print("You're exiting program, goodbye!")
            break

        if oper not in range(1,8):
            print("Wrong operation. Try again.\n")
            continue

        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
            
         
        operations = {
            1:("+",lambda x, y: x + y),
            2:("-",lambda x, y: x - y),
            3:("*",lambda x, y: x * y),
            4:("**",lambda x, y: x ** y),
            5:("/",lambda x, y: x / y),
            6:("//",lambda x, y: x // y),
            7:("%",lambda x, y: x % y)
        }

        symbol, func = operations[oper]
        result = func(num1,num2)
        
        # Removing .0
        if num1 == int(num1):
            num1 = int(num1)
        if num2 == int(num2):
            num2 = int(num2)
        if result == int(result):
            result = int(result)

        print(f"Result: {num1} {symbol} {num2} = {result}\n")
    
    except ValueError:
        print("Wrong input. Try again\n")
    except ZeroDivisionError:
        print("You can't divide by zero.\n")
