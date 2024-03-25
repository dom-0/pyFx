
import pytest

import pytest_framework.my_functions as my_functions

def test_add():
    res = my_functions.add(3, 4)
    assert res == 7

# def test_divide_by_zero():
#     res = my_functions.divide(10, 0)
#     assert True

def test_divide_by_zero():  ## Raising an error
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10, 0)


def test_divide():
    res = my_functions.divide(10, 5)
    assert res == 2

def test_add_two_strings():
    res = my_functions.add("I like ", "burgers")
    assert res == "i like burgers"
