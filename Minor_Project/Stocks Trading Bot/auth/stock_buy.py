from models.details import Detail
from db import db
from models.users_stock import UserStock


def check_balance(price,balance):
    if balance <= price:
        return 1
    return 2

def add_stock(data,id):
    stock={
        "user_id": id,
        "stocks":data['stock'],
        "quantity":data['quantity']

    }
    obj=UserStock(**stock)
    db.session.add(obj)
    db.session.commit()







