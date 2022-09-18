#write Program for atm using OOP with while loop



class atm:
    def __init__(self):
        self.pin_code = ''
        self.balance = 0
        self.main()

    def main(self):
        while True:

            choice = input("""
            1.Enter 1 for create pin
            2.Enter 2 for Deposit Money
            3.Enter 3 With Draw Money
            4.Enter 4 check balance
            5.exit
    
            Enter any choice : """)
            if choice == '1':
                self.pin()
            elif choice == '2':
                self.depoist()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                break



            else:
                print("Bye")
                break

    def pin(self):
        self.pin_code = input("Enter Your Pin : ")
        print("Pin Set sucesfully...")

    def depoist(self):
        temp = input("Enter Pin code : ")
        if temp == self.pin_code:
            new_amount = int(input("Enter Amount to depoist : "))
            self.balance = new_amount + self.balance
            print("Amount add sucesfully...")
            print("Your New amount is :", self.balance)
        else:
            print("Please Enter Valid pin code ")

    def withdraw(self):
        temp = input("Enter Pin code : ")
        if temp == self.pin_code:
            new_amount = int(input("Enter Amount to withdraw : "))
            if new_amount < self.balance:
                self.balance = self.balance-new_amount
                print("Your Reamming amount is :", self.balance)
            else:
                print("Balance not avaiable ")
        else:
            print("Enter Valid pin...!")

    def check_balance(self):
        temp = input("Enter Pin code : ")
        if temp == self.pin_code:
            print("Your Amount is :", self.balance)


obj = atm()

