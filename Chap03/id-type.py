#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def whatType(n):

  # You use this method to check types
  if isinstance(n,tuple):
    print("tuple")
  elif isinstance(n,list):
    print("list")
  else:
    print("something else")

x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))

# Even though they are the equal,
# their id is different
print(id(x))
print(id(y))

# Since 1 is a set value,
# it has the same id
print(id(x[0]))
print(id(y[0]))

y = [1, 'two', 3.0, [4, 'four'], 5]
whatType(x)
whatType(y)

