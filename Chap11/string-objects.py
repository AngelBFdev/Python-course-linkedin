#!/usr/bin/env python3

# Method that print backwards
# More info in: Chap09/string.py
class MyString(str):
  def __str__(self):
    return self[::-1]

s = MyString('Hello, World.')
print(s)

# You can add the format later
s = 'Hello, Wold. {}'
print(s.format(42 * 7))
print(s.format(42 * 8))
