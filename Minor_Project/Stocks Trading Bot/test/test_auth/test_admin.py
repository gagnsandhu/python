from auth import admin_


admin=admin_.Admin()
def test_see_all_user():
    admin.see_all_user()
    assert True

def test_remove():
    admin.remove()
    assert True


