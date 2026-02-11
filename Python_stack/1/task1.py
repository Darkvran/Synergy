"""
RU:
Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники.
Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца, 
его возраст и кличку, а потом выведет все эти данные в одно предложение. Например:
Это желторотый питон по кличке "Каа". Возраст: 34 года.

EN:
Imagine we are writing the backend for a veterinary clinic website.
We need to write a program that will ask the user for the type of pet,
its age, and its name, and then output all this information in a single sentence. For example:
This is a yellow-bellied python named "Kaa". Age: 34 years.
"""

#RU: Более простой, но неинтересный вариант решения. 
#EN: More simplier, but boring solution.
# petType = input("Введите вид питомца\n")
# petName = input("Введите имя питомца\n")
# petAge = input("Введите возраст питомца\n")
# print(f"Это {petType} по кличке \"{petName}\". Возраст: {petAge}.")

#EN:
# In future versions we can make more flex age attribution.
# (We can make it with user-input date of birth insead of age and using datetime module).
# Also we can make age filters. (Age is delta between cur. data and date of birth)

#RU:
#В будущих версиях мы можем сделать более гибкий атрибут возраста.
# (Это можно сделать с помощью ввода от пользователя даты рождения питомца заместо возраста
# и использования модуля datetime)
# Также можно будет добавить фильтры возраста.
# (Возраст - дельта между текущей датой и датой рождения.)

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
