"""
Input: String with len =< 1000
Output: Convert all consecutive whitespaces in one whitespace
"""

class UserString(str):
    "User class of string with new function"
    def __init__(self, string: str):
        self.string: str = string

    def remove_extra_whitespaces(self):
        "Remove extra whitespaces from the string"
        return " ".join([word for word in self.string.split() if word != " "])

print(UserString("У  меня     есть        нож, есть арбалет,      они    служат    мне          уже           тысячу     лет").remove_extra_whitespaces())
