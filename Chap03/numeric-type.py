#!/usr/bin/env python3

# Needed later
from decimal import *

# python read it as float
x = 7 / 3
print('x is {}'.format(x))

# This work as divition of int
x = 7 // 3
print('x is {}'.format(x))

# Gives you the quantity of numbers left out of
# the division
x = 7 % 3
print('x is {}'.format(x))

# Gives you the quantity of numbers left out of
# the division
x = 7 % 3
print('x is {}'.format(x))

# it's not 0 because in float there are 17
# places, and wants to be precise
x = .1 +.1 +.1 -.3
print('x is {}'.format(x))

# Decimal imported in order to have accured
# results with decimal neede for money
a = Decimal('.10')
b = Decimal('.30')
x= a+a+a-b
print('x is {}'.format(x))
