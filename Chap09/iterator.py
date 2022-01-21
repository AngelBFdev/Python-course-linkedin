#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# inclusive range used in the function from:
# Chap07/generator.py
class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

        # set _next to the begging
        self._next = self._start

    # identifier for iteration object
    # with this the object is constanly
    # looping
    def __iter__(self):
        return self

    def __next__(self):
        # stop if it's on the limit
        if self._next > self._stop:
            # command to stop the iteration/loop
            raise StopIteration
        else:
            # var r save the value of next
            _r = self._next
            # increment _next by one
            self._next += self._step
            # return the var _r
            return _r

def main():
    for n in inclusive_range(25):
        print(n, end=' ')
    print()

if __name__ == '__main__': main()
