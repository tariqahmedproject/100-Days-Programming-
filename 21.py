#Write a program to find the sum of n numbers, where n will be provided by the user

n=int(input("Enter Number How much you want to add:"))
sum=0
for i in range(0,n):
    num=int(input("Enter Number"))
    sum=sum+num
print("Answers is :",sum)