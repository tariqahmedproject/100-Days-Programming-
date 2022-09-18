# 59.	Write a python program to reverse a list

a=[1,2,3]
b=a[::-1]
print(b)

# ------------------- by user input()--------------------
print("\n Same program with user input \n")
n=int(input("Enter num you want to inputs : "))
list=[]

for i in range(n):
    num=input("Enter NUMBER : ")
    l=list.append(num)
    l=list[::-1]

print("Before Reverse :",list)
print("AFter Reverse :",l)
