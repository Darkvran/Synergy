"""
Two numbers list, len of each <= 100000
How many numbers in both of this lists?
"""

class BadRange(Exception):
    """
    Exception for the case value is not in range
    """
    def __init__(self, value: int, range: str):
        self.value = value
        self.range = range
    def __str__(self):
        return f"{self.value} is not in range {self.range}"

first_list: list[int] = list(map(int, input("Enter the first list of numbers separated with whitespaces: ").split()))
second_list: list[int] = list(map(int, input("Enter the second list of numbers separated with whitespaces: ").split()))

if len(first_list) > 100000:
        raise BadRange(len(first_list), f"<= 100000")
if len(second_list) > 100000:
        raise BadRange(len(second_list), f"<= 100000")

print(len(set(first_list).intersection(set(second_list))))
