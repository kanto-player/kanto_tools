import sys
import random

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: " + sys.argv[0] + " min max N")
        sys.exit(1)

    rmin = int(sys.argv[1])
    rmax = int(sys.argv[2])
    N = int(sys.argv[3])

    for i in range(0, N):
        print (random.randint(rmin, rmax))
