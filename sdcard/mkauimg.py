# Usage: ./mkauimg.py audio1.ogg [audio2.mp3 ...] output.raw
# Takes in several audio files, concatenates them, and converts
# then into raw 16-bit signed-integer big-endian PCM data.
#
# First words contain the lengths of all the files.

import sys
import subprocess
import os
import struct
import mutagen
from mutagen.mp3 import MP3

def get_song_title(filename):
    metadata = mutagen.File(filename)

    if type(metadata) is MP3:
        title = metadata['TIT2'].text[0]
        artist = metadata['TPE1'].text[0]
    else:
        title = metadata['title'][0]
        artist = metadata['artist'][0]

    return str(title + " - " + artist)

def make_header(offset, filename):
    
    if filename is not None:
        title = get_song_title(filename)
        print title

        if len(title) >= 60:
            raise Exception("Song title is too long")

        header = struct.pack(">I", offset) + title
        header = header.ljust(64, '\0')
    else:
        header = struct.pack(">I", offset).ljust(64, '\0')

    return header

if __name__ == '__main__':
    filesizelist = []
    curoff = 1
    offsetlist = [curoff]
    inputs = sys.argv[1:-1]

    if len(inputs) >= 8:
        print "Too many songs. Will only write the first seven."
        inputs = inputs[:7]

    for i, inptfile in enumerate(inputs):
        # convert to PCM using sox
        sox_call = "sox \"" + inptfile + "\" -b 16 -e signed-integer -B -c 1 -t raw tempfileformkau" + str(i)
        print(sox_call)
        os.system(sox_call)

# get number of characters, need to convert to 512byte block
        filelength = os.path.getsize("tempfileformkau" + str(i))
        newlength = int((filelength - 1)/512 + 1)
        filesizelist.append(newlength)
    
    for size in filesizelist:
        curoff += size
        offsetlist.append(curoff)

    print("Track offsets: " + str(offsetlist))

    header = ''.join([make_header(off, fname) 
                        for (off, fname) in zip(offsetlist[:-1], inputs)])
    header += make_header(offsetlist[-1], None)
    header = header.ljust(512, '\0')
    
    f = open(sys.argv[-1], "w")
    f.write(header)

    for i in range(0, len(inputs)):
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
