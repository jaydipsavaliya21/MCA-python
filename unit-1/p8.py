Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = input("Enter a string: ")
... 
... vowels = "aeiouAEIOU"
... vowel_count = 0
... for ch in s:
...     if ch in vowels:
...         vowel_count += 1
... print("Number of vowels:", vowel_count)
... 
... 
... length = 0
... for ch in s:
...     length += 1
... print("Length of string:", length)
... 
... rev = ""
... for ch in s:
...     rev = ch + rev
... print("Reversed string:", rev)
... 
... find_char = input("Enter character/string to find: ")
... replace_char = input("Enter character/string to replace with: ")
... new_string = s.replace(find_char, replace_char)
... print("String after replace:", new_string)
... 
... if s == rev:
...     print("The string is a Palindrome")
... else:
