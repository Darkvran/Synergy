"""
User enters the int number.
Outputs the description like "negative even number", "null number", "positive odd number".
If number is odd, outputs "Number is not even". 
"""
import pytest


class Number:
    """
    Provides decription of the number in string format
    """
    def __init__(self, number:int):
        self.number:int = number

    def __str__(self):
        if self.number == 0:
            return "Null number"
        elif self.number % 2 == 0 and self.number > 0:
            return "Positive even number"
        elif self.number % 2 == 0 and self.number < 0:
            return "Negative even number"
        elif self.number % 2 == 1 and self.number > 0:
            return "Positive odd number\nNumber is not even"
        elif self.number % 2 == 1 and self.number < 0:
            return "Negative odd  number\nNumber is not even"

def test_positive_even():
    """
    Test positive even value
    """
    assert str(Number(10)) == "Positive even number"
    assert str(Number(20)) == "Positive even number"
    assert str(Number(30)) == "Positive even number"
    assert str(Number(58)) == "Positive even number"
    assert str(Number(10336436342)) == "Positive even number"
    assert str(Number(654969232)) == "Positive even number"
    assert str(Number(2)) == "Positive even number"
    assert str(Number(100500)) == "Positive even number"
    assert str(Number(46)) == "Positive even number"
    assert str(Number(12343256)) == "Positive even number"

def test_positive_odd():
    """
    Test positive odd value
    """
    assert str(Number(11)) == "Positive odd number\nNumber is not even"
    assert str(Number(21)) == "Positive odd number\nNumber is not even"
    assert str(Number(31)) == "Positive odd number\nNumber is not even"
    assert str(Number(59)) == "Positive odd number\nNumber is not even"
    assert str(Number(10336436343)) == "Positive odd number\nNumber is not even"
    assert str(Number(654969233)) == "Positive odd number\nNumber is not even"
    assert str(Number(1)) == "Positive odd number\nNumber is not even"
    assert str(Number(100501)) == "Positive odd number\nNumber is not even"
    assert str(Number(47)) == "Positive odd number\nNumber is not even"
    assert str(Number(12343257)) == "Positive odd number\nNumber is not even"

def test_negative_even():
    """
    Test negative even value
    """
    assert str(Number(-110)) == "Negative even number"
    assert str(Number(-210)) == "Negative even number"
    assert str(Number(-310)) == "Negative even number"
    assert str(Number(-590)) == "Negative even number"
    assert str(Number(-103364363432)) == "Negative even number"
    assert str(Number(-6549692336)) == "Negative even number"
    assert str(Number(-1020)) == "Negative even number"
    assert str(Number(-1005014)) == "Negative even number"
    assert str(Number(-478)) == "Negative even number"
    assert str(Number(-123432576)) == "Negative even number"

def test_negative_odd():
    """
    Test negative odd value
    """
    assert str(Number(-1101)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-2103)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-3105)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-5907)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-1033643634329)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-65496923361)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-10203)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-10050145)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-4787)) == "Negative odd  number\nNumber is not even"
    assert str(Number(-1234325769)) == "Negative odd  number\nNumber is not even"

def test_null():
    """
    Test null value 
    """
    assert str(Number(0)) == "Null number"


def user_test():
    """User test"""
    user_number = int(input("Enter the int value\n"))
    print(Number(user_number))

user_test()
