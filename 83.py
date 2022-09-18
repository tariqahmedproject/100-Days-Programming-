#write program to show the word is palindrom is or not
#step 1 - reverse the string
#step-2 - compare the orginal

name=input("Enter Name:")

reverse=name[::-1]

if reverse==name:
    print(name,"word is palindrome")
else:
    print(name," word is NOT palindrome")
#------------------ same program using function-----------------
print("#------------------ same program using function-----------------")
def palindrom(name):
    reverse=name[::-1]
    if reverse==name:
        return True
    else:
        return False
name=input("Enter Name : ")

print(palindrom(name))
