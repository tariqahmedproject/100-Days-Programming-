# 7.	Write a program that will tell whether the given year is a leap year or not.
year=int(input("Enter Year to Check Leap Year :"))
if year%4==0:
    print(year,"This Is Leap Year")

elif year%400==0:
    print(year,"This Is Leap Year")
else:
    print(year,"Not leaf year")

