"""
Input: String with no whitespaces
Output: "Yes" if string is palindrome, else "No"
"""

class WhitespaceException(Exception):
    "Exception for the case whitespaces in string"
    def __str__(self):
        return "There are whitespaces in the string"

class UserString(str):
    "User class of string with new function"
    def __init__(self, string: str):
        if " " in string:
            raise WhitespaceException
        self.string: str = string.lower()

    def is_palindrome(self):
        "Check if the string is palindrome"
        if self.string ==  self.string[::-1]:
            return "Yes"
        else: return "No"

print(UserString("Шалаш").is_palindrome())
