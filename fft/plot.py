import matplotlib.pyplot as plt
import math
import sys

if __name__ == '__main__':
    imag = False
    if len(sys.argv) >= 2 and sys.argv[1] == "imag":
        imag = True

    if imag:
        vals = [tuple([int(i) for i in s.strip().split(' ')]) for s in sys.stdin]
        plt.plot([math.sqrt(r ** 2 + i ** 2) for (r, i) in vals])
    else:
        vals = [int(s.strip()) for s in sys.stdin]
        plt.plot(vals)
    plt.show()

