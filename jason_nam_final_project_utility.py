#-------------------------------------------------------------------------------
# Student Name: 
# Assignment: Final Project
# Python version:
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation, Lectures
#-------------------------------------------------------------------------------
# Notes: Any general comments to the grader
#-------------------------------------------------------------------------------

import random, string

def is_username_taken(username, users):
    '''
    Returns False if username already exists in users (dictionary)
    otherwise returns True
    '''
    #your code here
    #uses count as a check to see if the username was caught
    count = 1
    for x in users:
        if x == username:
            count = count + 1
    if count == 1:
        return True
    if count != 1:
        return False
            
    
def validate_username_password(username, password, users):
    '''
    Returns False if username and password do not match or username
    does not exist, otherwise returns True
    '''
    #your code here
    # combined this function with validate_existing_user
    if users[username][2] == password:
        return True
    else:
        return False
    
def new_user(users):
    '''
    Creates a new user with first name, last name, username
    password, random wallet number, initial balance.
    Returns None
    '''
    print('\n\nNew user')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    x = 0
    while x==0:
        #your code here
        #ask for username
        username = input("Enter username: ")
        #if username already taken -> print a message and go back to while
        if is_username_taken(username, users) == False:
            print("User name is taken")
            
        #otherwise ask for password and break
        if is_username_taken(username, users) == True:
            a = 0
            while a==0:
                password = input("Enter a password (6-12 characters): ")
                if len(password)>5 and len(password)<13:
                    a =a - 1
                    x= x -1
    #generate wallet number
    if is_username_taken(username, users) == True:
        wallet_n = generate_wallet_number()
        print("Your wallet number is " + wallet_n)
    #ask for other information
    if is_username_taken(username, users) == True:
        wallet_b = input("Enter initial wallet deposit: ")
    #add key-value pair to the dictionary users
    if is_username_taken(username, users) == True:
        users.update({username:[first_name,last_name,password,wallet_n,wallet_b]})
    print("E-wallet created for " + username)

def validate_existing_user(users):
    '''
    Existing user needs to validate with username and password and
    maximum chances is three. Returns username if login successful
    otherwise returns False if maximum chances are used. 
    '''
    #counter
    max_chance = 0
    #your code here
    #gives 3 tries to guess password and username reutnrs user name if matched, reutrns false if not
    while max_chance<3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            if users[username][2] == password and username in users:
                return username
        except:
            print("no match")
            max_chance +=1
            
    if max_chance == 3:
        return False
        
    
def validate_amount(users,username,amount):
    '''
	Returns True if amount to withdraw is less than the
    current balance otherwise returns False
    '''
    #your code here
    #checks to see if enough funds are available for process
    if int(users[username][4]) > int(amount):
        return True
    else:
        return False
    

def deposit(users, username, amount):
    '''
    Deposits amount to user's wallet and prints
    informational message
    '''
    #your code here
    #prints info you need as the program attempts to deposite amount given
    print("previous balance - " + users[username][4])
    users[username][4] = str(int(amount) + int(users[username][4]))
    print(amount + " deposited into acount")
    print("new balance - " + users[username][4])
    
    
def withdraw(users,username,amount):
    '''
    Withdraws amount if amount is valid otherwise
    prints informational message
    '''
    #your code here
    #prints extra info and attempts to withdraw from dictionary's list
    print("previous balance - " + users[username][4])
    users[username][4] = str(int(users[username][4])-int(amount))
    print(str(amount) + " withdrawed from acount")
    print("new balance - " + users[username][4])

def summary(users, username):
    '''
    Displays current summary of a user wallet
    '''
    #prints all username's information
    print("First Name: " + users[username][0])
    print("Last Name: " + users[username][1])
    print("Password: " + users[username][2])
    print("Wallet Number: #" + users[username][3])
    print("Current Wallet Balance: $" + users[username][4])
def transfer(users, sender, receiver, amount):
    '''
    Transfer money from sender (username) to receiver (username)
    if amount is valid AND if receiver username exists
    '''
    #transfers money from one account to another by converting list values
    print("Withdraw $" + amount)
    print("User gmason current wallet balance = " + users[sender][4])
    users[sender][4] = str(int(users[sender][4]) - int(amount))
    users[receiver][4] = str(int(users[receiver][4]) + int(amount))
    print("Transferred $" + amount + " from " + sender + " to " + receiver)
    print("New user gmason wallet balance = " + users[sender][4])
    
    
def generate_wallet_number():
        '''
        Returns 4 character random wallet number
        '''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))


