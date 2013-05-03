import sys

def convert_int(x, size):
    fmt = "%%0%dx" % (size / 4)
    return fmt % (x & ((1 << size) - 1))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: mifgen.py width [romfile]")
        sys.exit(1)

    width = int(sys.argv[1])

    if len(sys.argv) >= 3:
        romfile = open(sys.argv[2])
    else:
        romfile = sys.stdin

    values = [int(line.strip()) for line in romfile]
    depth = len(values)

    print("WIDTH=%d;" % width)
    print("DEPTH=%d;\n" % depth)
    print("ADDRESS_RADIX=UNS;")
    print("DATA_RADIX=HEX;\n")
    print("CONTENT BEGIN\n")
    
    for i, val in enumerate(values):
        print("%d : %s;" % (i, convert_int(val, width)))

    print("\nEND;")
