#1.	User will input (3ages).Find the oldest one

age1=int(input("Enter Age :"))
age2=int(input("Enter Age :"))
age3=int(input("Enter Age :"))

if age1<age2 and age1<age3:
    print("Age 1 is oldest ")
elif age2<age1 and age2<age3:
    print("age 2 is oldest")
elif age3<age1 and age3<age2:
    print("age 3 is oldest")
else:
    print("All are equal")

