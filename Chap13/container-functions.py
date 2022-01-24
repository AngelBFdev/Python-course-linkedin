#!/usr/bin/env python3

x = (1,2,3,4,5)

# save the reversed value of x tuple
y = list(reversed(x))
print(x)
print(y)

y= reversed(x)
# print each value of y
for i in y: print(i, end=' ')
print()

# Sum the values of the tuple
y = sum(x)
print(y)

# You can continuing adding more values
y = sum(x,10)
print(y)

# max value
y = max(x)
print(y)

# min value
y = min(x)
print(y)

# check if any of the values is true
y = any(x)
print(y)

# check if all of the values are true
y = all(x)
print(y)

# check if any of the values is true
y = ( 6, 7, 8, 9, 10 )
# zip return an iterator with 2 values
# in each items
z = zip( x, y )
for a, b in z: print(f'{a} - {b}')

x = ( 'cat', 'dog', 'rabbit', 'velociraptor' )
# enumerate gives you a number for each item
# starting from 0
for i, v in enumerate(x): print(f'{i}: {v}')

# For more information check the
# python documentation of built-in functions
