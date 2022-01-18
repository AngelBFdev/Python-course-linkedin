#!/usr/bin/env python3

# ''' is for multiline string
x = '''

Hola
Mundo

'''
print('x is {}'.format(x))

# upper apply uppercase to the string
# lower apply lowercase
# capitalize apply uppercase to the first letter
x = 'seven'.upper()
print('x is {}'.format(x))

# 1 represents the second value given in the formant
# < says to put the values after the number
# if just one value is given that value
# is the number of spaces
# if two values are given the first value is the
# caracter to fill the blanks
x = 'seven {1:<09} {0:>09}'.format(9,123218)
print('x is {}'.format(x))
print(type(x))
