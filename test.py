import unittest
from unittest.mock import patch
from controller import Controller
from bank import Bank


class TestController(unittest.TestCase):
    """Tester for Controller class."""

    def setUp(self):
        """Initalize instance of Bank, Controller, and card for the test use"""
        self.bank = Bank()
        self.ATM = Controller(self.bank, 100)
        self.card = self.bank.register_card(
            "12345", "user_1", "1111", {"checking": 50, "saving": 100}
        )

    @patch("bank.Bank.PIN_validation", return_value=True)
    def test_insert_card_valid_card_correct_PIN(self, mock_pin):
        """Insert card with valid card and PIN"""
        result = self.ATM.insert_card(self.card, "1111")
        self.assertTrue(result)
        self.assertEqual(self.ATM.card_number, "12345")

    @patch("bank.Bank.PIN_validation", return_value=False)
    def test_insert_card_valid_card_wrong_PIN(self, mock_pin):
        """Insert card with valid card but wrong PIN"""
        result = self.ATM.insert_card(self.card, "2222")
        self.assertFalse(result)
        self.assertEqual(self.ATM.card_number, None)

    @patch("card_reader.CardReader.get_card_number", return_value="00000")
    def test_insert_card_wrong_card_number(self, mock_num):
        """Insert card when card reader returns wrong card number"""
        result = self.ATM.insert_card(self.card, "1111")
        self.assertFalse(result)
        self.assertEqual(self.ATM.card_number, None)

    def test_remove_card_ATM_with_card(self):
        """remove card from ATM with a card"""
        self.ATM.insert_card(self.card, "1111")
        result = self.ATM.remove_card()
        self.assertTrue(result)
        self.assertEqual(self.ATM.card_number, None)

    def test_remove_card_ATM_without_card(self):
        """remove card from ATM without card"""
        result = self.ATM.remove_card()
        self.assertFalse(result)

    @patch("bank.Bank.check_account", return_value=True)
    def test_select_account_valid(self, mock_account):
        """Select an valid account"""
        self.ATM.insert_card(self.card, "1111")
        self.ATM.select_account("saving")
        self.assertEqual(self.ATM.account, "saving")
        self.ATM.select_account("checking")
        self.assertEqual(self.ATM.account, "checking")

    @patch("bank.Bank.check_account", return_value=False)
    def test_select_account_invalid(self, mock_account):
        """Select an invalid account"""
        self.ATM.insert_card(self.card, "1111")
        self.ATM.select_account("invalid_account")
        self.assertEqual(self.ATM.account, None)

    def test_check_balance(self):
        """Check the balance of account"""
        self.ATM.insert_card(self.card, "1111")
        self.ATM.select_account("saving")
        result = self.ATM.check_balance()
        self.assertEqual(result, 100)

    def test_deposit(self):
        """Check the updated balance after deposit"""
        self.ATM.insert_card(self.card, "1111")
        self.ATM.select_account("checking")
        result = self.ATM.deposit(100)
        self.assertEqual(result, 150)
        result = self.ATM.deposit(200)
        self.assertEqual(result, 350)

    @patch("cash_bin.CashBin.check_cash", return_value=10000)
    def test_withdraw_sufficient_balance(self, mock_cash):
        """Withdraw from account with sufficient balance in both cash bin and account"""
        self.ATM.insert_card(self.card, "1111")
        self.ATM.select_account("checking")
        result = self.ATM.withdraw(30)
        self.assertTrue(result)
        self.assertEqual(self.ATM.check_balance(), 20)

    @patch("cash_bin.CashBin.check_cash", return_value=-1)
    def test_withdraw_insufficient_balance_cashbin(self, mock_cash):
        """Withdraw from account with insufficient balance in cash bin"""
        self.ATM.insert_card(self.card, "1111")
        self.ATM.select_account("checking")
        result = self.ATM.withdraw(10)
        self.assertFalse(result)
        self.assertEqual(self.ATM.check_balance(), 50)

    @patch("cash_bin.CashBin.check_cash", return_value=10000)
    def test_withdraw_insufficient_balance_account(self, mock_cash):
        """Withdraw from account with insufficient balance in account"""
        self.ATM.insert_card(self.card, "1111")
        self.ATM.select_account("checking")
        result = self.ATM.withdraw(100)
        self.assertFalse(result)
        self.assertEqual(self.ATM.check_balance(), 50)


if __name__ == "__main__":
    unittest.main()
