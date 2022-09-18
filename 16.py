# 16.	Write a program that will check whether the number is armstrong number or not.

USER_num=int(input("Enter Number:"))
num=USER_num
#Split a number into digits

a=num%10
num=num//10

b=num%10

c=num//10

if (a**3)+(b**3)+(c**3)==USER_num:
    print("armstrong number ")
else :
    print("Not armstrong number")
