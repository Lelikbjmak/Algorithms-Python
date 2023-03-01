class Likes:
    def __init__(self):
        pass

    @staticmethod
    def likes(names):

        text = ""

        if len(names) == 0:
            text = "no one likes this"
        elif len(names) == 1:
            text = str(names[0]) + " likes this"
        elif 1 < len(names) < 4:
            for name in range(0, len(names) - 1):
                text = text + names[name] + ", "

            text = text[:-2]  # trim last ,
            text = text + " and " + str(names[len(names) - 1]) + " like this"
        else:
            for name in range(0, 2):
                text = text + names[name] + ", "
            text = text[:-2]
            text = text + " and " + str(len(names) - 2) + " others like this"

        return text
