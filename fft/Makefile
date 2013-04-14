all: simdft comp2real dftcoeffgen rccoeffgen

%: %.c
	gcc -Wall -O2 $< -lm -o $@
