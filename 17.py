# 17.	Write a program that will take user input of (4 digits number)
# and check whether the number is narcissist number or not.

USER_num=int(input("Enter Number:"))
num=USER_num
#Split a number into digits

a=num%10
num=num//10

b=num%10

c=num//10

d=num//10

if (a**3)+(b**3)+(c**3)+(d**3)==USER_num:
    print(" narcissist number ")
else :
    print("Not narcissist number")
