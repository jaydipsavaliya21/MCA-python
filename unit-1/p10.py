Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> add = lambda a, b: a + b
... sub = lambda a, b: a - b
... mul = lambda a, b: a * b
... div = lambda a, b: a / b if b != 0 else "Error: Division by zero"
... 
... num1 = float(input("Enter first number: "))
... num2 = float(input("Enter second number: "))
... op = input("Enter operator (+, -, *, /): ")
... 
... if op == '+':
...     print("Result:", add(num1, num2))
... elif op == '-':
...     print("Result:", sub(num1, num2))
... elif op == '*':
...     print("Result:", mul(num1, num2))
... elif op == '/':
...     print("Result:", div(num1, num2))
... else:
