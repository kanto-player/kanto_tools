# Usage: ./mkauimg.py audio1.ogg [audio2.mp3 ...] output.raw
# Takes in several audio files, concatenates them, and converts
# then into raw 16-bit signed-integer big-endian PCM data.
#
# First words contain the lengths of all the files.

import sys
import subprocess
import os
import struct

if __name__ == '__main__':
    filesizelist = []
    curoff = 1
    offsetlist = [curoff]

    for i, inptfile in enumerate(sys.argv[1:-1]):
        # convert to PCM using sox
        sox_call = "sox \"" + inptfile + "\" -b 16 -e signed-integer -B -c 1 -t raw tempfileformkau" + str(i)
        print sox_call 
        os.system(sox_call)

# get number of characters, need to convert to 512byte block
        filelength = os.path.getsize("tempfileformkau" + str(i))
        newlength = ((filelength - 1)/512 + 1)
        filesizelist.append(newlength)
    
    for size in filesizelist[:-1]:
        curoff += size
        offsetlist.append(curoff)

    header = ''.join([struct.pack(">I", l) for l in offsetlist])
    header = header.ljust(512, '\0')
    f = open(sys.argv[-1], "w")
    f.write(header)

    for i in range(0, len(sys.argv) - 2):
        fin = open("tempfileformkau" + str(i), "r")
        data = fin.read(512)
        while len(data) == 512:
            f.write(data)
            data = fin.read(512)

        if len(data) > 0:
            f.write(data)
            padding = '\0' * (512 - len(data))
            f.write(padding)

    for i in range(0, len(sys.argv) - 2):
        os.remove("tempfileformkau" + str(i))
