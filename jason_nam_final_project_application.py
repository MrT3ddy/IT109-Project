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

import jason_nam_final_project_utility as u #change the name of the file

def build_dict():
    '''
    Returns a dictionary created from input file (user_list.txt)
    where key is an existing username and
    value is a list of fistname, lastname, wallet number and balance.
    '''
    #your code here
    y = []
    firstDict = {}
    file = open("user_list.txt", "r")
    placeholder = file.read().splitlines()
    for x in placeholder:
        y.append(x.split("|"))
    for x in y:
        firstDict.update({x[0]: [x[1],x[2],x[3],x[4],x[5]]})
    return firstDict
    
        

def write_to_file(users):
    '''
    Writes the updated user information to user_list.txt file
    '''
    #your code here
    #call this function from Exit option
        
            
def main():
    
    print('\n\n********** Welcome to e-Wallet! *************')
    users= build_dict()
    option = 0
    QUICK_WITHDRAW_AMOUNT = 20
    
    while option!=3: #outer loop - main menu option
        #your code here
        
        #display main menu options
        print("Main Menu \n 1. New User \n 2. Sign in \n 3. Exit Application: ")
        
        option = int(input('Enter option (1-3): '))
        
        if option == 1:
            u.new_user(users)#create new user

     
        elif option == 2:
            username = u.validate_existing_user(users)
            
            if username != False: #if username is not False
                while True: #inner while loop - sub menu option
                    #your code here
                    print("Login Succesful. Welcome ")
                    #display sub menu option
                    print("\n Existing User Menu \n 1. Add money to Wallet \n 2. Withdraw money to bank \n 3. Quick withdraw \n 4. Transfer \n 5. Wallet Summary \n 6. Logout")
                    submenu_option = int(input('Enter option (1-6): '))


                    if submenu_option == 1:
                        #your code here
                        #define try-except block
                        try:
                        #ask for amount to deposite
                            amount = input("Enter amount to deposite: ")
                        #valid amount will deposit
                            u.deposit(users,username,amount)
                        #Invalid amount (exception) wil take the user to the main menu
                        except:
                            print("Invalid format [non numeric], returning to main menu")

                   
                    elif submenu_option == 2:
                        #your code here
                        #define try-except block
                        
                        try:
                        #ask for amount to deposite
                            amount = input("Enter amount to withdraw: ")
                            validation = u.validate_amount(users,username,amount)
                            if validation == True:
                                u.withdraw(users,username,amount)
                            else:
                                print("Invalid Amount")
                        #valid amount will withdraw
                            
                        #Invalid amount (exception) wil take the user to the main menu
                        except:
                            print("Invalid format [non numeric] or value is to large, returning to main menu")

                        
                        

                    elif submenu_option == 3:
                        
                        #your code here
                        z = 20
                        validation = u.validate_amount(users,username,z)
                        
                        try:
                            if validation == True:
                                u.withdraw(users,username,z)
                        except:
                            print("Invalid format [non numeric] or value is to large, returning to main menu")
            
                    
                    elif submenu_option == 4:
                        username_t = input("Enter username to transfer: ")
                        amount_t = input("Enter amount to transfer: ")
                        if u.validate_amount(users,username,amount_t)==True and u.is_username_taken(username, users)==False:
                            try:
                                u.transfer(users,username,username_t,amount_t)
                            except:
                                print("Invalid datatype, or username")
                        else:
                            print("-Invalid request-")
                        

                    elif submenu_option == 5:
                        
                        #your code here
                        u.summary(users,username)
                    elif submenu_option == 6:
                        print('Logging out. Returning to main menu. ')
                        break #break out of sub-menu option

                    else:
                        print('Invalid Option. Returning to main menu. ')
            
        elif option == 3:
            exit()
        else:
            print('Invalid option! Returning to main menu. ')
           
    
if __name__== '__main__':
    main()


main()
