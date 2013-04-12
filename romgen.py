#!/usr/bin/env python

import struct
import json
import sys
import math
import os.path

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
    if len(sys.argv) < 2:
        print("Usage: romgen.py romfile.json")
        sys.exit(1)

    with open(sys.argv[1], "r") as jsonf:
        romdata = json.load(jsonf)

    arr = romdata['values']
    dtype = romdata['dtype']
    dsize = romdata['dsize']
    
    vhdltype = {'int': 'signed', 
                'uint': 'unsigned', 
                'float': 'std_logic_vector'}[dtype]

    if dtype == 'float':
        arrstr = convert_float_array(arr, dsize == 64)
    else:
        arrstr = convert_int_array(arr, dsize)

    print "(" + arrstr + ")"
