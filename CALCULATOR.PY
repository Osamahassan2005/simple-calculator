# SIMPLE CALCULATOR
def add(a, b):
    return a + b

def subt(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        print("Division by zero is not allowed")

while True:
    choice = input('''Welcome to the simple calculator :)
Please select an option:
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Exit
''')

    if choice == "5":
        print("Thank you!")
        break

    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))

    if choice == "1":
        print("Final result:", add(a, b))
    elif choice == "2":
        print("Final result:", subt(a, b))
    elif choice == "3":
        print("Final result:", mult(a, b))
    elif choice == "4":
        print("Final result:", div(a, b))
    else:
        print("Invalid option. Please try again.")

