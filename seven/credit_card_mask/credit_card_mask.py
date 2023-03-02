class CreditCardMask:

    def __init__(self):
        pass

    @staticmethod
    def mask(card):
        size = len(card) - 4
        masked_card = '#' * size + card[-4:]
        return masked_card
