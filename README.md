# mission_python
#def start():
Bal = 1000
print('********************************')
print('Type of Action     Bal:', Bal)
print('********************************')

print('1. Withdrawal\n2. Balance Enquiry\n3. Deposit')
print('********************************')

inp = input('Enter Action Number:')
if inp.isdigit() == True:
    inp = int(inp)

    if inp == 1:
        wth = input('Enter Amount to Withdraw:')
        wth = int(wth)
        Bal = Bal - wth
        if Bal < 0:
            print('Insufficient Balance')
        else:
            print('Please collect the cash\nRemaining Balance is:', Bal)



    elif inp == 2:
        print('Your Balance is:', Bal)


    elif inp == 3:
        dep = input('Enter Amount to be deposited:')
        dep = int(dep)
        Bal = Bal + dep
        print('Balance is:', Bal)


    else:
        print('Incorrect Input')
    # start()

else:
    print('Invalid input')
    # start()









