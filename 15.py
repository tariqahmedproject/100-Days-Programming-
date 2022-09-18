# 15.	Write a program that will take three digits from the user and add the square of each digit.?
#three input using list
x, y, z = [int(x) for x in input("Enter three value with seprate with comma: ").split(",")]
square=x**2+y**2+z**2
print(square)
