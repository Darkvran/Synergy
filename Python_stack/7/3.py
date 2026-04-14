"""
Number sequence separated with whitespace. YES for each number if this number was later. NO if not
"""
numbers = set()
while True:
    number = int(input())
    if number in numbers:
        print("YES")
    else:
        print("NO")
        numbers.add(number)
