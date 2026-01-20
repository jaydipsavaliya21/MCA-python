num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
op=input("enter operator(+,-,*,/):")

if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    
    if num2!=0:
        result=num1/num2
    else:
        result ="error ! division by zero"
else:
    result="invalid operator"

print("Result:",result)
      
