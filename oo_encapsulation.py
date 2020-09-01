#!/usr/bin/python3
"""Demonstrate object oriented encapsulation:
 - classes hide, or restrict some (or all) of their data
 - classes must provide "manipulator" or "accessor" methods
 - not fool-proof
"""

# test via pytest
import pytest


class Account():
    """
    Basic bank account, with added chat support for the cli user and units ($,Y,r$).
    Do calculations in cents for no accumulating round-off errors. No class should know.
    """

    def __init__(self, initial_balance=0, chat=False, initial_interest=False, initial_unit='cad'):
        self.__Interest = initial_interest
        self.__Unit = initial_unit
        self.__Balance = int( float(initial_balance) * 100.0 + 0.5)  # round up
        self.Conversion = {
            'cad': (1.00000, "$"),     # canadian dollars
            'usd': (0.75967, "$"),     # american dollars
            'rmb': (5.24866, "\245"),  # chinese renminbi (official currency vs. yuan )
            'brl': (4.25496, "R$"),    # brazillian reais (plural, real signular)
        }
        if chat:
            print("Created an account with a " + self.Conversion.get(self.__Unit)[1] + "%.2f "%initial_balance + "initial balance.")

    def __str__(self):
        return("Current account balance is " + self.Conversion.get(self.__Unit)[1] + "%.2f."%float(self.__Balance/100))

    def balance(self):
        return float(self.__Balance/100)

    def deposit(self, amount, chat=False, unit='cad'):
        if amount >= 0:  # jiachen: this is untested
            self.__Balance += int(float(amount) * 100.0 + 0.5)
            if chat:
                print("Deposited " + self.Conversion.get(self.__Unit)[1] + "%.2f "%amount + "to the account.")
            else:
                return float(self.__Balance/100)

    def withdraw(self, amount, chat=False, unit='cad'):
        if amount >= 0:  # jiachen: this is untested too
            self.__Balance -= int(float(amount) * 100.0 + 0.5)
            if chat:
                print("Withdrew " + self.Conversion.get(self.__Unit)[1] + "%.2f "%amount + "from the account.")
            else:
                return float(self.__Balance/100)

    def has_interest(self):
        return self.__Interest


# Test the Account creation, deposit and withdrawl methods.


@pytest.fixture
def empty_account():
    """The most basic, empty account"""
    return Account()


def test01(empty_account):
    """Can we create an account?"""
    assert empty_account is not None


def test02(empty_account):
    """Is the balance encapsulated, i.e. unaccessible?"""
    bal = 0.0
    # F841 local variable 'bal' is assigned to but never used
    with pytest.raises(AttributeError) as except_info:
        bal += empty_account.__Balance
    assert "has no attribute" in str(except_info)


def test03(empty_account):
    """Is the initial balance zero?"""
    assert empty_account.balance() == 0


def test04(empty_account):
    """Can we deposit $20?"""
    empty_account.deposit(20.003)
    assert empty_account.balance() == 20

def test05(empty_account):
    """Basic accounts don't pay interest"""
    assert empty_account.has_interest() == False

@pytest.fixture
def account_with_twenty():
    return Account(20.001)


def test05(account_with_twenty):
    """Can we withdraw $5?"""
    assert account_with_twenty.withdraw(5.002) == 15


def test10():
    """Jiachen create a test for deposit amounts less than 0 doesn't work"""
    pass


def test11():
    """Jiachen create a test for withdrawls less than 0 don't work either"""
    pass


if __name__ == "__main__":
    acct = Account(25, True, False, 'rmb')
    acct.deposit(10, True)
    print(acct)
    acct.withdraw(5, True)
    print(acct)
