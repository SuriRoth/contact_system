balance = 256.35

while True:
    userOption = input('''Welcome to our Bank ATM!
What would you like to do today?
    Enter 1 to Check Balance
    Enter 2 to Deposit Funds
    Enter 3 to Withdraw Funds
    Enter 4 to Cancel and Exit \n''')

    if userOption == '1':
        print ('\n Your current balance is: $'+ str(balance) + '\n')
        choice = input('Enter 1 to go back to the main menu \n'
                        'Enter 2 to Cancel and Exit \n' )
        if choice != '1':
            print('\n Ok, Thank you for choosing our bank!')
            break
        else:
            print('You will be redirected to the main menu.')
    
    elif userOption == '2':
        try:
            deposit = float(input('\n How much would you like to deposit today? \n '))
            if deposit > 0:
                balance = balance + deposit
                print ('\n Your balance is now: $' + str(balance))
            else:
                print('\n Invalid deposit amount. Please enter a positive value. \n')
        except ValueError:
            print('\n Invalid input. Please enter a valid number for the deposit amount. \n')
            
        choice = input('Enter 1 to go back to the main menu \n'
                        'Enter 2 to Cancel and Exit \n' )
        if choice != '1':
            print('\n Ok, Thank you for choosing our bank!')
            break
        else:
            print('You will be redirected to the main menu.')
    
    elif userOption == '3':
        try:
            withdraw = float(input('\n How much would you like to withdraw today? \n'))
            if withdraw > 0: 
                if withdraw <= balance:
                    balance = balance - withdraw
                    print ('\n Your balance is now: $' + str(balance)+ '\n')
                else: 
                    print ('\n You do not have enough funds in your account. \n')
            else:
                print('\n Invalid withdrawal amount. Please enter a positive value. \n')              
        except ValueError:
            print('\n Invalid input. Please enter a valid number for the withdrawal amount. \n')
        
        choice = input('Enter 1 to go back to the main menu \n'
                        'Enter 2 to Cancel and Exit \n' )
        if choice != '1':
            print('\n Ok, Thank you for choosing our bank!')
            break
        else:
            print('You will be redirected to the main menu.')

            
    elif userOption == '4':
        print('\n Ok, Thank you for choosing our bank!')
        break
    
    else: print('\n You entered an invalid option \n')