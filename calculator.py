print("Calculator(simple)")

x = int(input("Enter first number"))
y = int(input("Enter second number"))


operator = input("please enter: Add, Subtract, divide or multiply")





if operator == "add":
    total = x + y
    print ("x + y =", total)

if operator == "subtract":
    total = x - y
    print ("x - y =", total)

if operator == "divide":
    total = x / y
    print ("x ÷ y =", total)

if operator == "multiply":
    total = x * y
    print ("x*y =", total)

