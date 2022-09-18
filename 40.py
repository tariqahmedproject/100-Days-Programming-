# 40.	Write a program to print the following pattern
# *
# **
# ***
# **
# *




for i in range(0,5):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

for k in range(5,0,-1):
    for l in range(0,k-1):
        print("*",end=" ")
    print(" ")
