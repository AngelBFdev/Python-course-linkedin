#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    v = sys.version_info

    # print python version split for each .
    print('Python version {}.{}.{}'.format(*v))

    # print the platform
    print(sys.platform)

    # print the operating system
    print(os.name)

    # all files in PATH
    # print(os.getenv('PATH'))

    # current directory
    print(os.getcwd())

    # generate unicode random (25 digits)
    print(os.urandom(25))

    # translate in hexadecimal
    print(os.urandom(25).hex())

    # random integer between 1-1000
    print(random.randint(1,1000))

    # generate a list from 0-24
    x = list(range(25))
    print(x)

    # shuffle the list
    random.shuffle(x)
    print(x)

    # get the time
    now = datetime.datetime.now()
    print(now)
    # you can print it individually
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__': main()

# For more information use the documentation of
# python in library
