import pytest
# from main import user_menu
# import main
from auth import signup
from util import file_util


def test_functions():
    Name=signup.get_name()
    username="jatt_lyf"
    bool=(username in Name)
    print(Name)
    assert bool is True 

    # assert True