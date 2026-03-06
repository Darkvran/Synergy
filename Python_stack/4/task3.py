"""
Input: Integers  A, B, A <= B
Output: Even numbers at range [a,b] with whitespace separator
"""

class  WrongRange(Exception):
    """
    Exception for the  case first border greater than second_border
    """
    def __str__(self):
        return "first_border must be lesser or equal than second_border"

class NumberRange:
    """
    Class for number range like [a, b]
    """
    def __init__(self, first_border: int, second_border: int):
        if first_border > second_border:
            raise WrongRange()

        self.first_border = first_border
        self.second_border = second_border

    def get_even_numbers(self):
        "Get even numbers on the range [a, b]"
        even_numbers_list: list[int] = []
        for i in range(self.first_border, self.second_border + 1):
            if i % 2 == 0 and i != 0:
                even_numbers_list.append(i)
        return even_numbers_list

user_range = input("Enter the range borders separated with whitespace: ")

user_range = NumberRange(*list(map(int, user_range.split())))
print(*user_range.get_even_numbers())
