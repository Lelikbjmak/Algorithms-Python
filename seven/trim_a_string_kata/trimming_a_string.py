class TrimmingString:
    def __init__(self, text, trim_number):
        self.__trim_number = trim_number
        self.__text = text

    @staticmethod
    def trim(text, number):
        if len(text) <= number:
            return text

        if len(text) > 3 and number > 3:
            number -= 3  # 3 dots at the end

        result = text[:number]
        result += "..."

        return result
