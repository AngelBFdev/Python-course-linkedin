#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # Set doesn't allow duplicates
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)

    # order the set
    print_set(sorted(a))
    print_set(b)

    # member that are in set a but no in set be
    print_set(a - b)

    # all the members in both
    print_set(a | b)

    # member that are not in both
    print_set(a ^ b)

    # members that are in both
    print_set(a & b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
