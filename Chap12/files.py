#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # open a file
    # ('name_file', 'w') -> this will write
    # from ZERO
    # ('name_file', 'a') -> this will write
    # continuing from the end
    # ('name_file', 'r+') -> allow you to read
    # and write
    f = open('lines.txt')
    for line in f:
        # Read a string and remove spaces
        # at the end of the string
        print(line.rstrip())

if __name__ == '__main__': main()
