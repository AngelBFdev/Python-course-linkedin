#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from pathlib import Path

def main():
    # Got the path
    script_location = Path(__file__).absolute().parent

    # Open the file in read and binary mode
    infile = open(f'{script_location}/berlin.jpg', 'rb')

    # Open the file in write and binary mode
    outfile = open(f'{script_location}/berlin-copy.jpg', 'wb')

    while True:
        # read 10240 bytes for the buffer
        buf = infile.read(10240)
        if buf:
            # write in the outfile
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
