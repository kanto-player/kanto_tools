import numpy as np
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " N")
    fs = 44100.
    W = 10000
    N = int(sys.argv[1])
    i = np.array(range(0, N))
    t = i / fs
    x = (2 ** 15 - 1) * np.cos(2 * np.pi * W * t)
    for real in x:
        print int(real)
