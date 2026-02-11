"""
Imagine we are writing the backend for a veterinary clinic website.
We need to write a program that will ask the user for the type of pet,
its age, and its name, and then output all this information in a single sentence. For example:
This is a yellow-bellied python named "Kaa". Age: 34 years.
"""

# petType = input("Введите вид питомца\n")
# petName = input("Введите имя питомца\n")
# petAge = input("Введите возраст питомца\n")
# print(f"Это {petType} по кличке \"{petName}\". Возраст: {petAge}.")

# In future versions we can make more flex age attribution.
# (We can make it with user-input date of birth insead and data).
# Also we can make age filters.

class Pet:
    """
    Doctring of Pet class
    """
    def __init__(self, pet_specie=None, pet_name=None, pet_age=None):
        self.specie: str = pet_specie
        self.name: str = pet_name
        self.age: str = pet_age

    def __str__(self):
        return f'This is {self.specie} with name "{self.name}". Age: {self.age}.'


print(Pet(input("Enter the pet specie\n")\
        , input("Enter the pet name\n")\
        , input("Enter the pet age\n")))
