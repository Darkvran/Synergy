"""
Input: Integer X (X <= 2e9)
Output: Dividers of X including 1 and X itself 
"""

MAX_VALUE = 2e9

class NotNaturalNumber(Exception):
    "Exception for the case number is not natural"
    def __init__(self, inputed):
        self.inputed: int = inputed

    def __str__(self):
        return  f"{self.inputed} is not natural value"

class OutOfRange(Exception):
    "Exception for the case number is greater then MAX_VALUE"
    def __init__(self, inputed, max_value):
        self.inputed = inputed
        self.max_value = max_value

    def __str__(self):
        return f"{self.inputed} greater then {self.max_value}. Enter the value lesser or equal {self.max_value}"

class Number:
    """
    Class for integer number
    """
    def __init__(self, number: int):
        self.number: int = number

    def get_dividers(self):
        "Getting dividers of the Number"
        dividers_list : list[int] = []
        for i in range(self.number):
            if self.number % (i+1) == 0:
                dividers_list.append(i+1)
        return dividers_list

try:
    user_value: int = int(input("Enter the integer value: \n"))
    if user_value < 0: 
        raise NotNaturalNumber(user_value)
    elif user_value > MAX_VALUE:
        raise OutOfRange(user_value, MAX_VALUE)
    else:
        user_number = Number(user_value)
        print(user_number.get_dividers())

except ValueError as e:
    print(e)
except NotNaturalNumber as e:
    print(e)
except OutOfRange as  e:
    print(e)
