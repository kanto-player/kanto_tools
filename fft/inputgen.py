import numpy as np
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " N W")
        sys.exit(1)
    fs = 44100.
    N = int(sys.argv[1])
    W = float(sys.argv[2])
    i = np.array(range(0, N))
    t = i / fs
    x = (2 ** 15 - 1) * np.cos(2 * np.pi * W * t)
    for real in x:
        print int(real)
