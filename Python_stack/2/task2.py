"""
Five digital number given. Count of ten raise to a power of ones count.
Then multuply this number at hundreds count,
and then divide it on the difference between ten thousands count and thousand count. 
Example for 46275: 
7(tens) ** 5 (ones) * 2 (hundreds) / (4(ten thousands) - 6(thousands)) = -16807.0
"""
import pytest

class NotFiveDigital(Exception):
    """
    Exception for the case user inputs not five digital number
    """
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"{self.number} is not five digital number"

def get_answer(number:str):
    """
    Getting an answer of the task
    """
    if len(number) == 5:
        return (int(number[-2]) ** int(number[-1]) * int(number[-3])
                ) / (int(number[-5]) - int(number[-4]))
    else:
        raise NotFiveDigital(number)

def test():
    """
    Pytest test
    """
    assert get_answer("46275") == -16807.0
    assert get_answer("72845") == 1638.4
    assert get_answer("23222") == -8
    assert get_answer("57395") == -88573.5
    assert get_answer("79276") == -117649.0

def test_zero_division():
    """
    Checking exception for zero division error
    """
    with pytest.raises(ZeroDivisionError):
        get_answer("11111")

def test_not_five_digits_short():
    """
    Checking exception for not five digits numbers
    """
    with pytest.raises(NotFiveDigital):
        get_answer("2214")

def test_not_five_digits_long():
    """
    Checking exception for not five digits numbers
    """
    with pytest.raises(NotFiveDigital):
        get_answer("43534532214")
