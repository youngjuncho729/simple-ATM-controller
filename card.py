class Card:
    def __init__(self, card_number, card_holder) -> None:
        self.number = card_number
        self.holder = card_holder

    def get_number(self) -> None:
        """Getter method for card_number"""
        return self.number

    def get_holder(self) -> None:
        """Getter method for card_holder"""
        return self.holder
