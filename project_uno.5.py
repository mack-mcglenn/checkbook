# cur_balance = 1200.00
# # post_deposit = cur_balance + make_deposit






# This might be excessive, I don't think a welcome is completely necessary but if it is:
# def welcome():
#      greeting = ('Welcome to Your Checkbook!')
#      print(greeting)

# welcome()


def checkbook_menu():
    options = ['View Balance', 'Withdrawal', 'Deposit', 'Exit']
    for i in range(0,len(options)):
        if input == '1':
            'View Balance'
        print(f'{i + 1}: {options[i]}\n')




def get_user_input():
 select_option = input(f'What would you like to do?\n' 
                        '1. View My Balance\n'
                        '2. Make a Withdrawal\n' 
                        '3. Make a Deposit\n' 
                        '4. Exit the Menu\n')


def view_bal():
    bal_message = ('Your current balance is')
    print(bal_message, cur_balance)


#Deposit

def get_deposit_amount():
    global deposit_amount
    deposit_amount = input('What is your deposit amount?:')


def apply_deposit_amount():
    post_deposit = cur_balance + float(deposit_amount)
    print(post_deposit)


#Withdrawal

def get_withdrawal_amount():
    global withdrawal_amount
    withdrawal_amount = input('What is your withdrawal amount?:')


def apply_withdrawal_amount():
    post_withdrawal = cur_balance - float(withdrawal_amount)
    print(post_withdrawal)


def exit_funct():
    exit_message = ('Thank You, Come Again!')
    exit_prompt = ('Would you like to exit?')
    Yes = True
    if input(exit_prompt) == ('Yes') :
        print(exit_message)
        exit()
    else:
        print('Error. Please select again.')

# #Store previous balance for future use:

def read_balance():
    global cur_balance
    with open("balance.txt", 'r') as f:
        cur_balance = f.read()
        return cur_balance
    print(f'The current balance is ${cur_balance}')


def update_balance():
    with open('balance.txt', 'w') as f:
        cur_balance = f.write()
        return cur_balance
    
def write_file(amount):
    with open('balance.txt', 'w') as f:
        cur_balance = f.write(amount)

















 
# welcome()
# checkbook_menu()
# get_user_input()
# view_bal()
# get_deposit_amount()
# apply_deposit_amount()
# get_withdrawal_amount()
# apply_withdrawal_amount()
# exit_funct()
# read_balance()
# update_balance()
# write_file()