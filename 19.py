#19.	Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to pkr  4.exit
print(""" 
1. cm to ft
2. k to miles
3. usd to pkr
4. exit
""")
num=float(input("Enter Your Choise : "))
if num==1:
    cm=float(input("Enter Cm :"))
    feet=cm/30.48
    print(cm,"Feet is =",feet)
elif num==2:
    kelometer= float(input("Enter KeloMeter :"))
    miles=kelometer*0.62137
    print("Miles is =",miles)
elif num==3:
    pkr=207
    usd=float(input("Enter USD :"))
    pkr=usd*pkr
    print("Pkr is : ",pkr)

elif num==4:
    print("Exit sucesfully")


else:
    print("Invlaid choise...!")


