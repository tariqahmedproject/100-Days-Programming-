# 65.	Create 2 lists from a given list where 1st list will contain all the odd numbers from the
# original list and
# the 2nd one will contain all the even numbers

a=[]
b=[]
for i in range(5):
    n=int(input("Enter Five Number :"))
    if n%2==0:
        a.append(n)



    else:
        b.append(n)
print("Even = ",a)
print("odd = ",b)

