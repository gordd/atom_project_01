#!/usr/bin/python3

"""Demonstrate polymorphism for Jiachen"""


class Interface():
    """Generic interface, no data, only method names."""
    def method_A(self, arg):
        pass

    def method_B(self, arg):
        pass


class Type1(Interface):
    """The first type inherits, and implements the interface."""
    def method_A(self, arg):
        print(self.__my_name, "Method a arg", arg)

    def method_B(self, arg):
        print(self.__my_name, "Method b arg", arg)

    def __init__(self, myname="type 1"):
        self.__my_name = myname


class Type2(Interface):
    """The second type also inherits, and implements the interface."""
    def method_A(self, arg):
        print("Type 2 Method a arg", arg)

    def method_B(self, arg):
        print("Type 2 Method b arg", arg)


# First demo: create two different objects that implement the interface
one = Type1("blah")
two = Type2()


print("polymorphic method use")
for atype in (one, two):
    atype.method_A("foo")
    atype.method_B("bar")


# Second demo: create a method_A that will use whatever type is needed.
print("polymorphic function use")


def method_A(poly, morphic):
    poly.method_A(morphic)


def method_B(what_type_to_use, any_old_argument_for_the_method):
    what_type_to_use.method_B(any_old_argument_for_the_method)


method_A(one, "fizz")
method_A(two, "bang")

method_B(one, "here is a string to pass to the object to print")
method_B(two, 3.1414926535)
