### Description

[Kata](https://www.codewars.com/kata/546f922b54af40e1e90001da/python)

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

#### Example
```python
alphabet_position("The sunset sets at twelve o' clock.")
```
Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` ( as a string )


### Solutions

```python
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
```
