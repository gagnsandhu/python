
import json
from auth import user
from util import file_util
from util import label


CONFIG_DATA=label.get_labels()

class Admin(user.User):
    """Admin class inherits User class to access all functions available to User."""
    def see_all_user(self):
        """Only Admin can see all users"""
        file="shadow.json"
        data=file_util.open_file(file)
        users=data.get("users")
        for user in users:
            print(user.get('username'))

    def remove(self):
        """To remove user"""
        username=input("Enter the name of user you want to remove: ")
        file_name="database\shadow.json"
        with open(file_name,"r+",encoding="UTF-8") as file:
            file_data=json.load(file)
            file.seek(0)
            json.dump(file_data,file,indent=4)
        iterator=0
        for item in file_data.get("users"):
            if item.get('username') == username:
                break
            iterator+=1
        if iterator == len(file_data.get("users")):
            print(CONFIG_DATA.get('comman_labels')[0]['user_do_not_exist'])
        else:
            del file_data["users"][iterator]
            print(CONFIG_DATA.get('comman_labels')[0]['user_removed'])
        file="shadow.json"
        file_util.write(file,file_data)
    
    def change_role(self):
        """Making User a Admin or Admin or a User"""
        username=input("Enter the name of user you want to change the role of: ")
        file="shadow.json"
        data=file_util.open_file(file)
        isAdmin=False
        users=data.get("users")
        for user in users:
            if user.get('username') == username:
                if user.get('role') == 'admin':
                    user['role']='user'
                elif user.get('role') == 'user':
                    user['role']='admin'
                isAdmin=True
        if isAdmin is False:
            print(CONFIG_DATA.get('comman_labels')[0]['no_such_user'])
        else:
            data['users']=users
        file_util.write(file,data)

    def unblock(self):
        """To Unblock a user """
        file="balance.json"
        print("List of all suspended users: ")
        data=file_util.open_file(file)
        users=data.get('users')
        for user in users:
            if user.get('suspended') == "True":
                print(user.get('username'))
        try:
            username=input(CONFIG_DATA.get('comman_labels')[0]['unblock'])
            for user in users:
                if user.get('username') == username:
                    if user.get('suspended') == "True":
                        user['suspended']="False"
            data['users']=users
            file_util.write(file,data)
        except ValueError:
            print(CONFIG_DATA.get('comman_labels')[0]['no_such_user'])    
        except Exception as exception_catch:
            print(exception_catch)
            print(CONFIG_DATA.get('comman_labels')[0]['no_such_user'])

    def block(self):
        """To suspend a user"""
        print(CONFIG_DATA.get('comman_labels')[0]['see_all_users'])
        self.see_all_user()
        file='balance.json'
        data=file_util.open_file(file)
        users=data.get('users')
        try:
            username=input(CONFIG_DATA.get('comman_labels')[0]['block'])
            for user in users:
                if user.get('username') == username:
                    user['suspended']="True"
            data['users']=users
            file_util.write(file,data)
            return
        except ValueError:
            print(CONFIG_DATA.get('comman_labels')[0]['no_such_user'])
        except Exception as exception_catch:
            print(exception_catch)
            print(CONFIG_DATA.get('comman_labels')[0]['no_such_user'])
