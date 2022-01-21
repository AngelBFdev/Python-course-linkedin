#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        # You can raise error like this
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

def main():
    try:
        for i in inclusive_range(1,1,1,1):
            print(i, end = ' ', flush = True)
        print()
    # You can even catch your own Error
    # 'as' saves the message of the error
    # as the name you say
    except TypeError as e:
        print(f'range error: {e}')


if __name__ == '__main__': main()
