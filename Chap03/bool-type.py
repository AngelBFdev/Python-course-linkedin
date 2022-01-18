#!/usr/bin/env python3

def trueStatement(n):
  if n:
    print("True")
  else:
    print("False")

# The following are considered false as well
x = None
print('x is {}'.format(x))
trueStatement(x)

x = 0
print('x is {}'.format(x))
trueStatement(x)

x = ""
print('x is {}'.format(x))
trueStatement(x)

# Any value would made them true
