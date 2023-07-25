"""
hashlib : to store passowrd as Hash
"""
import hashlib
import getpass
import json
from util import file_util
from util import label


CONFIG_DATA = label.get_labels()

class User():
    """User Class : All functions avaialble to user is defined here"""
    def __init__(self):
        print("Welcome!!!")

    def check_sus(self,username):
        """Checking if a user is suspended or not."""
        file="balance.json"
        data=file_util.open_file(file)
        users=data["users"]
        for user in users:
            if user.get('username')==username:
                if user.get('suspended')=="True":
                    return True
                else:
                    return False
        return False

    def login(self,username,password):
        """Login Function which will check hash"""
        file="shadow.json"
        data=file_util.open_file(file)
        unames=data.get("users")
        successful_login=False
        role=''
        for user in unames:
            if user.get('username')==username:
                '''salt here used is the username itself which provide more security to the password'''  
                salt=username+password
                hashed=hashlib.sha512(salt.encode())
                if user.get('password') == hashed.hexdigest():
                    isSuspened=self.check_sus(username)
                    if isSuspened is True:
                        print(CONFIG_DATA.get('comman_labels')[0]['suspend'])
                        exit()
                    print(CONFIG_DATA.get('comman_labels')[0]['login'])
                    successful_login=True
                    role=user.get('role')
                    return role

                else:
                    print("Incorrect Password!!\n")
                    file_name='config\config.json'
                    fhandle=open(file_name)
                    data=json.load(fhandle)
                    attempts=data.get("no_of_attempts")
                    for _ in range(int(attempts)):
                        passw=getpass.getpass(CONFIG_DATA.get('comman_labels')[0]['enter_password'])
                        hashed=hashlib.sha512(passw.encode())
                        if attempts == 0:
                            exit()
                        if user["password"] == hash.hexdigest():
                            print("SuccessFull !!!")
                            return user['role']
                        else:
                            print(f'You only have {attempts} left.')                            
        if successful_login is False:
            print(CONFIG_DATA.get('comman_labels')[0]['user_do_not_exist'])
            return None

    def check_balance(self,username):
        """To view Balance"""
        print("IN balance function")
        file="balance.json"
        data=file_util.open_file(file)
        users=data.get("users")
        for user in users:
            if user.get('username') == username:
                print("\t\tThe available balance is: "+user.get('balance'))
                return user.get('balance')   
        return None  

    def deposit_bal(self,username):
        """To Deposit Money"""
        amt=input("Enter amount you want to Deposit: ")
        while True:
            if amt.isdigit():
                break
            else:
                print(CONFIG_DATA.get('comman_labels')[0]['valid_input'])
                amt=input("Enter again: ")
        config_file="config\config.json"
        conf_file=open(config_file)
        data=json.load(conf_file)
        max_amt=data.get('max_amount')
        file="shadow.json"
        file_data=file_util.open_file(file)
        shadow_data=file_data['users']
        role=''
        for user in shadow_data:
            if user.get('username') == username :
                role=user.get('role')
        if int(amt)>max_amt and role!='admin':
            print("Contact Admin...")
        else:
            balance_file="balance.json"
            data=file_util.open_file(balance_file)
            users=data.get("users")
            for user in users:
                if user.get('username')==username:
                    user['balance']=str(int(user.get('balance'))+int(amt))
                    print(user.get('balance'))
            data['users']=users
            file_util.write(balance_file,data)

    def withdraw(self,username,amt):
        """To Withdraw Money"""
        while True:
            if str(amt).isdigit():
                break
            else:
                print(CONFIG_DATA.get('comman_labels')[0]['valid_input'])
                amt=input("Enter again: ")
        file="balance.json"
        data=file_util.open_file(file)
        users=data.get("users")
        for user in users:
            if user.get('username') == username:
                if int(user.get('balance'))>=int(amt):
                    user['balance']=str(int(user.get('balance'))-int(amt))
                    print(user.get('balance'))
                else:
                    print(CONFIG_DATA.get('comman_labels')[0]['not_enough_balance'])
        data['users']=users
        file_util.write(file,data)   

    def see_all_stocks(self):
        """All Stocks with their Tokens will be visible"""
        file="stocks.json"
        data=file_util.open_file(file)
        for token,stk in data.items():
            print(stk+"  "+token)

