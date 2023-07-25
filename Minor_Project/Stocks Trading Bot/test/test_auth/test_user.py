from auth import user

user=user.User()
def test_suspended():
    username='yogesh'
    bool=user.check_sus(username)
    assert bool==False

def test_login():
    username='yogesh'
    password='123456'
    bool=user.login(username,password)
    assert bool==None

def test_balance():
    username='yogesh'
    bool=user.check_balance(username)
    assert bool!=None

def test_deposit():
    username='yogesh'
    amount=100
    bool=user.deposit(username,amount)
    assert bool!=None

def test_withdraw():
    username='yogesh'
    amount=100
    bool=user.withdraw(username,amount)
    assert bool!=None