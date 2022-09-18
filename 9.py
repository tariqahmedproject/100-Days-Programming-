#9.	Write a program that take a user input of three angles and will find out
# whether it can form a triangle or not.
a=int(input("Enter the angle:"))

b=int(input("Enter the angle:"))

c=int(input("Enter the angle:"))


# checking Triangle is Valid or Not
total = a + b + c

if (total == 180 and a != 0 and b != 0 and c != 0):
    print("\nThis is a Valid Triangle")
else:
    print("\nThis is an Invalid Triangle")
