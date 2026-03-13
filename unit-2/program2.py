class AgeTooSmallError(Exception):
    pass

age = int(input("Enter your age: "))
try:
    if age < 18:
        raise AgeTooSmallError("Age must be at least 18.")
    print("Access granted.")
except AgeTooSmallError as e:
    print("Error:", e)
