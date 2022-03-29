class CashBin:
    def __init__(self, cash: int):
        self.cash = cash

    def check_cash(self) -> int:
        """Return the balance of cash bin"""
        return self.cash

    def deposit_cash(self, amount: int) -> None:
        """Deposit amount of cash into cash bin"""
        self.cash += amount

    def withdraw_cash(self, amount: int) -> None:
        """Withdraw amount of cash from cash bin"""
        self.cash -= amount
