#cur_balance = 1200.00
# post_deposit = cur_balance + make_deposit


#My first major change was eliminating my welcome() function and my checkbook() function because they were redundant

#My next major change was relocating my get_user_input() function. Before, I had it listed near the top. That resulted in an error
#message because vscode likes for the functions to be listed in order of definition

def view_bal(cur_balance):
    bal_message = ('Your current balance is $')
    print(bal_message, cur_balance)
    return cur_balance


# I improved my exit_function by adding a 'No' option if the user doesn't want to exit and instead wants to return to the menu.
#I also simplified my input syntax so that the user doesn't have to fully type out 'Yes' or 'No'
# If the user selects something other than 'Y' or 'N', they will recieve an error message and be directed back to the main menu.
def exit_funct():
    exit_message = ('Thank You, Come Again!')
    exit_prompt = input('Would you like to exit? Select Y for Yes or N for No')
    Yes = True
    if exit_prompt == ('Y') :
        print(exit_message)
        exit()
    elif exit_prompt == ('N'):
        return get_user_input(cur_balance)
    else:
        print('Error. Please select again.')



#Deposit code
def get_deposit_amount():
    global deposit_amount
    deposit_amount = input('What is your deposit amount?: ')


def apply_deposit_amount():
    deposit_amount = input('What is your deposit amount?: ')
    post_deposit = cur_balance + float(deposit_amount) #Since my write files are strings, I have to convert my values to floats
    # here to update my balance.
    #I improved my deposit and withdrawal functions by adding an input function which gives the user the option to view their
    #updated balance or return to the main menu
    update_dep_ms= input("""Your deposit has been applied. Would you like to see your new balance?
    Press Y for yes or N to return to main menu""")
    update_balance(post_deposit)
    if update_dep_ms == 'Y':
        cur_balance == view_bal(post_deposit)
        return view_bal(post_deposit)
    elif update_dep_ms == 'N':
        return get_user_input(cur_balance)
    else:
        print('Command unkown. Returing to main menu')

#Withdrawal code

def get_withdrawal_amount():
    global withdrawal_amount
    withdrawal_amount = input('What is your withdrawal amount?:')


def apply_withdrawal_amount():
    withdrawal_amount = input('What is your withdrawal amount?:')
    post_withdrawal = cur_balance - float(withdrawal_amount)
    update_wd_ms = input("""Your withdrawal has been applied. Would you like to see your new balance?
    Press Y for yes or N to return to main menu""")
    update_balance(post_withdrawal)
    if update_wd_ms == 'Y':
        cur_balance == view_bal(post_withdrawal)
        return view_bal(post_withdrawal)
    elif update_wd_ms == 'N':
        return get_user_input(cur_balance)
    else:
        print('Command unknown. Returning to main menu')
    

#There have been several updates to my user input function:
#1. Identifying cur_balance as my argument. Before, the function was defined as get_user_input(). Adding the argument of cur_balance throughout the 
# definition of the function allows my most current balance to be pulled from my balance.txt file w/o breakage by ensuring that I have the most up-to-date
# balance info after my deposits/withdrawals have been applied to my starting amount.

def get_user_input(cur_balance):
    select_option =input(f'What would you like to do?\n' 
                        '1. View My Balance\n'
                        '2. Make a Withdrawal\n' 
                        '3. Make a Deposit\n' 
                        '4. Exit the Menu\n')
    if select_option == '1':
        view_bal(cur_balance)
        return cur_balance
    elif select_option == '2':
        cur_balance= apply_withdrawal_amount()
        return cur_balance
    elif select_option == '3':
        cur_balance =apply_deposit_amount()
        return cur_balance
    elif select_option == '4':
        exit_funct()
        
#get_user_input()
#Store previous balance for future use:

def read_balance():
    # global cur_balance
#my cur_balance has to be saved as a float in order to function properly, but ONLY in my read file. If I try to save it as a float in my write_file or 
    # update_balance functions, I'll get an error message because the write function only accepts strings.
    with open("balance.txt", 'r') as f:
        cur_balance = float(f.read())
    print(f'Welcome back! The current balance is ${cur_balance}')
    return cur_balance


def update_balance(cur_balance):
    with open('balance.txt', 'w') as f:
        f.write(str(cur_balance))

    
def write_file(amount):
    with open('balance.txt', 'w') as f:
        cur_balance = f.write(str(amount))

cur_balance= read_balance()
#Changing my cur_balance variable from an absolute value like it was before eliminates concerns that my balance won't hold after I reopen the program


while True:
    cur_balance= get_user_input(cur_balance)
#This simplified while loop infers that while my get user input function is true with my cur_balance argument in place, the subfunctions(?) within my
#get_user_input loop can continue to run. If I remove the cur_balance argument from my while loop and try to run the project, it won't launch bc I'm missing
#the positional argument








 
welcome()
get_user_input()
view_bal()
get_deposit_amount()
apply_deposit_amount()
get_withdrawal_amount()
apply_withdrawal_amount()
exit_funct()
read_balance()
update_balance()
write_file()