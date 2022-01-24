#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from pathlib import Path

def main():
    # Got the Path for the parent carpet of the script
    script_location = Path(__file__).absolute().parent

    # write the route and open it for read in text mode
    infile = open(f'{script_location}/lines.txt', 'rt')

    # write the route and open it for write in text mode
    # write mode clean the file and start writing
    outfile = open(f'{script_location}/lines-copy.txt', 'wt')
    for line in infile:
        # write the line from infile into the outfile
        print(line.rstrip(), file=outfile)

        # Also save the lines, but do not strip
        # the spaces at the end
        outfile.writelines(line)

        # print '.' for each line
        # flush start writing dots without
        # needing a new line
        print('.', end='', flush=True)

    # Close the file in order to do not
    # lose data
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
