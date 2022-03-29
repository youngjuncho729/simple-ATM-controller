# Simple-ATM-Controller

A simple ATM controller for coding assessment.

## Project Design

The ATM controller is implemented based on the assumption that the user follows the procedure of using the real ATM.

Insert card ⇒ Enter PIN ⇒ Select Account => Balance/Deposit/Withdraw ⇒ Remove card

Some exceptions that violate this order are not considered. These exceptions include but are not limited to checking balance before card insertion, or withdrawing before selecting the account.

This project consists of five major classes:

- Controller Class (controller.py)
  - Main class that controls the general functions of the ATM.
  - ATM controller is constructed with a bank, a card reader and a cash bin with initial balance.
  - Contains the card number, the account of the currently inserted card.
  - insert_card method reads the card_number using the card reader and accepts the card only if the PIN_validation from the bank is passed.
  - select_account sets up the account of the controller only if the account is valid.
  - check_balance method returns the balance of the selected account.
  - deposit method adds cash into the account and the cash bin.
  - withdraw method enables the user to withdraw cash from the account and the cash bin only if the balance of both are sufficient.
  - remove_card resets card and account property of the controller.
- Bank Class (bank.py)
  - Bank object for demo purpose.
  - register_card initializes a new card with a card number, a holder name, a PIN and accounts with initial balance, then stores card information into the bank data.
    ```python
    # Bank data examaple
    data = {
        "card_number_1": {"PIN": "1234", "accounts": {"saving": 0, "checking": 200}},
        "card_number_2": {"PIN": "4321", "accounts": {"saving": 150}},
    }
    ```
  - PIN_validation provides validation of user inputted PIN with the PIN in bank data.
  - check_card and check_account return the existence of the card or the account in data.
  - get_balance returns the balance of the account from the data.
  - deposit and withdraw methods update the balance of corresponding account in data.
- Card Class (card.py)
  - Card object for demo purpose.
  - Contains the card number and the card holder name.
- CardReader Class (card_reader.py)
  - Card reader object for demo purpose.
  - Returns the card number and the holder name of the card inserted to the controller.
- CashBin Class (cash_bin.py)
  - Cash bin object for demo purpose.
  - Contains the balance of cash in the cash bin.
  - check_cash method returns the balance of the cash bin.
  - deposit_cash and withdraw_cash method add or remove cash from the cash bin.

## How to run

### Installation

This project is coded and tested with `python 3.9`.

Clone the project by running the following command in your directory.

```bash
git clone https://github.com/youngjuncho729/simple-ATM-controller.git

cd simple-ATM-controller
```

### Testing

The controller part was tested with `unittest` framework.

Run the test by running the following command.

```bash
python test.py
# or
python -m unittest test.py
```

If you want to add more test cases for the controller, you can add them inside test.py file under the TestController Class.
