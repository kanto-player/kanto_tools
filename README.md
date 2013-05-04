# Tools for working with FPGAs

## roms/arraygen.py

Helpful tool for generating VHDL array initializers from text.
This tool takes integers line by line from standard input and converts them
into an initializer for a VHDL array.

Usage: arraygen.py size [integers.txt]

The `size` argument is the size of each integer in bits. Arraygen generates
all numbers in hexadecimal, so only multiples of four are accepted.

The optional second argument is a file from which arraygen should read integers
instead of from standard input.

### Example

If integers.txt contains

	5
	2
	3
	12

and we run

	python arraygen.py 4 integers.txt

we get the output

	(x"5", x"2", x"3", x"c")

## roms/mifgen.py

Same interface as arraygen.py, except it generates memory-intialization files
(MIF) instead of array initializers.

## sdcard/crc7\_calc 

Calculates the crc7 of a 40 bit number. You supply the number as the first
argument in hexadecimal. The tool will print out `(crc7 << 1 | 0x1)` in hex.
This number can then be used as the last byte of an SD card SPI command.

## sdcard/text2pcm

Takes textual integers line by line on standard input and writes 16-bit
big-endian signed integers to standard output.

## sdcard/pcm2text

The opposite of text2pcm. Reads 16-bit big-endian signed integers from standard
input and writes their textual form to standard output.

## sdcard/mkauimage.sh

Takes several audio files from standard input and writes then in raw PCM to
an output file. The input files can be in any audio format recognized by `sox`.

All input files are assumed to have a framerate of 44100 Hz. 
Any input file with stereo audio is mixed down to a single channel.

Usage: mkauimage.sh input1 [input2 input3 ...] output

## sdcard/playimage.sh

Plays audio from a raw PCM data file at a rates of 44100 samples / second.

## fft/dftcoeffgen

Generates the coefficients for a 16-point DFT computation.
The ordering of the outputs is that the input index `n` is incremented before
the output index `k`. So the outputs would be ordered in the form.

	k = 0, n = 0
	k = 0, n = 1
	...
	k = 0, n = 15
	k = 1, n = 0
	k = 1, n = 1
	...
	k = 15, n = 15

The format of the output is two integers on each line separated by a space.
The first integer on the line is the real part and the second is the 
imaginary part.


## fft/rccoeffgen

Generates coefficients for an N point FFT recombination. The N is given as
the first argument on the command line. Prints out N / 2 complex integers
to standard output.

## fft/dftsim

Simulates a hardware DFT computation. Takes in 16 real numbers on standard
input and prints out 16 complex numbers to standard output.

## fft/recombsim

Simulates an N point recombination. The N is given as the first argument.
Reads in N / 2 pairs of complex numbers from standard input. The format of
each line should be

	evenreal evenimag oddreal oddimag

Prints out N complex integers to standard output.

## fft/fftsim.sh

Simulates the entire FFT hardware computation including DFT and all 4 
recombination steps.

Takes 256 real numbers on standard input and prints out 256 complex numbers
to standard output.

Optionally, you can give fftsim.sh a file as an argument from which it will
read the input numbers.

## fft/plot.py

Plots textual numbers from standard input. If you give it the string `comp`
as the second argument, it will take complex numbers on standard input
and plot their magnitude.

## fft/comp2real

Takes complex numbers on standard input and writes out their hardware 
representation to standard output. The hardware representation is

	real << 16 | imag
