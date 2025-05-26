import time
import os
import sys

# #Setting initial balance to my current bank balance, the assumption made here is everyone is as rich as I am
balance = 0.00
b = '-'
#
# #Funtion created to clear the current terminal for any of the 3 main OSs
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def n():
    null = input()

def showBalance(balance):
    clear_screen()
    ast()
    print("\n\tAutomated Teller Machine")
    ast()
    print(f"\n\n\n 0. Balance = ${balance:.2f}{b:-<21}\n\n")
    ast()

def deposit(balance):
    dep = float(input("Enter amount to be deposited: "))
    balance += dep
    time.sleep(1)
    print(f"Amount being deposited now..")
    for i in range(4):
        time.sleep(1)
        print(".", end="")
    print("\n")
    showBalance(balance)
    return balance


def withdraw(balance):
    amt = float(input("Enter amount to be withdrew: "))
    if amt > balance:
        print("ERROR, Insufficient Funds")
        for i in range(3):
            time.sleep(1)
            print(".",end="")
        print("\n")
        showBalance(balance)
    else:
        balance -= amt
        time.sleep(1)
        print(f"Amount being withdrawn now..")
        for i in range(3):
            time.sleep(1)
            print(".",end="")
        print("\n")
        showBalance(balance)
    return balance



def goAgain():
    ast()
    print("\n\tAutomated Teller Machine")
    ast()
    print("\nWould you like to do another transaction"
          f"\n\n 1. Yes{b:-<33}"
          f"\n 2. No{b:-<34}\n")
    ast()

    choice = int(input("\n\n\nInput: "))
    if choice == 1:
        return True
    elif choice == 2:
        clear_screen()
        return False
    else:
        print("\n\nInvalid Command")
        time.sleep(3)
        clear_screen()
        goAgain()
    return None




def ast():
    for y in range(40):
        print("*",end="")








while True:
    clear_screen()
    ast()
    print("\n\tAutomated Teller Machine")
    ast()
    print("\n 0. Select the desired option below(1-4)"
          "\n 1. Show Balance------------------------"
          "\n 2. Deposit-----------------------------"
          "\n 3. Withdraw----------------------------"
          "\n 4. Exit--------------------------------")
    ast()
    print("\n")
    opt = int(input("\n\nSelect the option you would like to do: "))

    match opt:
        case 1:
            showBalance(balance)
            print("\n")
            time.sleep(2)
            clear_screen()
            if not goAgain():
                break


        case 2:
            balance = deposit(balance)
            print("\n")
            time.sleep(2)
            clear_screen()
            if not goAgain():
                break

        case 3:
            balance = withdraw(balance)
            print("\n")
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            if not goAgain():
                break
        case 4:
            print("\n\nHave a good day!!")
            print("\n")
            time.sleep(1)
            clear_screen()
            break

        case _:
            break

