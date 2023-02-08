class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show(self):
        print("Balance: ", self.balance)

    def deposit(self, money):
        self.balance += money
        print("The current balance:", self.balance)
    
    def withdraw(self, money):
        if money > self.balance:
            print("Withdrawal of funds cannot exceed the available balance")
            exit()

        else:
            self.balance -= money
            print("The current balance:", self.balance)


def login():
    return str(input("Login: "))

def op():
    return str(input("Select an operation: balance, deposit, withdraw: "))

def op1():
    return str(input("Select an operation: deposit, withdraw, exit: "))

def check(operation, flag):
    ok = False
    cnt = 0
    while ok == False:
        if cnt == 2:
            print("Number of attempts exceeded")
            exit()
        print("Operation is not available, please try again")
        operation = op()
        if((operation == "deposit" or operation == "withdraw" or operation == "balance") and flag == 1):
            ok = True
            return operation
        elif((operation == "deposit" or operation == "withdraw" or operation == "exit") and flag == 2):
            ok = True
            return operation
        cnt += 1


p1 = Account("John", 570000)
p2 = Account("Arman", 36660)
p3 = Account("Smith", 4000)
p4 = Account("Saken", 185960)
p5 = Account("Daryn", 960000)

client = [p1, p2, p3, p4, p5]


p = login()
ok = False
for i in client:
    if p == i.owner:
        p = i
        ok = True
        break

if ok == False:
    cnt = 0
    while ok == False:
        if cnt == 2:
            print("Number of attempts exceeded")
            exit()
        print("User is not exist, please try again")
        p = login()
        for i in client:
            if p == i.owner:
                p = i
                ok = True
                break
        cnt += 1
    

ok = True
operation = op()
if operation != "deposit" and operation != "withdraw" and operation != "balance":
    flag = 1
    operation = check(operation, flag)

if operation == "balance":
    p.show()
    operation = op1()

    if operation != "deposit" and operation != "withdraw" and operation != "exit":
        flag = 2
        operation = check(operation, flag)



if operation == "exit":
    exit()

money = int(input("Amount of money: "))


if operation == "deposit":
    p.deposit(money)
    
  
elif operation == "withdraw":
    p.withdraw(money)