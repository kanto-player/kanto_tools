import numpy as np

if __name__ == '__main__':
    fs = 44100.
    W = 10000
    N = 16
    i = np.array(range(0, N))
    t = i / fs
    x = (2 ** 15 - 1) * np.cos(2 * np.pi * W * t)
    for real in x:
        print int(real)
