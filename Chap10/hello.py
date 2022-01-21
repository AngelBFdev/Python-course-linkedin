#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    try:
        x=5/0
    # if a ValueError appear, it says this
    # message and continue
    except ValueError:
        print('I caught a ValueError')
    # if any Error appear, it says this
    # message and continue
    except:
        # print the error info in the
        # position 1 of the array
        print(f'unknown error: {sys.exc_info()[1]}')
    else:
        print('good job!')
        print(x)

if __name__ == '__main__': main()
