all: simdft comp2real dftcoeffgen

%: %.c
	gcc -Wall -O2 $< -lm -o $@
