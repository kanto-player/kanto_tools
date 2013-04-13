#include <stdio.h>
#include <stdlib.h>

#define N 16

int main(void)
{
	int i;
	int real, imag, comb;

	for (i = 0; i < N; i++) {
		fscanf(stdin, "%d %d\n", &real, &imag);
		real &= 0xffff;
		imag &= 0xffff;
		comb = (real << 16) | imag;
		printf("%d\n", comb);
	}

	return 0;
}
