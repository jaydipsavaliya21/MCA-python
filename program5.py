odd_numbers=[]

print("enter the 10 numbers=")
for i in range(10):
    num=int(input(f"number{i+1}:"))
    if num % 2!=0:
        odd_numbers.append(num)

if odd_numbers:
    largest_odd=max(odd_numbers)
    print("the largest odd number is:",largest_odd)
else:
    print("no odd numbers were entered.")
