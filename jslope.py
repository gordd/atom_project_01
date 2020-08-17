# jaichen (chauhui) li, [09.07.20 22:06]
# accomodations for python2: math needs float(), class needs str()
# echo look for syntax errors or undefined names
# flake8 --count --select=E9,F63,F7,F82 --show-source --statistics gslope.py
# echo look for all errors as warnings
# flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics gslope.py
# echo run pytest
# python3 -m pytest gslope.py

import math


class Point:
    def __init__(self, init_x=0, init_y=0):
        self.x = float(init_x)
        self.y = float(init_y)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def __str__(self):
        say = "(" + str(self.x) + ", " + str(self.y) + ")"
        return say


def slope(p1, p2):
    """Calculate the slope (m) between point 1 and point 2"""
    run = p2.x - p1.x
    if run == 0:
        return
    rise = p2.y - p1.y
    slope = rise / run
    return slope


def test00():
    """Is a default point properly constructed?"""
    p = Point()
    if p.x == 0:
        if p.y == 0:
            print("Test_00: PASS")
        else:
            print("Test_00: FAIL y")
    else:
        print("Test_00: FAIL x")


def test01():
    """Is a specific (5,20) point properly constructed?"""
    p = Point(5, 20)
    if p.x == 5:
        if p.y == 20:
            print("Test_01: PASS")
        else:
            print("Test_01: FAIL y")
    else:
        print("Test_01: FAIL x")


def test02():
    """ does slope return anything at all ? """
    p1 = Point(0, 1)
    p2 = Point(2, 3)
    anything = slope(p1, p2)
    if anything is None:
        print("Test_02: FAIL")
    else:
        print("Test_02: PASS")


def test03():
    """ does slope cope with a slope of 0? """
    p1 = Point(1, 1)
    p2 = Point(2, 1)
    anything = slope(p1, p2)
    if anything is None:
        print("Test_03: FAIL")
    else:
        if anything == 0:
            print("Test_03: PASS")
        else:
            print("Test_03: FAIL, anything=", anything)


def test04():
    """ does slope cope with an infinite slope? """
    p1 = Point(1, 1)
    p2 = Point(1, 2)
    anything = slope(p1, p2)
    if anything is None:
        print("Test_04: PASS")
    else:
        if anything == 0:
            print("Test_04: FAIL")
        else:
            print("Test_04: FAIL, anything=", anything)


def test05():
    """Test the slope function"""
    p1 = Point(5, 6)
    p2 = Point(10, 12)
    m = slope(p1, p2)
    if m == 1.2:
        print("Test_05: PASS")
    else:
        print("Test_05: FAILED m", m)


def y_intercept(p1, p2):
    """Calculate the y intercept of 2 points"""
    if (p1 == p2) | (p1.x == p2.x):
        return
    if p1.y == p2.y:
        return p1.y
    return p1.y - p1.x * slope(p1, p2)


def test06():
    """ does the Y-intercept return anything at all?
     - If the two points are the same, then it shouldn't
     - If the two points make a vertical line, then it shouldn't"""
    p1 = Point(5, 6)
    same_point = y_intercept(p1, p1)
    if same_point is None:
        p2 = Point(5, 9)
        vertical = y_intercept(p1, p2)
        if vertical is None:
            print("Test_06: PASS")
        else:
            print("Test_06: FAIL, vertical")
    else:
        print("Test_06: FAIL, same point")


def test07():
    """does the y-intercept handle the case of a horizontal?"""
    p1 = Point(5, 6)
    p3 = Point(9, 6)
    horizonal = y_intercept(p1, p3)
    if horizonal is not None:
        if horizonal == 6:
            print("Test_07: PASS")
        else:
            print("Test_07: FAIL, horizontal =", horizonal)
    else:
        print("Test_07: FAIL, horizontal")


def test08():
    """Can we actually calculate the b intercept?
       Assume y = 4x+3. let x=1 then y=7."""
    m = 4
    b = 3
    x = 1
    y = m * x + b
    p1 = Point(x, y)
    x = 10
    y = m * x + b
    """Alternatively, let x=10 then y=43"""
    p2 = Point(x, y)
    intercept = y_intercept(p1, p2)
    if intercept == b:
        print("Test_08: PASS")
    else:
        print("Test_08: FAIL intercept =", intercept)


def distance(p1, p2):
    """Calculate the distance between two points.
       distance**2 = rise * rise + run * run """
    run = p2.x - p1.x
    rise = p2.y - p1.y
    return math.sqrt(run * run + rise * rise)


def test09():
    """ Jiachen will write this.  """
    p1 = Point(4, 0)
    p2 = Point(6, 6)
    d = distance(p1, p2)
    if d == math.sqrt(40):
        print("Test_09: PASS")
    else:
        print("Test_09: FAIL ", d)


def midpoint(p1, p2):
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)


def test10():
    p1 = Point(4, 4)
    p2 = Point(5, 5)
    p3 = Point(6, 6)
    mid = midpoint(p1, p3)
    assert mid is not None
    assert mid == p2
    if mid is not None:
        if mid == p2:
            print("Test_10: PASS " + str(mid))
        else:
            print("Test_10: FAIL mid")
    else:
        print("Test_10: FAIL mid is None")


class Line:
    def __init__(self, p2=Point(0, 0), p1=Point(0, 0)):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        say = "Line(" + str(self.p1) + " to " + str(self.p2) + ")"
        return say

    def slope(self):
        """Calculate the slope (m) between 2 points"""
        run = self.p2.x - self.p1.x
        if run == 0:
            return
        rise = self.p2.y - self.p1.y
        slope = rise / run
        self.slope = slope
        return self.slope

    def intercept(self):
        """Calculate the y intercept of 2 points"""
        if (self.p1 == self.p2) | (self.p1.x == self.p2.x):
            return
        if self.p1.y == self.p2.y:
            return self.p1.y
        return self.p1.y - self.p1.x * slope(self.p1, self.p2)

    def distance(self):
        """Calculate the distance between 2 points.
           distance**2 = rise * rise + run * run """
        run = self.p2.x - self.p1.x
        rise = self.p2.y - self.p1.y
        return math.sqrt(run * run + rise * rise)

    def midpoint(self):
        """ Calculate the mid point between 2 points."""
        mx = (self.p1.x + self.p2.x)/2
        my = (self.p1.y + self.p2.y)/2
        return Point(mx, my)


def test11():
    """ Simplest construction of a line. """
    aline = Line()
    if aline is not None:
        print("Test_11: PASS", aline)
    else:
        print("Test_11: FAIL")


def test12():
    """ Construct a line segment from 2 points. """
    begin = Point(3, 3)
    end = Point(5, 5)
    segment = Line(begin, end)
    if segment is not None:
        print("Test_12: PASS", segment)
    else:
        print("Test_12: FAIL")


def test13():
    """ Construct a line segment from 1 point, using the default. """
    begin = Point(3, 3)
    segment = Line(begin)
    if segment is not None:
        print("Test_13: PASS", segment)
    else:
        print("Test_13: FAIL")


def test14():
    """Compute the slope of a line"""
    begin = Point(3, 3)
    end = Point(5, 5)
    segment = Line(begin, end)
    line_slope = segment.slope()
    m = slope(begin, end)
    if m == line_slope:
        print("Test_14: PASS")
    else:
        print("Test_14: FAILED m", m, "line_slope", line_slope)


def test15():
    """Compute the intercept of a line"""
    begin = Point(3, 3)
    end = Point(5, 5)
    segment = Line(begin, end)
    line_intercept = segment.intercept()
    intercept = y_intercept(begin, end)
    if line_intercept == intercept:
        print("Test_15: PASS")
    else:
        print("Test_15: FAILED line_intercept", line_intercept, "intercept", intercept)


def test16():
    """Compute the distance of a line segment."""
    begin = Point(3, 3)
    end = Point(5, 5)
    segment = Line(begin, end)
    line_distance = segment.distance()
    d = distance(begin, end)
    if line_distance == d:
        print("Test_16: PASS")
    else:
        print("Test_16: FAIL line_distance", distance, "distance", d)


def test17():
    """Compute the midpoint of a line segment."""
    begin = Point(3, 3)
    end = Point(5, 5)
    segment = Line(begin, end)
    line_midpoint = segment.midpoint()
    mid_point = midpoint(begin, end)
    if line_midpoint == mid_point:
        print("Test_17: PASS")
    else:
        print("Test_17: FAIL line_midpoint", line_midpoint, "midpoint", mid_point)

def test18():
    """Jiachen: try adding something here!"""
    print("This is our first time doing pair programming woot woot!")
    # I think this warrents a pass!
    print("Test_18: PASS")

#the thing is i don't know how to run and i am trying to find it
def test():
    test00()
    test01()
    test02()
    test03()
    test04()
    test05()
    test06()
    test07()
    test08()
    test09()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()
    test16()
    test17()
    test18()
    test19()

test()
