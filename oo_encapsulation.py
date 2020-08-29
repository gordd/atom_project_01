#!/usr/bin/python3
"""Demonstrate object oriented encapsulation:
 - classes hide, or restrict some (or all) of their data
 - classes must provide "manipulator" or "accessor" methods
 - not fool-proof
"""

# test via pytest
import pytest


class Account():
    """Basic bank account, with added chat support for the cli user."""

    def __init__(self, initial_balance = 0, chat = False ):
        self.__Interest = False
        self.__Unit = 'dollars'
        self.__Balance = float(initial_balance)
        self.Conversion = {
            'dollars':(1.0, "$"), 
            'rmb':(5.0, "Y"), 
            'reais':(3.3, "r$"),
        }
        if chat:
            print("Created account with a $" + str(initial_balance), "initial balance.")

    def __str__(self):
        return "Current balance is " + str(self.__Balance) + str(self._Unit)


    def balance(self):
        return self.__Balance
        
    def deposit(self, amount, chat=False, unit='dollars'):
        if amount >=0:
            self.__Balance += float(amount)
            if chat:
                print("Deposited $" + str(amount), "to account. New balance is $" + str(self.__Balance))
            else:
                return self.__Balance

    def withdraw(self, amount, chat=False, unit='dollars'):
        if amount >=0:
            self.__Balance -= float(amount)
            if chat:
                print("Withdrew $" + str(amount), "from account. New balance is $" + str(self.__Balance))
            else:
                return self.__Balance


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
    with pytest.raises(AttributeError) as except_info:
        bal = empty_account.__Balance
    assert "has no attribute" in str(except_info)


def test03(empty_account):
    """Is the initial balance zero?"""
    assert empty_account.balance() == 0


def test04(empty_account):
    """Can we deposit $20?"""
    empty_account.deposit(20)
    assert empty_account.balance() == 20


@pytest.fixture
def account_with_twenty():
    return Account(20)


def test05(account_with_twenty):
    """Can we withdraw $5?"""
    assert account_with_twenty.withdraw(5) == 15


if __name__ == "__main__":
    acct = Account(0, True)
    acct.deposit(10, True)
    acct.withdraw(5, True)
