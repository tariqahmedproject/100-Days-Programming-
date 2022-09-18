# Write a program that keeps on accepting a number from the user
# until the user enters Zero. Display the sum and average of all the numbers.

#num=int(input("Enter Number if You Enter (0) Then Program will be stop : "))

while True:
    n=int(input("Enter Number if You Enter (0) Then Program will be stop : "))
    if n==0:
        print("Thank You")
        break
    else:
        print("Your Enter Number is ,",n)
