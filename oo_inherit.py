#!/usr/bin/python3
"""Demonstrate object oriented inheritance:
 - classes inherit their parents methods and data
 - inherited methods can be overwritten
 - can use a parent's method with a super reference
"""

# test via pytest


class Colour():
    """Parent, or "base" class, to be inherited"""

    def __str__(self):
        """Method to inherit"""
        return "This is the " + str(self.my_colour) + " colour class."

    def __init__(self):
        """Method to override"""
        self.my_colour = "missing"


def test01():
    """Can we make a colour?"""
    colour = Colour()
    assert colour is not None


def test02():
    """Is the base class colour 'missing'?"""
    colour = Colour()
    assert colour.my_colour == "missing"


def test03():
    """Will the base colour say it is 'the missing colour'?"""
    colour = Colour()
    assert str(colour) == "This is the missing colour class."


# Example to get Jiachen started
class Red(Colour):
    """The Red colour inherits Colour class and extends it."""
    def __init__(self):
        """Override the missing colour"""
        self.my_colour = "Red"


def test10():
    """(Jiachen: Delete the 'pass' first) Check that Red knows it's name"""
    red = Red()
    assert red.my_colour == "Red"


def test11():
    """Jiachen: 'pass' deleted here too)Check that Red can use inherited __str()__"""
    red = Red()
    assert str(red) == "This is the Red colour class."


class Blue(Colour):
    """Jiachen: this is where you show how to inherit a class and extend it."""

    def mood(self):
        return


def test20():
    """Test Blue"""
    pass


def test21():
    """Test Blue's use of super"""
    pass


def test22():
    """Test the blue new mathod, mood"""
    # assert blue.mood() == "blue"


if __name__ == "__main__":
    print("main")
else:
    print("NOT main")
