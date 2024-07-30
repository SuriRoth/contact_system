balance = 256.35

while True:
    userOption = input('What would you like to do today?\n'
                   'Enter 1 to Check Balance \n'
                   'Enter 2 to Deposit Funds \n'
                   'Enter 3 to Withdraw Funds \n'
                   'Enter 4 to Cancel and Exit \n')

    if userOption == '1':
        print ('\nYour current balance is: $'+ str(balance) + '\n')
    
    elif userOption == '2':
        try:
            deposit = float(input('\n How much would you like to deposit today? \n '))
            if deposit > 0:
                balance = balance + deposit
                print ('\nYour balance is now: $' + str(balance))
            else:
                print('\nInvalid deposit amount. Please enter a positive value. \n')
        except ValueError:
            print('\nInvalid input. Please enter a valid number for the deposit amount. \n')
    
    elif userOption == '3':
        
        try:
            withdraw = float(input('\nHow much would you like to withdraw today? \n'))
    
            if withdraw > 0: 
                if withdraw <= balance:
                    balance = balance - withdraw
                    print ('\nYour balance is now: $' + str(balance)+ '\n')

                else: 
                    print('\nInvalid withdrawal amount. Please enter a positive value. \n')

            elif withdraw > balance:
                print ('\nYou do not have enough funds in your account. \n')
                
        except ValueError:
            print('\nInvalid input. Please enter a valid number for the withdrawal amount. \n')

            
    elif userOption == '4':
        print('\nOk, Thank you for choosing our bank!')
        break
    
    else: print('\nYou entered an invalid option \n')