a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operator (+, -, *, /): ")
if operation == "+":
    print("Result:", a + b)
elif operation == "-":
    print("Result:", a - b)
elif operation == "*":
    print("Result:", a * b)
elif operation == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operator")
