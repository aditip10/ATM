database = {"Aditi": [181091003,9131234567,123456,"1234",1],
            "Tanvi": [181091002,9136123456,56849,"1234",1],
            "Ankush": [181091004,9512345685,123897,"1234",1],
            "Jyoti": [181091005,9123456789,56847,"1234",1],
            "Divya": [181091006,9594123123,225589,"1234",1]}


class ATM:
    def __init__(self, name, acc_no, mobileno, bal, pin, acc_status):
        self.acc_no = acc_no
        self.pin = pin
        self.balance =bal
        self.name = name
        self.mobileno= mobileno
        self.status=acc_status

    def user_authentication(self):
        code = input("Enter PIN: ")
        count = 3
        if self.status==0:
            print("ACCOUNT BLOCKED\nVisit nearest branch to unblock account")
        while (code!= self.pin):
            count = count - 1
            print("INCORRECT PIN\nTires left:",count)
            code = input("Enter PIN: ")
            if (count == 1 and code!= self.pin):
                print("INCORRECT PIN\nTires left:0")
                print("ACCOUNT BLOCKED")
                self.status=0
                exit()
            elif code==self.pin:
                print("Access Granted")



    def info(self):
        print(f"\nName: {self.name}\nAccount Number: {self.acc_no}\nMobile no.: {self.mobileno}\nBalance(in Rs): {self.balance}")

    def balance_inquiry(self):
        print(f"Account balance: {self.balance}")

    def pin_change(self):
        while True:
            print("Old PIN details:")

            self.user_authentication()
            new=input("Enter New PIN:")
            if new.isdigit():
                confirm=input("Re-enter New PIN:")
                if new==confirm:
                    print ("PIN CHANGED")
                    self.pin=new
                    break
                else:
                    print("PIN doesnot match")
        return new

    def withdrawal(self):
        while True:
            try:
                w_amount = int(input("Enter the amount to be withdrawn: "))
            except:
                print("Invalid input")
                continue
            else:
                break
        if (w_amount > self.balance):
            print("INSUFFICIENT ACCOUNT BALANCE! ")
        elif (w_amount < 100):
            print("Minimum withdrawal limit is Rs 100\nWITHDRAWAL DENIED!")
        elif (w_amount > 10000):
            print("Maximum withdrawal limit is Rs 10000\nWITHDRAWAL DENIED!")
        elif (self.balance - w_amount < 100):
            print("Minimum balance should be Rs.100\nWITHDRAWAL DENIED!")
        else:
            self.balance = self.balance - w_amount
            print("AMMOUNT WITHDRAWN!")
            self.balance_inquiry()
        return self.balance

    def deposit(self):
        while True:
            try:
                d_amount = int(input("Enter amount to be deposited: "))
            except:
                print("Invalid input")
                continue
            else:
                break
        if (d_amount < 100):
            print("Minimum amount for deposition is Rs.100\nDEPOSITION DENIED!")
        elif (d_amount > 10000):
            print("Maximum amount for deposition is Rs.10000\nDEPOSITION DENIED!")
        else:
            self.balance = self.balance + d_amount
            print("AMOUNT DEPOSITED!")
            self.balance_inquiry()
        return self.balance
def start(ATM):
    flag=1
    while True:
        try:
            name = input("Enter Name: ").capitalize()
        except:
            print("USER NOT FOUND!")
            continue
        else:
            break
    a = ATM(name, database[name][0], database[name][1], database[name][2], database[name][3], database[name][4])
    a.user_authentication()
    while True:

        if flag==1:
            # MENU
            print('''
                1) Account Information
                2) PIN Change
                3) Balance Inquiry
                4) Withdrawal
                5) Deposit
                6) Exit
                Select an option- ''',end=" ")
            choice = int(input())

            if choice == 1:
                a.info()
            if choice == 2:
                database[name][3]=a.pin_change()
            if choice == 3:
                a.balance_inquiry()
            if choice == 4:
                database[name][2]=a.withdrawal()
            if choice == 5:
                database[name][2]=a.deposit()
            if choice == 6:
                exit()
        c = input("Do you want to continue? y/n")
        if c == "y" or c == "Y":
            flag = 1
        else:
            flag = 0
            exit()

start(ATM)