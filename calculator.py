logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1, n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


##Dict where keys are symbols +*-/ and values are names of function
operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():

    num1 = float(input("What's the first number?:"))

    should_continue = True

    while should_continue:
        for key in operations_dict:
            print(key)
        operation_symbol = input("Select operation from symbols above, you want to perform:\n")
        num2 = float(input("What's next number?:"))
        operation = operations_dict[operation_symbol]
        answer = operation(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        again = input(f"Type 'y' to continue operations with {answer} or type 'n' to start new calculation or 'exit' to quit program:\n")
        if again == "y":
            num1=answer
        elif again == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("bye bye".title())

calculator()