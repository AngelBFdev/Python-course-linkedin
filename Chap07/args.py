#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = ('Hello', 'World')
    kitten('meow', 'grrr', 'purr')
    # without * make it just a variable list
    # * send the data in the list as
    # a group of variables
    kitten(*x)


# *args send list
def kitten(*args):
    # runs if you have any argument
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
