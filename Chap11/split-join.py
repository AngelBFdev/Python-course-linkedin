#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is    a long string with    a bunch   of words in it.'
# split method by itself, separate the string
# by the spaces
print(s.split())

s = 'This is a long string with a bunch of words in it.'
# You can choose specific characters to split
# with
print(s.split('i'))

l=s.split()
# This is the way to apply join in python.
s2= ':'.join(l)
print(s2)
