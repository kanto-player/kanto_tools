all: simdft comp2real coeffgen

%: %.c
	gcc -Wall -O2 $< -lm -o $@
