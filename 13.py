# 13.	Write  a program that will tell whether the given number is divisible by 3 & 6.
num=int(input("enter number"))
if num%3==0 and num%6==0:
    print("Divisible")
else:
    print("Not divsible")