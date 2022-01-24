#!/usr/bin/env python3

class bunny:
  def __init__(self, n):
    self._n = n

  # if you just have repr it would print this
  # method
  def __repr__(self):
    return f'repr: the number of the bunnies is {self._n} \U0001f596'

  # it's the default method of print
  def __str__(self):
    return f'str: the number of the bunnies is {self._n}'

x = bunny(47)

# repr print emojis
print(repr(x))
print(x)

# print the unicode for the emoji
print(ascii(x))

# print the character for the numeric value given
print(chr(128406))

# print the numeric value for the emoji
print(ord('🖖'))

# for more infomation check the documentation
# of the python built-in Functions
