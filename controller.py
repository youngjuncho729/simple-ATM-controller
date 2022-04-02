from card import Card
from bank import Bank
from card_reader import CardReader
from cash_bin import CashBin


class Controller:
    def __init__(self, bank: Bank, cash: int) -> None:
        self.card_number = None
        self.account = None
        self.bank = bank
        self.cash_bin = CashBin(cash)
        self.card_reader = CardReader()

    def insert_card(self, card: Card, PIN: str) -> bool:
        """
        Insert the card if PIN_validation is passed, else card is not inserted and return False
        """
        card_number = self.card_reader.get_card_number(card)
        if self.bank.PIN_validation(card_number, PIN):
            self.card_number = card_number
            return True
        else:
            return False

    def remove_card(self) -> bool:
        """
        Remove card if a card is inserted in ATM then reset card_number and account to None
        """
        if self.card_number != None:
            self.card_number, self.account = None, None
            return True
        else:
            return False

    def select_account(self, account: str) -> bool:
        """Select the account if the account is valid in this card"""
        if self.card_number is None:
            return False

        if self.bank.check_account(self.card_number, account):
            self.account = account
            return True
        else:
            return False

    def check_balance(self) -> int:
        """Return the balance of the account of this card"""
        return self.bank.get_balance(self.card_number, self.account)

    def deposit(self, amount: int) -> int:
        """Deposit amount of mooney into account and cash bin then return the updated balance of the account"""
        self.bank.deposit(self.card_number, self.account, amount)
        self.cash_bin.deposit_cash(amount)
        return self.check_balance()

    def withdraw(self, amount: int) -> bool:
        """Withdraw amount of money from the account if account and ATM both have sufficient balance"""
        if self.cash_bin.check_cash() < amount:
            return False
        if self.bank.withdraw(self.card_number, self.account, amount):
            self.cash_bin.withdraw_cash(amount)
            return True
        else:
            return False
