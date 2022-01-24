#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from pathlib import Path

def main():
    # Got the Path for the parent carpet of the script
    script_location = Path(__file__).absolute().parent
    # write the route
    file_location = script_location / 'lines.txt'
    # just to verify the route
    print(file_location)
    # open a file
    # ('name_file', 'w') -> this will write
    # from ZERO
    # ('name_file', 'a') -> this will write
    # continuing from the end
    # ('name_file', 'r+') -> allow you to read
    # and write
    f = open(file_location)
    for line in f:
        # Read a string and remove spaces
        # at the end of the string
        print(line.rstrip())

if __name__ == '__main__': main()
