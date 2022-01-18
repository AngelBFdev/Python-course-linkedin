#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:

    sound = 'Quaaack!'

    # self is a variable refering to itself,
    # it can have any name
    def quack(self):
        print(self.sound)

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
