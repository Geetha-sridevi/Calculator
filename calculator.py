a = float(input("Enter first number => "))
opr = str(input("Enter Operation(+,-,*,/,%) >= "))
b = float(input("Enter second number => "))


if opr == "+":
    sum = a + b
    total = str(f"The sum of {a} + {b} is {sum}")
elif opr == "-":
    diff = a - b
    total = str(f"The difference of {a} - {b} is {diff}")
elif opr == "*":
    mul = a * b
    total = str(f"The difference of {a} * {b} is {mul}")
elif opr == "/":
    div = a / b
    total = str(f"The difference of {a} / {b} is {div}")
elif opr == "%":
    mod = a % b
    total = str(f"The difference of {a} % {b} is {mod}")
else:
    total = str("Please enter an valid operation.....")
print(total)