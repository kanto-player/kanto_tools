#include <stdio.h>
#include <stdlib.h>

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
