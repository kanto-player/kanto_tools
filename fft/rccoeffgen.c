#include <stdio.h>
#include <complex.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>

int main(int argc, char *argv[])
{
	int k, n;
	float coeff;
	short real, imag;

	if (argc < 2) {
		fprintf(stderr, "Usage: %s N\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	n = atoi(argv[1]);
	
	for (k = 0; k < n / 2; k++) {
		coeff = SHRT_MAX * cexp(-2 * M_PI * I * k / n);
		real = creal(coeff);
		imag = creal(coeff);
		printf("%d %d\n", real, imag);
	}

	return 0;
}
