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
    def __init__(self, inputed):
        self.inputed = inputed

    def __str__(self):
        return f"{self.inputed} greater than {MAX_VALUE}. Enter the value lesser or equal {MAX_VALUE}"

class Number:
    """
    Class for integer number
    """
    def __init__(self, number: int):
        if number < 0:
            raise NotNaturalNumber(number)
        elif number > MAX_VALUE:
            raise OutOfRange(number)
        self.number: int = number

    def get_dividers(self):
        "Getting dividers of the Number"
        dividers_list : list[int] = []
        for i in range(self.number):
            if self.number % (i+1) == 0:
                dividers_list.append(i+1)
        return dividers_list

user_value: int = int(input("Enter the integer value: \n"))
user_number = Number(user_value)
print(user_number.get_dividers())
