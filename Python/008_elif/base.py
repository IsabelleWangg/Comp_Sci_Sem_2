a = int(input("Please enter a number: "))
op = str(input("Please enter an operation: "))
b = int(input("Please enter another number: "))

if op == "+":
    c = a+b
    print(str(a) + " + " + str(b) + " = " + str(c))
elif op == "-":
    c = a-b
    print(str(a) + " - " + str(b) + " = " + str(c))
elif op == "*":
    c = a*b
    print(str(a) + " * " + str(b) + " = " + str(c))
elif op == "/":
    c = a/b
    print(str(a) + " / " + str(b) + " = " + str(c))
    