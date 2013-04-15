all: simdft comp2real dftcoeffgen rccoeffgen recombsim

%: %.c
	gcc -Wall -O2 $< -lm -o $@
