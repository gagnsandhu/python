import hashlib
from models.shadow import Shadow


class UserLogin():
    @staticmethod
    def user_login(username, password):
        obj=Shadow.query.get(username)
        hash_password=hashlib.sha512(password.encode()).hexdigest()
        if obj is None:
            return 1
        if obj.username == username and obj.password != hash_password:
            return 2
        return 3
        

