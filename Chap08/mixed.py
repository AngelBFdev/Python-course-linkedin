#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# globals
dlevel = 0 # manage nesting level

def main():
    r = range(11)
    l = [ 1, 'two', 3, {'4': 'four' }, 5 ]
    t = ( 'one', 'two', None, 'four', 'five' )
    s = set("It's a bird! It's a plane! It's Superman!")
    d = dict( one = r, two = l, three = s )
    mixed = [ l, r, s, d, t ]
    disp(mixed)

def disp(o):
    global dlevel

    # 1st step: o = [ l, r, s, d, t ]
    # 2nd step: o = [ 1, 'two', 3, {'4': 'four' }, 5 ]
    # 3rd step: o = 1
    # 1st step: dlevel = 1
    # 2nd step: dlevel = 2
    dlevel += 1
    # 1st step: send it to print_list
    # 2nd step: send it to print_list
    if   isinstance(o, list):  print_list(o)
    elif isinstance(o, range): print_list(o)
    elif isinstance(o, tuple): print_tuple(o)
    elif isinstance(o, set):   print_set(o)
    elif isinstance(o, dict):  print_dict(o)
    elif o is None: print('Nada', end=' ', flush=True)
    # if is not any from above it would print it
    # method repr print with characters, example
    # 'Hola' instead of Hola
    else: print(repr(o), end=' ', flush=True)
    # dlevel = 2 now, minus 1 now is 1
    dlevel -= 1

    if dlevel <= 1: print() # newline after outer

def print_list(o):
    print('[', end=' ')
    for x in o: disp(x)
    print(']', end=' ', flush=True)

def print_tuple(o):
    print('(', end=' ')
    for x in o: disp(x)
    print(')', end=' ', flush=True)

def print_set(o):
    print('{', end=' ')
    for x in sorted(o): disp(x)
    print('}', end=' ', flush=True)

def print_dict(o):
    print('{', end=' ')
    for k, v in o.items():
        print(k, end=': ' )
        disp(v)
    print('}', end=' ', flush=True)

if __name__ == '__main__': main()
