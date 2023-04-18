"""
Implement a class representing an account exception.

Implement a class representing a single bank account.

This class should control access to the account number and account balance
attributes by implementing the properties:
    - it should be possible to read the account number only, not change it.
      In case someone tries to change the account number, raise an alarm by
      raising an exception.
    - it should not be possible to set a negative balance. In case someone
      tries to set a negative balance, raise an alarm by raising an exception.
    - when the bank operation (deposit or withdrawal) is above 100.000, then
      additional message should be printed on the standard output (screen) for
      auditing purposes.
    - it should not be possible to delete an account as long as the balance is
      not zero.

Test your class behavior by:
    - setting the balance to 1000;
    - trying to set the balance to -200;
    - trying to set a new value for the account number;
    - trying to deposit 1.000.000;
    - trying to delete the account attribute containing a non-zero balance.
"""


class BankAccountException(Exception):
    pass


class BankAccount:
    def __init__(self, acc_number: str):
        self.__acc_number = acc_number
        self.__acc_balance = 0

    @property
    def acc_number(self):
        return self.__acc_number

    @acc_number.setter
    def acc_number(self, value):
        raise BankAccountException("Is not possible change the account number")

    @acc_number.deleter
    def acc_number(self):
        if self.__acc_balance:
            raise BankAccountException(
                f"Is not possible to delete the account with non-zero balance;"
                f"Current balance: {self.__acc_balance}"
            )
        self.__acc_number = None

    @property
    def acc_balance(self):
        return self.__acc_balance

    @acc_balance.setter
    def acc_balance(self, value):
        if value < 0:
            raise BankAccountException(
                "Is not possible set a negative balance"
            )
        self.__acc_balance = value
        if value > 100_000:
            print("Operation above $100.000")
