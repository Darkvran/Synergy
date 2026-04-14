"""
Input: Number N, then list with N integer values
Output: Number of zeros
"""

class WrongListLen(Exception):
    """
    Exception for the case user enter list with len not equal N
    """
    def __init__(self, actual: int, expected: int):
        self.actual: int = actual
        self.expected: int = expected

    def __str__(self):
        return f"Expected {self.expected} elements, but got {self.actual}."

class  NumberList:
    """
    Class for number list with defined len
    """
    def __init__(self, numbers, expected_len, finding_symbol=0):
        """
        When user enters string or list len is not equal N, then raising exceptions
        """
        if len(numbers) != expected_len:
            raise WrongListLen(len(numbers), expected_len)
        self.number_list: list[int] = numbers
        self.finding_symbol: str = finding_symbol
    def get_symb_num(self):
        "Returns the self.finding_symbol num in the self.number_list"
        return self.number_list.count(self.finding_symbol)


expected_len: int = int(input("Enter the len of number list:\n"))
raw_numbers: list[int] = list(map(int, input("Enter the numbers separated  with whitespace:\n").split()))
my_numbers: NumberList =  NumberList(raw_numbers, expected_len)
print(f"Result: {my_numbers.get_symb_num()}")
