"""
First string is N - count of integers (1 <= N <= 100000).
Second string is N integers separated with whitespace. Every integer is lesser than 2*10e9 by module. 
How many different integers in data?
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

integers_num: int = int(input("Enter the integers num: "))

if integers_num > 1 and integers_num < 100000:   
    number_list: list[int] = list(map(int, input().split()))
    if len(number_list) != integers_num:
        raise BadRange(len(number_list), f"equal to {integers_num}")

    for number in number_list:
        if abs(number) > 2*10e9:
            raise BadRange(number, "lesser than 2*10e9 by module")
    print (f"{len(set(number_list))} different integers.")
else:
    raise BadRange(integers_num, "from 1 to 100000")
