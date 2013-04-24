#include <stdio.h>
#include <stdlib.h>

/* Takes complex number pairs line by line on standard input,
 * combines them using the formula num = (real << 16) | imag
 * and then writes them out to standard output */

int main(void)
{
	int real, imag, comb;

	while (fscanf(stdin, "%d %d\n", &real, &imag) == 2) {
		real &= 0xffff;
		imag &= 0xffff;
		comb = (real << 16) | imag;
		printf("%d\n", comb);
	}

	return 0;
}
