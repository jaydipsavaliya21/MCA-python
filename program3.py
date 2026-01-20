s1=float(input("enter marks for subject1:"))
s2=float(input("enter marks for subject2:"))
s3=float(input("enter marks for subject3:"))
s4=float(input("enter marks for subject4:"))

total=s1+s2+s3+s4
percentage=(total/400)*100

if percentage >=90:
    grade="A+"
elif percentage >=80:
    grade="A"
elif percentage >=70:
    grade="B"
elif percentage >=60:
    grade="C"
elif percentage >=50:
    grade="D"
else:
    grade="fail"

print("\n---student Result ---")
print("Total Marks:",total)
print("Percentage Marks:",percentage)
print("grade:",grade)
