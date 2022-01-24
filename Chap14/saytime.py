#!/usr/bin/env python3
# saytime.py by Bill Weinman [http://bw.org/]
# Copyright 2010-2019 The BearHeart Gorup, LLC
# updated 2019-12-02 for python 3.8

import sys
import time

__version__ = '1.3.0'

class numwords():
    '''
        return a number as words,
        e.g., 42 becomes 'forty-two'
    '''

    # dictionary for each segment of a number
    _words = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
        ), 'quarters': (
            'o\'clock', 'quarter', 'half'
        ), 'range': {
            'hundred': 'hundred'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'    # Out Of Range

    def __init__(self, n):
        self._number = n

    def numwords(self, num = None):
        'Return the number as words'
        n = self._number if num is None else num
        s = ''
        if n < 0:           # negative numbers
            s += self._words['misc']['minus'] + ' '
            n = abs(n)
        if n < 10:          # single-digit numbers
            s += self._words['ones'][n]
        elif n < 20:        # teens
            s += self._words['teens'][n - 10]
        elif n < 100:       # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m: s += '-' + numwords(m).numwords()    # recurse for remainder
        elif n < 1000:      # hundreds
            m = n % 100
            t = n // 100
            s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
            if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
        else:
            s += self._oor
        return s

    def number(self, n = None):
        'setter/getter'
        if n is not None:
            self._number = n
        return str(self._number);

class saytime(numwords):
    '''
        return the time (from two parameters) as words,
        e.g., fourteen til noon, quarter past one, etc.
    '''

    _specials = {
        'noon': 'noon',
        'midnight': 'midnight',
        'til': 'til',
        'past': 'past'
    }

    def __init__(self, h = None, m = None):
        self.time(h, m)

    def time(self, h = None, m = None):
        if h is not None:
            self._hour = abs(int(h))
        if m is not None:
            self._min = abs(int(m))
        return (h, m)

    def time_t(self, t = None):
        if t is None:
            t = time.localtime()
        self._hour = t.tm_hour
        self._min = t.tm_min

    def words(self):
        h = self._hour
        m = self._min

        if h > 23: return self._oor     # OOR errors
        if m > 59: return self._oor

        # set the special dictionary to past
        sign = self._specials['past']

        # if it's over 30 min
        if self._min > 30:
            # set the special dictionary to til
            sign = self._specials['til']

            # add 1 hour since it's going to say the remaining
            # time to the next hour: 30 til midnight
            h += 1

            # get the remaining minutes
            m = 60 - m
        # instead of 24 it's 0
        if h > 23: h -= 24
        # to get format of 12 pm and am
        elif h > 12: h -= 12

        # hword is the hours word)
        if h == 0: hword = self._specials['midnight']
        elif h == 12: hword = self._specials['noon']
        else: hword = self.numwords(h)

        if m == 0:
            # just return noon or midnight
            if h in (0, 12): return hword   # for noon and midnight

            # self._words['quarters'][m] is equal to o'clock
            else: return "{} {}".format(self.numwords(h), self._words['quarters'][m])
        if m % 15 == 0:
            # self._words['quarters'][m // 15] equal to 'quarter' or 'half'
            # example: quarter til midnight
            # example: half past one
            return "{} {} {}".format(self._words['quarters'][m // 15], sign, hword)
        # example: fourteen past two
        return "{} {} {}".format(self.numwords(m), sign, hword)

    def digits(self):
        'return the traditionl time, e.g., 13:42'
        return f'{self._hour:02}:{self._min:02}'

class saytime_t(saytime):   # wrapper for saytime to use time object
    '''
        set the time from a time object
    '''
    def __init__(self, t = None):
        self.time_t()

def main():
    # runs if you give an argument
    if len(sys.argv) > 1:
        # if it's equal to test
        if sys.argv[1] == 'test':
            test()
        else:
            # if the argument is 10:30 would run
            # method words from saytime and print
            # half past ten
            try: print(saytime(*(sys.argv[1].split(':'))).words())

            # Error if you give invalid argument
            except TypeError: print('Invalid time ({})'.format(sys.argv[1]))
    else:
        # if no argument print current time
        print(saytime_t().words())

def test():
    st = saytime()
    print('\nnumbers test:')
    list = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30,
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000
    )
    for l in list:
        # set the number in the saytime object by calling
        # the method number from the saytime object
        st.number(l)
        # print the number with words and the number itself
        # using the numwords
        # example: 1 one
        print(l, st.numwords())

    print('\ntime test:')
    list = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15),
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in list:
        # call the method time and set hour and minutes
        # in the object saytime
        st.time(*l)
        # use the method digits, example: 12:00
        # use the method words, example: midnight
        print(st.digits(), st.words())

    # sending no value set it to localtime
    st.time_t() # set time to now
    print('\nlocal time is ' + st.words())

if __name__ == '__main__': main()
