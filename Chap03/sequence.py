#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A list can be modified
x = [ 1, 2, 3, 4, 5 ]
x[2]=42
for i in x:
    print('i is {}'.format(i), end=' - ')
print()

# A tuple can't be modified
x =  (1, 2, 3, 4, 5)
# Gives you an error
# x[2]=42
for i in x:
    print('i is {}'.format(i), end=' - ')
print()

# range: first value is the start
# second value is the end
# third value is how to advance
# (by default is one)
# if it's just one value is the end
x =  range(5, 10, 2)
# Gives you an error
# x[2]=42
for i in x:
    print('i is {}'.format(i), end=' - ')
print()

# In order to being able to modified it
x =  list(range(5, 10, 2))
x[2]=42
for i in x:
    print('i is {}'.format(i), end=' - ')
print()

# A dictionary
x =  { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5}
x['three'] = 42
for k,v in x.items():
    print('k: {}, v: {}'.format(k, v), end=' - ')
print()
