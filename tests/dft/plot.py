import matplotlib.pyplot as plt
import math
import sys

if __name__ == '__main__':
    vals = [tuple([int(i) for i in s.strip().split(' ')]) for s in sys.stdin]
    plt.plot([math.sqrt(r ** 2 + i ** 2) for (r, i) in vals])
    plt.show()
