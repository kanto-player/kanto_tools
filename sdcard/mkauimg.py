# Usage: ./mkauimg.py audio1.ogg [audio2.mp3 ...] output.raw
# Takes in several audio files, concatenates them, and converts
# then into raw 16-bit signed-integer big-endian PCM data.
#
# First words contain the lengths of all the files.

import sys
import subprocess
import os
import struct

filesizelist = []

for i, inptfile in enumerate(sys.argv[1:-1]):
  # convert to PCM using sox
  sox_call = "sox \"" + inptfile + "\" -b 16 -e signed-integer -B -c 1 -t raw - " + "> tempfileformkau" + str(i)
  print sox_call 
  os.system(sox_call)

# get number of characters, need to convert to 512byte block
  filelength = os.path.getsize("tempfileformkau" + str(i))
  newlength = ((filelength - 1)/512 + 1)
  filesizelist.append(newlength)

header = ''.join([struct.pack(">H", l) for l in filesizelist])
header = header.ljust(512, '\0')
f = open(sys.argv[-1],"a")
f.write(header)

for i, inptfile in enumerate(sys.argv[1:-1]):
  fin = open("tempfileformkau" + str(i), "r")
  data = fin.read()
  f.write(data)

os.system("rm tempfileformkau*")
