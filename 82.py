#write program to spilit user name of email using function

def user_name(email):
    email,g= email.split("@")
    return email


email=input("Enter Email : ")

print(user_name(email)) #comment if we want only email and passsword

print("------------------------- program to show user name and password")

#email=input("Enter email ")
password=input("Enter password :")

print("Your User Name is : ",user_name(email))
print("Your password is : ",password)