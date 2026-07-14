def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def mod(a,b):
    return a%b

def exp(a,b):
    return a**b


while True:
    try:
        a,b=map(float, input(f"Enter a and b (use space; int or float only): ").split())
        print(f"Which operation do u wanna perform?")
        print('''
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Modulus(Remainder)
            6. Exit
            7. Power/Exponent
            ''')
    
    except ValueError:
        print("Plz enter value only in integer or float; enter both a and b with space separated.")

    try:
        choice=int(input(f"Enter ur choice here: "))
        
        if choice==1:
            result=add(a,b)
            print(f"The addition of {a} and {b} is {result}")

        elif choice==2:
            result=subtract(a,b)
            print(f"The difference of {a} and {b} is {result}")
            
        elif choice==3:
            result=multiply(a,b)
            print(f"The product of {a} and {b} is {result}")
            
        elif choice==4:
            result=divide(a,b)
            print(f"The division of {a} and {b} is {result}")
            
        elif choice==5:
            result=mod(a,b)
            print(f"The remainder of {a} and {b} is {result}")
            
        elif choice==7:
            result=exp(a,b)
            print(f"The power of {a} and {b} is {result}")

        elif choice==6:
            print("Thank you for visiting.")
            break
        
        else:
            print("Enter a valid choice...")
            
    except ZeroDivisionError:
        print(f"The division between {a} and {b} is: Value is not defined...")
    except ValueError:
        print("Enter choices between 1-5!!!")