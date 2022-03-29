from typing import Dict, Optional
from card import Card


class Bank:
    def __init__(self):
        self.data = {}

    def register_card(
        self, card_number: str, card_user: str, PIN: str, accounts: Dict[str, int]
    ) -> Optional[Card]:
        """Initialize a new card and register into data with the PIN and accounts with initial balance"""
        if self.check_card(card_number):
            return None
        else:
            card = Card(card_number, card_user)
            self.data[card_number] = {"PIN": PIN, "accounts": {}}
            for account in accounts:
                self.data[card_number]["accounts"][account] = accounts[account]
            return card

    def PIN_validation(self, card_number: str, PIN: str) -> bool:
        """Return the validation of user inputted PIN with the PIN in data"""
        if self.check_card(card_number):
            return self.data[card_number]["PIN"] == PIN
        else:
            return False

    def check_card(self, card_number: str) -> bool:
        """Return the exsistence of card in data"""
        return card_number in self.data

    def check_account(self, card_number: str, account: str) -> bool:
        """Return the exsistence of the account in card"""
        return account in self.data[card_number]["accounts"]

    def get_balance(self, card_number: str, account: int) -> bool:
        """Return the balance of account in data"""
        return self.data[card_number]["accounts"][account]

    def deposit(self, card_number: str, account: str, amount: int) -> None:
        """Deposit amount of cash into the account in data"""
        self.data[card_number]["accounts"][account] += amount

    def withdraw(self, card_number: str, account: str, amount: int) -> bool:
        """Withdraw amount of cash from the account in data"""
        if self.get_balance(card_number, account) >= amount:
            self.data[card_number]["accounts"][account] -= amount
            return True
        else:
            return False
