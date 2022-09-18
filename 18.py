#18.	Write a program that will give you the in hand salary after deduction of
# HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _
# – 30%)(0-1lakh print k).

salary=int(input("Enter Salary : "))
hra=10
da=5
pf=3
if salary >= 500000 or salary <=100000:
    tax=(10/100)*salary
    tmp_slaray=salary-tax
    print(tmp_slaray)

elif salary >= 1100000 or salary <=2000000:
    tax=(20/100)*salary
    tmp_slaray=salary-tax
    print(tmp_slaray)

elif salary >= 2100000 or salary <=3000000:
    tax=(30/100)*salary
    tmp_slaray=salary-tax
    print(tmp_slaray)
