#include <stdio.h>
#include <stdlib.h>

#define N 16

int main(void)
{
	int i;
	int real, imag;

	for (i = 0; i < N; i++) {
		fscanf(stdin, "%d %d\n", &real, &imag);
		printf("%d\n", real << 16 | imag);
	}

	return 0;
}
