from utils_calc import *

while True:

    operation = input(
        "Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n"
    ).lower()

    if operation == "exit":
        break

    elif operation == "add":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", add(num1, num2))

    elif operation == "subtract":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", sub(num1, num2))

    elif operation == "multiply":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", multiply(num1, num2))

    elif operation == "divide":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        result = divide(num1, num2)
        print(result if isinstance(result, str) else f"The result is: {result}")

    elif operation == "exponent":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        print("The result is:", exponent(num1, num2))

    elif operation == "modulo":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        result = modulo(num1, num2)
        print(result if isinstance(result, str) else f"The result is: {result}")

    elif operation == "floor_divide":
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        result = floor_divide(num1, num2)
        print(result if isinstance(result, str) else f"The result is: {result}")

    elif operation == "absolute":
        num = float(input("Enter the number:\n"))
        print("The result is:", absolute(num))

    else:
        print("Invalid option!")