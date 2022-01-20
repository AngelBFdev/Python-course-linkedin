#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    print_list(seq)
    action(seq,'mul')
    action(seq,'mod')
    action(seq,'tuple')
    action(seq,'import')
    action(seq,'')



def print_list(o):
    for x in o: print(x, end = ' ')
    print()

def action(seq2=0,opt=''):
    # multiply all the elements in the array
    # by two
    if(opt==''):
        seq3 = { x: x**2 for x in seq2}
        print(seq3)

    elif(opt=='mul'):
        seq3=[x * 2 for x in seq2]

    # mod by three all the elements in the
    # array, if the mod is equal 0, it doesn't
    # get print
    elif(opt=='mod'):
        seq3=[x for x in seq2 if x % 3 != 0]

    # list of tuples for each item in the array
    elif(opt=='tuple'):
        seq3=[(x, x**2) for x in seq2]

    # use round method to round the digits of
    # pi by the number in the range array
    elif(opt=='import'):
        from math import pi
        seq3=[round(pi, i) for i in seq2]

    print_list(seq3)


if __name__ == '__main__': main()
