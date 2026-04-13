"""
Input: Number N. Then N numbers not greater than 10e5.
Output: Reversed array of the numbers
"""

class OutOfRange(Exception):
    "Exception for the case out of value"
    def __init__(self, N: int):
        self.value: int = N

    def __str__(self):
        return f"Value {self.value} is out of range."

reversed_list = []
i_num = int(input("Enter the N: "))

if i_num > 10000 or i_num < 1:
    raise OutOfRange(i_num)

for _ in range(i_num):
    adding_value = int(input())

    if adding_value > 10e5:
        raise OutOfRange(adding_value)

    reversed_list.append(adding_value)

reversed_list = reversed_list[::-1]
print(reversed_list)
