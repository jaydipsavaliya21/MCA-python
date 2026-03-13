Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculate(num1, num2, operator):
...     if operator == '+':
...         return num1 + num2
...     elif operator == '-':
...         return num1 - num2
...     elif operator == '*':
...         return num1 * num2
...     elif operator == '/':
...         if num2 != 0:
...             return num1 / num2
...         else:
...             return "Error: Division by zero"
...     else:
...         return "Invalid operator"
... 
... a = float(input("Enter first number: "))
... b = float(input("Enter second number: "))
... op = input("Enter operator (+, -, *, /): ")
... 
... result = calculate(a, b, op)
