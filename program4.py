armstrong_number=[]

print("enter 10 numbers:")

for i in range(10):
    num=int(input(f"Number {i+1}="))

    digits=str(num)
    power=len(digits)
    total=sum(int(d)** power for d in digits)

    if total == num:
        armstrong_number.append(num)

print("armstrong numbers found:",armstrong_number)
