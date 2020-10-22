#!/usr/bin/python3
"""Create a savings (with interest) account"""

# test via pytest
import pytest
from oo_encapsulation import Account


class Savings(Account):
    """Basic account with interest"""

    def __init__(self, initial_balance=0, chat=False, initial_interest_rate=0, initial_units='cad'):
        """A Savings account is a basic account with interest in percent"""
        super().__init__(initial_balance, chat, True, initial_units)
        self.__rate = initial_interest_rate

    # accessors for the interest rate

    def set_interest_rate(self, new_rate, chat=False):
        """Rates fluctuate, so we need a way to set rates in percent"""
        old_rate = self.__rate
        self.__rate = new_rate
        if chat:
            print("The new interest rate is", str(self.__rate) + "%, changed from", str(old_rate) + "%.")
        else:
            return self.__rate

    def get_interest_rate(self, chat=False):
        """Today's Rate in percent"""
        if chat:
            print("Today's interest rate is", str(self.__rate) + "%")
        else:
            return self.__rate

    def pay_interest(self, chat=False):
        """Calculate the amount based upon today's Rate """
        interest = super().balance() * float(self.__rate / 100.0)
        if chat:
            # print("Your balance pays", "$" + str(interest), "of interest.")
            print("Your balance pays $%.2f" % interest, "of interest.")
        else:
            return interest


@pytest.fixture
def empty_account():
    """The empty account"""
    return Savings()


def test01(empty_account):
    """Can we create a savings account?"""
    assert empty_account is not None


def test02(empty_account):
    """Is the initial balance zero?"""
    assert empty_account.balance() == 0


def test03(empty_account):
    """Basic account methods: Can we deposit $20?"""
    empty_account.deposit(20)
    assert empty_account.balance() == 20
    """And can we withdraw too? """
    empty_account.withdraw(2)
    assert empty_account.balance() == 18

# test the interest rate feature


def test10(empty_account):
    """Savings accounts pay interest."""
    assert empty_account.has_interest()


def test11(empty_account):
    """initial interest rate should be 0"""
    assert empty_account.get_interest_rate() == 0


def test12(empty_account):
    """can we set the rate to 10%?"""
    empty_account.set_interest_rate(10)
    assert empty_account.get_interest_rate() == 10


@pytest.fixture
def account_with_twenty():
    """We are satisfied that deposit works, start with $20 and 10%"""
    return Savings(20, False, 10)


def test13(account_with_twenty):
    assert account_with_twenty.pay_interest() == 2.0


class Chequing(Savings):
    """If the account balance is over 1,000, it pays interest. If less, not."""

    def pay_interest(self, chat=False):
        if self.balance() >= 1000:
            return super().pay_interest(chat)
        else:
            if chat:
                print("Sorry, account balance is below $1,000. No interest eligible.")
            return 0.0


@pytest.fixture
def chequing_account_999():
    """Create a chequing account that could pay 10% interest"""
    return Chequing(999, False, 10)


def test20(chequing_account_999):
    """Can we create a chequing account? """
    assert chequing_account_999 is not None


def test21(chequing_account_999):
    """Accounts with less than 1,000 don't pay interest"""
    assert chequing_account_999.pay_interest() == 0.0


def test22(chequing_account_999):
    """see if depositing just one will cause interest to be paid"""
    chequing_account_999.deposit(1)  # should tip the balance to 1,000
    assert chequing_account_999.pay_interest() == 100.0


if __name__ == "__main__":
    print("Test savings account")
    save = Savings(0, True, 4.5, 'brl')
    save.set_interest_rate(10, True)
    save.get_interest_rate(True)
    save.deposit(12.34, True)
    print(save)
    save.pay_interest(True)
    save.deposit(save.pay_interest(), True)
    print(save)
    save.withdraw(5.55, True)
    print(save)
    print("Test chequing account")
    chkg = Chequing(999, True, 10, 'cad')
    chkg.pay_interest(True)
    print(chkg)
    chkg.deposit(1.00, True)
    chkg.pay_interest(True)
    chkg.deposit(chkg.pay_interest(), True)
    print(chkg)

    print("Test polymorphic method")
    for account in (save, chkg):
        account.pay_interest(False)
        account.deposit(account.pay_interest(), True)
        print(account)
