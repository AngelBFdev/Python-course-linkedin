#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

# format is a method in the String object
x=42
print('Hello, World. {}'.format(x))

# You can use format outside a print since
# it's a String method
x=53
s = 'Hello, World. {}'.format(x)
print(s)

# You can use alse the C format
x=64
print('Hello, World. %d' % x)

# You can put f at the begging to call the
# method format
x=75
print(f'Hello, World. {x}')
