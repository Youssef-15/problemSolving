#Problem solving

#Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# .
# D means deposit while 
# W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# .
# Then, the output should be:
# 500
net_amount = 1000
def D():
    while True:
        deposite = int(input("Enter the amount of deposite: "))
        if deposite < 0:
            print("Invalid Input..!")
        elif deposite < 10:
            print("You must Enter a value that is greater than 10")
        else:
            global net_amount
            net_amount = net_amount + deposite
            return net_amount

def W():
    while True:
        withdraw = int(input("Enter the amount of withdrawal: "))
        if withdraw < 0:
            print("Invalid Input..!")
        elif withdraw < 10:
            print("You must Enter a value that is greater than 10")
        else:
            global net_amount
            net_amount = net_amount - withdraw
            return net_amount


while True:
    
    print("---------Choose the number of your Operation---------")
    print("1- Deposite")
    print("2- Withdrawal")
    print("3- Exit")
    choice = input()
    if choice == "1":
        print(D())
    elif choice == "2":
        print(W())
    elif choice == "3":
        break
    else:
        print("Invalid Input..!")