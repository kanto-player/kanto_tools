#!/usr/bin/env python

# Generate ROM for DFT coefficients

import itertools
import math
from romgen import convert_int_array

if __name__ == '__main__':
    N = 16
    prec = 16
    coeffs = [math.exp(-2 * math.pi * k * n / float(N)) 
                for (k, n) in itertools.product(range(0, N), range(0, N))]
    intcoeffs = [int((2 ** (prec - 1) - 1) * c) for c in coeffs]
    print "(" + convert_int_array(intcoeffs, prec) + ")"
