
Bal = 1000

loop = 1
while loop==1:
    print('********************************')
    print('Type of Action        Bal:', Bal)
    print('********************************')

    print('1. Withdrawal\n2. Balance Enquiry\n3. Deposit')
    print('********************************')

    inp = input('Enter Action Number:')
    if inp.isdigit() == True:
        inp = int(inp)

        if inp == 1:
            wth = input('Enter Amount to Withdraw:')
            wth = int(wth)

            if wth > Bal:
                print('Insufficient Balance')

            else:
                Bal = Bal - wth
                print('Please collect the cash\nRemaining Balance is:', Bal)

            loop = 1

        elif inp == 2:
            print('Your Balance is:', Bal)

            loop = 1

        elif inp == 3:
            dep = input('Enter Amount to be deposited:')
            dep = int(dep)
            Bal = Bal + dep
            print('Balance is:', Bal)

            loop = 1
        else:
            print('Incorrect Input')

            loop = 1


    else:
        print('Invalid input')
        loop = 0




















