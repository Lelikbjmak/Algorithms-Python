import re


class AlphabetReplace:
    __ALPHABET_ORDINAL_POSITION = 96

    def __init__(self):
        pass

    def replace_string_with_alphabet_letter_numbers(self, text):
        text = re.sub(r"[^A-z]", '', text)
        text = text.lower()
        replaced_string = ""
        for char in text:
            replaced_string = replaced_string + str(self.__get_alphabet_position_for_letter(char)) + " "

        replaced_string = replaced_string.strip()
        return replaced_string

    def __get_alphabet_position_for_letter(self, letter):
        return ord(letter) - self.__ALPHABET_ORDINAL_POSITION
