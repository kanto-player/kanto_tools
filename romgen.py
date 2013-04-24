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

def convert_float(x, double=False):
    if double:
        intfmt = '<L'
        floatfmt = '<d'
        stringfmt = 'x\"%016x\"'
    else:
        intfmt = '<I'
        floatfmt = '<f'
        stringfmt = 'x\"%08x\"'

    return stringfmt % struct.unpack(intfmt, struct.pack(floatfmt, x))

def convert_int_array(arr, size):
    return ', '.join([convert_int(x, size) for x in arr])


def convert_float_array(arr, double=False):
    return ', '.join([convert_float(x, double) for x in arr])

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: romgen.py dtype dsize [romfile]")
        sys.exit(1)

    dtype = sys.argv[1]
    dsize = int(sys.argv[2])
    
    if len(sys.argv) >= 4:
        romfile = open(sys.argv[3])
    else:
        romfile = sys.stdin
    
    if dtype == 'float':
        values = [float(line.strip()) for line in romfile]
        arrstr = convert_float_array(values, dsize == 64)
    else:
        values = [int(line.strip()) for line in romfile]
        arrstr = convert_int_array(values, dsize)

    print "(" + arrstr + ")"
