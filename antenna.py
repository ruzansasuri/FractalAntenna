"""
File: antenna.py
Authors : av2833@cs.rit.edu   Akash Venkatachalam
          rps7183@cs.rit.edu  Ruzan Sasuri
          Description: Draws a fractal antenna based on the user input. The user will enter the size of the antenna, the depth and whether he
             wants to draw it as squares or a wire.
"""

import turtle as t
import math

def square(a):
    """
    pre: At the center of the square, pointing away from the center, pen down.
    post: At the center of the square, pointing away from the center, pen down.
    :param a: None size of the square diagonal.
    :return: None
    """
    t.up()
    t.forward(a)
    t.down()
    t.left(135)
    for _ in range(4):
        t.forward(math.sqrt(2) * a)
        t.left(90)
    t.left(45)
    t.up()
    t.forward(a)
    t.left(180)

def squarelevel(a,n,n1):
    """
    pre: At the center of the current depth of the antenna, pointing away from the center, pen down.
    post: At the center of the current depth of the antenna, pointing away from the center, pen down.
    :param a: Overall size of the antenna.
    :param n: Depth of the antenna.
    :param n1: Current depth.
    :return: None.
    """
    s = a / ((math.pow(3,n)) * 2)
    d = a / math.pow(3,n-n1+1)
    if n1 == 1:
        square(s)
        for _ in range(4):
            t.forward(2 * s)
            square(s)
            t.back(2 * s)
            t.left(90)
    else:
        t.up()
        for _ in range(4):
            t.forward(d)
            squarelevel(a,n,n1-1)
            t.back(d)
            t.left(90)
        squarelevel(a, n, n1 - 1)

def wiring(s,n):
    """
    pre: Start of a quarter of the antenna, pen down.
    post:  End of a single quarter  of the antenna.
    :param s: Overall size of the antenna.
    :param n: Current depth of the antenna.
    :return: None
    """
    x = s / math.sqrt(2)
    if n == 1:
        t.forward(x + 1)
        t.left(90)
        t.forward(x - 1)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x - 1)
        t.left(90)
        t.forward(x + 1)
    else:
        wiring(s/9,n-1)
        t.left(90)
        wiring(s/9, n - 1)
        t.right(90)
        wiring(s/9, n - 1)
        t.right(90)
        wiring(s/9, n - 1)
        t.left(90)
        wiring(s/9, n - 1)

def draw():
    """
    To take the user input in regards to the overall size and depth of the antenna, and whether to draw the antenna using
    squares or a single antenna. then draws the antenna based on these choices.
    pre: At the origin, facing eastward, pen down.
    post: a) If s chosen, at the origin, facing eastward, pen down.
          b) If w chosen, at the extreme right point of the antenna, facing north east, with the pen down.
    :return: None.
    """
    size = -1
    n = -1
    choice = 'x'
    while size <= 0:
        size = int(input("Enter the overall size of the antenna(>0): "))
    while n <= 0:
        n = int(input("Enter the depth of the antenna(>0): "))
    while choice != 's' and choice != 'w':
        choice = input("Do you want to see it as square or a single wire(s/w): ")
    t.speed(0)
    if choice == 's':
        squarelevel(size,n,n)
        t.mainloop()
    elif choice == 'w':
        s = size / ((math.pow(3, n)) * 2 * math.sqrt(2))
        t.up()
        t.forward(size/ 2)
        t.left(135)
        t.down()
        for _ in range(4):
            wiring(size,n)
            t.left(90)
        t.mainloop()

if __name__ == '__main__':
    draw()