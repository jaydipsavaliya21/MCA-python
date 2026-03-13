Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
... 
... def outer_function():
...     
...     y = 20
... 
...     def inner_function():
...         nonlocal y
...         global x
... 
...         z = 30  
... 
...         x = x + 5
...         y = y + 5
...         z = z + 5
... 
...         print("Inside inner function:")
...         print("Global variable x:", x)
...         print("Nonlocal variable y:", y)
...         print("Local variable z:", z)
... 
...     inner_function()
...     print("\nInside outer function:")
...     print("Nonlocal variable y:", y)
... 
... outer_function()
... 
... print("\nOutside all functions:")
