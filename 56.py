# 56.	Write a python program to remove all the duplicates from a list

list=[1,2,3,4,5,1]
check=[]
print("Before Duplication : ",list)

for i in list:
    if i not in check:
        check.append(i)
print("After Remove dupication:",check)

# +---------------------------------- same program with user inputs-----------------------
print("\n  same program with user inputs\n\n")
n_list=int(input("Enter List how much you want a list :"))
check_list=[]


for i in range(n_list):
    n=input("Enter Numbers:")

    for j in n:
        if j not in check_list:
            check_list.append(j)

print("After remove",check_list)

