a = int(input("Enter first number:"))
op = input("Enter Operator:")
b = int(input("Enter second number:"))
if op == "+":
    print(a+b)

elif op == "-":   
    print(a-b)

elif op == "*":
    print(a*b)

elif op == "/":
    print(a/b)

elif op == "%":
    print(a%b)

elif op == "**":
    print(a**b)

else:
    print("invalid operator")
