from bank import Card


class CardReader:
    def get_card_number(self, card: Card) -> int:
        """Return the card number of the inserted card"""
        return card.get_number()

    def get_card_holder(self, card: Card) -> str:
        """Return the holder name of the inserted card"""
        return card.get_holder()
