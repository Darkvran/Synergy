"""
input: 1 <= N <= 100000. 1 <= N numbers <= 10e9
output: Changed array with all positions moved to right ([-1] to [0], [0] to [1] etc.)
"""

class OutOfRange(Exception):
    "Exception for the case value out of range"
    def __init__(self, value: int):
        self.value = value
    def __str__(self):
        return f"{self.value} is out of range."

class InvalidArrayLen(Exception):
    "Exception for the case user inputs array with wrong len"
    def __init__(self, value: int, correct_len: int):
        self.value: int = value
        self.correct_len: int = correct_len
    def __str__(self):
        return f"Your actual array size {self.value} is not equal to stated {self.correct_len}"

class CustomInt(int):
    "int class with range checking"
    def __init__(self, user_value: int):
        if int(user_value) < 1 or int(user_value) > 10e9:
            raise OutOfRange(user_value)
        self.user_value = user_value

class CustomList(list):
    "list class with size checking"
    def __init__(self, user_list_size: int, user_list: list):
        actual_user_list_size = len(user_list)
        if actual_user_list_size != user_list_size:
            raise InvalidArrayLen(actual_user_list_size, user_list_size)
        self.user_list = user_list

    def __str__(self):
        return str(self.user_list)

    def list_process(self):
        new_array = []
        for i in range(len(self.user_list)):
            new_array.append(self.user_list[i-1])
        return new_array

user_arr_len = int(input())
if user_arr_len < 1 or user_arr_len > 100000:
    raise OutOfRange(user_arr_len)

user_arr = CustomList(user_arr_len, list(map(CustomInt, input().split())))
print(user_arr.list_process())
