Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def total_sum(*args):
...     total = 0
...     for num in args:
...         total += num
...     print("Total of given numbers:", total)
... 
... total_sum(10, 20, 30)
... total_sum(5, 15)
