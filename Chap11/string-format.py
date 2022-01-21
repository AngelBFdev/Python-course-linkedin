#!/usr/bin/env python3

x=42
y=73
print('the number is {}'.format(x))
print('the number is {} {}'.format(x, y))
# You can create variables
print('the number is {xx} {bb}'.format(xx=x, bb=y))
# you can use position arrays to print it
print('the number is {1} {0}'.format(x, y))
# you can use print spaces <(right) >(left)
print('the number is {0:<5} {1:>5}'.format(x, y))
# fill the space with 0
print('the number is {0:<5} {1:>05}'.format(x, y))
# add plus sign
print('the number is {0:<5} {1:>+5}'.format(x, y))
# fill 0 and put a + at the beggining
print('the number is {0:<5} {1:+05}'.format(x, y))

# Numeric format
x= 10000000
# print in readable format (10,000,000)
print('the number is {:,}'.format(x))
# replace , for .
print('the number is {:,}'.format(x).replace(',','.'))
# add decimals
print('the number is {:f}'.format(x))
# add just 3 decimals
print('the number is {:.3f}'.format(x))

# Traductions
# traduce to octal
print('the number is {:o}'.format(y))
# traduce to Hexadecimal
print('the number is {:x}'.format(y))
# traduce to Binary
print('the number is {:b}'.format(y))


