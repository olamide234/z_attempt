"""This have a lookalike to how a bank operate. Login, Register a user, generate account number, deposit and withdraw funds, etc"""
#login
#register
#bankaccount

import random 
database = {} #dictionary

#initializing the bank account
def initiate():
    
    print('Welcome to bank Apex')

    haveAccount= int(input('Do you have an account with us: 1 (yes) 0 (no) \n'))
    
    if (haveAccount == 1):
         return login()
    elif (haveAccount == 0):
        return register()
    else:
        print('You have selected a wrong option')
        return initiate()

def register():     
    print('Register')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Enter a password for yourself? \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [email, first_name, last_name, password]
    
    print('Your account number is: %d' % accountNumber)
    print('Please keep it safe \n')

    # return database
    return login()

def login():
    print('Login to your account')

    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountNumber, accountDetails in database.items():
        if (accountNumber == accountNumberFromUser):
            if (accountDetails[3] == password):
                return bankOperation(accountDetails)
            else:
                print('Invalid account number or password entered')
                return login()
        else:
            print('Invalid account number or password entered')
            return login()

    

def bankOperation(user):
    print('Welcome %s %s' % (user[1], user[2]))
    
    option = int(input('What will you like to do? (1) Withdraw (2) Deposit (3) Logout (4) Exit \n'))

    if (option == 1):
        return withrawalOperation()
    elif (option == 2):
        return depositOperation()
    elif (option == 3):
        return logout()
    elif (option == 4):
       return exits()
    else:
        print('Invalid option selected')
        return bankOperation(user)
    

def withrawalOperation():
    print('Withrawal')
    toWithdraw = int(input('How much would you like to withdraw \n'))
    print("\ntake your cash\n")
    login()

def depositOperation():
    print('Deposit')
    toDeposit = int(input('How much would you like to deposit? \n'))
    balance = toDeposit
    print("\nCurrent Balance: %s \n" % balance)
    login()

def generateAccountNumber():
    print('Your account has been created')
    print('account number generator')
    return random.randrange(1111111111, 9999999999)

def logout():
    print('Logging out')
    login()

def exits():
    print('Thanks For Coming! \nBye for now!!')

#ACTUAL SYSTEM WORKING
initiate()