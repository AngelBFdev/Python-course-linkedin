#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    # end: put at the end of the string
    # the paramether that you put in it
    # flush: clean the buffer so it work
    # without it
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending
