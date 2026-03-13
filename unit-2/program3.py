import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError as e:
    logging.error("Arithmetic Exception: %s", e)
    print("Cannot divide by zero.")
