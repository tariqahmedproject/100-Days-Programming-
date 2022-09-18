#24.	Write a program that can find the factorial of a given number provided by the user.
num=int(input("Enter Number :"))

j=1
for i in range(num,0,-1):  #(5(start),   0(end) ,-1(stepvalue)
    j=j*i
print(j)
