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
        self.__Balance = int(float(initial_balance) * 100.0 + 0.5)  # round up
        self.Conversion = {
            'cad': (1.00000, "$"),     # canadian dollars
            'usd': (0.75967, "$"),     # american dollars
            'rmb': (5.24866, "\245"),  # chinese renminbi (official currency vs. yuan )
            'brl': (4.25496, "R$"),    # brazillian reais (plural, real signular)
        }
        if chat:
            long_msg = "Created an account with a " + self.Conversion.get(self.__Unit)[1]
            long_msg += "%.2f " % initial_balance + "initial balance."
            print(long_msg)

    def __str__(self):
        return("Current account balance is " + self.Conversion.get(self.__Unit)[1] + "%.2f." % float(self.__Balance / 100))

    def balance(self):
        return float(self.__Balance / 100)

    def deposit(self, amount, chat=False, unit='cad'):
        str_amount = self.Conversion.get(self.__Unit)[1] + "%.2f " % amount
        cents = int(float(amount) * 100.0 + 0.5)  # round up
        if cents > 0:  # don't allow users to suck money out of the account!
            self.__Balance += cents
            if chat:
                print("Deposited " + str_amount + "to the account.")
        if cents < 0:
            if chat:
                print("Sorry, you can't deposit", str_amount)
        return float(self.__Balance / 100)

    def withdraw(self, amount, chat=False, unit='cad'):
        str_amount = self.Conversion.get(self.__Unit)[1] + "%.2f " % amount
        cents = int(float(amount) * 100.0 + 0.5)  # round up
        if (cents > 0) & (cents <= self.__Balance):
            self.__Balance -= cents
            if chat:
                print("Withdrew " + str_amount + "from the account.")
        if (cents > self.__Balance) & chat:
            print("Not Sufficient Funds to withdraw", str_amount + "from your account.")
        if cents < 0 & chat:
                print("Sorry, you can't withdraw ", str_amount)
        return float(self.__Balance / 100)

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
    assert not empty_account.has_interest()


@pytest.fixture
def account_with_twenty():
    return Account(20.001)


def test06(account_with_twenty):
    """Can we withdraw $5?"""
    assert account_with_twenty.withdraw(5.002) == 15


def test10(account_with_twenty):
    """Create a test for deposit amounts less than 0 doesn't work"""
    starting_balance = account_with_twenty.balance()
    so_called_deposit = -5
    final_balance = account_with_twenty.deposit(so_called_deposit)
    assert final_balance == starting_balance  # money not sucked out


def test11(account_with_twenty):
    """Create a test for withdrawl amounts less than 0 don't work."""
    starting_balance = account_with_twenty.balance()
    so_called_withdrawl = -5
    final_balance = account_with_twenty.withdraw(so_called_withdrawl)
    assert final_balance == starting_balance


def test12(account_with_twenty):
    """Test for withdrawl amounts more than balance (NSF) don't work."""
    starting_balance = account_with_twenty.balance()
    so_called_withdrawl = 23.45
    final_balance = account_with_twenty.withdraw(so_called_withdrawl)
    assert final_balance == starting_balance


if __name__ == "__main__":
    acct = Account(25, True, False, 'rmb')
    acct.deposit(10, True)
    acct.deposit(-11, True)
    print(acct)
    acct.withdraw(5, True)
    print(acct)
    acct.withdraw(-6, True)
    print(acct)
    acct.withdraw(31, True)
    print(acct)
