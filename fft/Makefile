all: dftsim comp2real dftcoeffgen rccoeffgen recombsim sumbins

%: %.c
	gcc -Wall -O2 $< -lm -o $@
