"""
Input: english word in lowercase. 
Output: Number of vowels and consonants. Number of each vowel.
"""
import json

CONFIG_LANGUAGE = "RU" #EN or RU available

language_letters = json.load(open("task2_symb.json", "r", encoding="utf-8"))[CONFIG_LANGUAGE]

class UndefinedCharacter(Exception):
    """
    Exception for the caste user enters 
    """
    def __init__(self, character: str):
        self.character = character

    def __str__(self): 
        return f"'{self.character}' is not in current language dictionary."

class Word:
    """
    Class for word processing
    """
    def __init__(self, word: str):
        for character in word.lower():
            if character not in language_letters['alphabet']:
                raise UndefinedCharacter(character)
        self.word = word.lower()

    def phonetic_analysis(self):
        """
        Returns the dict with word analysis
        
        :param self: Description
        """
        vowels_sum = 0
        vowels_num_dict = {}
        for vowel in language_letters['vowels']:
            vowels_num_dict[vowel] = self.word.count(vowel)
            vowels_sum += self.word.count(vowel)

        return {"vowels": 
                    {"sum": vowels_sum,
                     "letters":vowels_num_dict},
                "consonants": len(self.word) - vowels_sum}
