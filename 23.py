#23.	Write a program that can multiply 2 numbers provided by the user without using the * operator
num1=int(input("Enter Number :"))
num2=int(input("Enter Number :"))
product=0
for i in range (1,num2+1):  #Python for loop
 product=product+num1       #product+=num1
print(product)