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

    def __init__(self, initial_colour="missing"):
        """Method to override"""
        self.my_colour = initial_colour


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
    """Check that Red knows it's name"""
    red = Red()
    assert red.my_colour == "Red"


def test11():
    """Check that Red can use inherited __str()__"""
    red = Red()
    assert str(red) == "This is the Red colour class."


class Blue(Colour):
    """Use the super method"""

    def __init__(self):
        super().__init__("Blue")


def test20():
    """Test Blue"""
    bule = Blue()
    assert bule.my_colour == "Blue"


if __name__ == "__main__":
    print("main")
else:
    print("NOT main")
