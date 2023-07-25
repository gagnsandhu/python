"""
getpass to hide password while taking input
"""
import getpass
import json
from auth import user
from auth import signup
from trade import trade
from auth import admin_
from util import label

COMMAN_LABEL=label.get_labels()
CURRENT_BALANCE=''

def admin_menu():
    """ Admins Menu"""
    global CURRENT_BALANCE
    if USERNAME=='admin' or ROLE=='admin':
        print(COMMAN_LABEL.get('comman_labels')[0]['welcome_admin'])
        admin=admin_.Admin()
        while True:  
            config_file='config/config.json'
            file=open(config_file)
            admin_menu=json.load(file)
            for statement in admin_menu.get('admin_menu'):
                print(statement)
            choice=input(COMMAN_LABEL.get('comman_labels')[0]['choice']).lower()
            match choice :
                case 'a':
                    admin.see_all_user()
                case 'b':
                    admin.remove()
                case 'c':
                    admin.change_role()
                case 'q':
                    break
                case 'e':
                    admin.unblock()
                case 'd':
                    admin.block()
                case other:
                    print(COMMAN_LABEL.get('comman_labels')[0]['valid_input'])  

def user_menu():
    """ User Menu"""
    while True:
        global CURRENT_BALANCE
        config_file='config/config.json'
        file=open(config_file)
        users_menu=json.load(file)
        for statement in users_menu.get('user_menu'):
                print(statement)
        choice_=(input(COMMAN_LABEL.get('comman_labels')[0]['choice']).lower())
        match choice_:
            case '1':
                CURRENT_BALANCE = user.check_balance (USERNAME)
            case '2':
                user.deposit_bal(USERNAME)
            case '3':
                amt=input(COMMAN_LABEL.get('comman_labels')[0]['amount_to_withdraw'])
                while True:
                    if amt.isdigit():
                        break
                    else:
                        amt=input(COMMAN_LABEL.get('comman_labels')[0]['valid_input'])
                user.withdraw(USERNAME,int(amt))
            case '4':
                ret=trade.trade(CURRENT_BALANCE)
                if ret is None:
                    print(COMMAN_LABEL['comman_labels'][0]['session_end'])
                else:
                    user.withdraw(USERNAME,ret)
            case '5':
                user.see_all_stocks()
            case 'q':
                break
            case other:
                print(COMMAN_LABEL.get('comman_labels')[0]['valid_input'])

greet=label.get_labels()
for statement in greet.get('greet'):
    print(statement)
user=user.User()
USERNAME=''
PASSWORD=''
ROLE=''

while True:
    choice=input(COMMAN_LABEL.get('comman_labels')[0]['login_signup']).lower()
    match choice:
        case 'yes':
            print("Please Sign in..")
            USERNAME=input("Enter USERNAME: ")
            PASSWORD=getpass.getpass("Enter password : ")
            ROLE=user.login(USERNAME,PASSWORD)
            if ROLE is not None:
                break
        case 'no':
            print("Sign Up")
            signup.sign_up()
            USERNAME=input(COMMAN_LABEL.get('comman_labels')[0]['enter_username'])
            password=getpass.getpass(COMMAN_LABEL.get('comman_labels')[0]['enter_password'])
            user_ = user.login(USERNAME,password)
            if user_:
                break
            else:
                continue
        case 'q':
            exit()
        case other:
            print(COMMAN_LABEL.get('comman_labels')[0]['valid_input'])

while True:
    if ROLE != 'admin':
        user_menu()
        break
    elif ROLE=='admin':
        config_file='config/config.json'
        file=open(config_file)
        admin_traversal=json.load(file)
        for statement in admin_traversal.get('admin_traversal'):
            print(statement)
        user_input=input("Enter choice: ")
        match user_input:
            case '1':
                user_menu()
            case '2':
                admin_menu()
            case 'Q':
                exit()
            case 'q':
                exit()
            case other:
                print(COMMAN_LABEL.get('comman_labels')[0]['valid_input'])
