#!/usr/bin/env python

# Converts a stream of numbers into a VHDL array initializer

import struct
import sys
import math
import os.path
import sys

def convert_int(x, size):
    fmt = "x\"%%0%dx\"" % (size / 4)
    return fmt % (x & ((1 << size) - 1))

def convert_int_array(arr, size):
    return ', '.join([convert_int(x, size) for x in arr])



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: arraygen.py dtype dsize [romfile]")
        sys.exit(1)

    dsize = int(sys.argv[1])
    
    if len(sys.argv) >= 3:
        romfile = open(sys.argv[2])
    else:
        romfile = sys.stdin
    
    values = [int(line.strip()) for line in romfile]
    arrstr = convert_int_array(values, dsize)

    print "(" + arrstr + ")"
