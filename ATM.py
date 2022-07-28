print("Welcome to National Bank of Uranius")
restart = ("Y")
chances = 3
balance = 475.48

while chances >= 0:
    pin = int(input("Enter Your PIN: "))
    if pin == (1234):
        print("Please Select your Desired Option\n")
        while restart not in ('n', 'NO', 'no', 'N'):
            print("Press 1 for Balance Check")
            print("Press 2 for Withdrawl")
            print("Press 3 for Deposite")
            print("Press 4 to Return Card\n")
            option = int(input(">>> "))
            if option == 1:
                print("Your Balance is $", balance, "\n")
                restart = input(
                    "For Main Menu Please Press 'Y' or You can press 'N' to finish Transaction\n>>> ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(
                    input("How Much Would Like to Withdraw? \n$50/ $100/ $500/ $1000 \n>>> "))
                if withdrawl in [50, 100, 500, 1000]:
                    if withdrawl > balance:
                        print("Insufficiant Balance")
                    else:
                        balance -= withdrawl
                        print("\nYour Current Balance is: $", balance)
                        restart = input(
                            "For Main Menu Please Press 'Y' or You can press 'N' to finish Transaction\n>>> ")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("Thank You")
                            break
                elif withdrawl != [50, 100, 500, 1000]:
                    print("Invalid Amount, Please Enter Valid Amount\n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Please Enter You Amount"))
            elif option == 3:
                deposite = float(input("Enter Amount: "))
                balance += deposite
                print("\nYour Current Balance is: $", balance)
                restart = input(
                    "For Main Menu Please Press 'Y' or You can press 'N' to finish Transaction\n>>> ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait.....\n.........................[100%]\n")
                print("Thank You")
                break
            else:
                print("Please Correct Option from the Menu.\n")
                restart = ("y")
    elif pin != (1234):
        print("Incorrect PIN.\nPLEASE TRY AGAIN")
        chances -= 1
        if chances == 0:
            print("Sorry too many Attempt")
