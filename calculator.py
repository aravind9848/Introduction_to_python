a = float(input("enter the first number: "))
op = input("operator (+,-,*,/): ")
b = float(input("enter the second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Error: Division by zero")
    else:
        print(a / b)
else:
    print("invalid operator:", op)
