#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import time

def elapsed_time(f):
    def wrapper():
        # save time at the beginning
        t1 = time.time()

        # call the function send as argument
        # in this case big_sum
        f()

        # save time after the function is done
        t2 = time.time()

        # calculate the responsed time
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


# call function elapsed_time everytime you call function
# big_sum and send it to the 1st function as an argument
@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        # fill the list with numbers from
        # 0 to 10,000
        num_list.append(num)

    # sum all the elements in the list
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__': main()
