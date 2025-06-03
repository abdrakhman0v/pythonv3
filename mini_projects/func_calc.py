#-----------------------FUNC CALC------------------------

def calc(num1,num2,oper):

    try:

        num1 = int(num1)
        num2 = int(num2)
        
        if oper == "+":
            res = num1 + num2
        elif oper == "-":           
            res = num1 - num2
        elif oper == "*":       
            res = num1 * num2         
        elif oper == "**":
            res = num1 ** num2
        elif oper == "/":
            res = num1 / num2
        elif oper == "//":
            res = num1 // num2
        elif oper == "%":
            res = num1 % num2
        else:
            print("Unknown operation.")
            return
        
        print(f"Result: {num1} {oper} {num2} = {res}")
        
   
    except ValueError:
        print("Wrong input. Enter numbers.")
    except ZeroDivisionError:
        print("You can't divide by zero.")

# calc(10,2,"4")

def new_calc(num1, num2, oper):
    try:
        num1 = int(num1)
        num2 = int(num2)

        operations = {
            "+":lambda x, y: x + y,
            "-":lambda x, y: x - y,
            "*":lambda x, y: x * y,
            "/":lambda x, y: x / y,
            "//":lambda x, y: x // y,
            "**":lambda x, y: x ** y,
            "%":lambda x, y: x % y,
        }

        if oper not in operations:
            print("Unknown operation.")
            return

        result = operations[oper](num1,num2)

        print(f"Result: {num1} {oper} {num2} = {result}")

    except ValueError:
        print("Invalid input. Enter numbers.")
    except ZeroDivisionError:
        print("You can't divide by zero.")

# new_calc(25,0,"%")
