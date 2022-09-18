#12.	Write a program to find the volume of the cylinder.
# Also find the cost when ,when the cost of 1 litre milk is 40Rs.
radius=float(input("Enter Radius of cylinder :"))
height=float(input("Enter Height of cylinder :"))
pi=3.14
volume=pi*radius*height
print("Volume is =",volume)

cost_per_letter=40
find_cost=volume/cost_per_letter
print("Cost is=",find_cost)