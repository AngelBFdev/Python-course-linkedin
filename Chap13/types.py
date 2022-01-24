#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('STRING')
x = '47'
y = int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

print('ABSOLUTE')
x = -47
# Absolute value: change negative
# to positive
y = abs(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

print('DIVMOD')
x = 47
# return a tuple the divisor,
# and the remaining in this case
# (15, 2)
y = divmod(x,3)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

print('COMPLEX')
x = 47
# return a complex value
y = complex(x,73)
# same as:
# y = x + 73j
print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

# more information in the documentation
# of python built-in functions
