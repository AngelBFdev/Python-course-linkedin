#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class RevStr(str):
    def __str__(self):
        # [::-1]: set:
        # start at the end
        # end at the 0
        # step in -1
        # go backwards
        return self[::-1]

def main():
    # print backwards
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()
