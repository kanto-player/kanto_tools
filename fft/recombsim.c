#include <stdio.h>
#include <complex.h>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>
#include <math.h>

/* Simulates the recombination stage of the FFT computation
 * Takes n / 2 complex number pairs on standard input
 * prints out n complex number pairs on output */

int main(int argc, char *argv[])
{
	int k, n;
	float coeff;
	int16_t coreal, coimag;
	int16_t evenreal, evenimag;
	int16_t oddreal, oddimag;
	int32_t multreal, multimag;
	int16_t *resreal, *resimag;

	if (argc < 2) {
		fprintf(stderr, "Usage: %s N\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	n = atoi(argv[1]);

	resreal = malloc(sizeof(int16_t) * n);
	resimag = malloc(sizeof(int16_t) * n);

	if (resreal == NULL || resimag == NULL) {
		fprintf(stderr, "Could not allocated memory.\n");
		return EXIT_FAILURE;
	}

	for (k = 0; k < n / 2; k++) {
		fscanf(stdin, "%hd %hd %hd %hd\n", &evenreal, &evenimag,
					           &oddreal, &oddimag);
		coeff = SHRT_MAX * cexp(-2 * M_PI * I * k / n);
		coreal = creal(coeff);
		coimag = cimag(coeff);
		multreal = oddreal * coreal - oddimag * coimag;
		multimag = oddreal * coimag + oddimag * coreal;
		evenreal >>= 1;
		evenimag >>= 1;
		multreal >>= 17;
		multimag >>= 17;
		resreal[k] = evenreal + multreal;
		resimag[k] = evenimag + multimag;
		resreal[k + n / 2] = evenreal - multreal;
		resimag[k + n / 2] = evenimag - multimag;
	}

	for (k = 0; k < n; k++) {
		printf("%d %d\n", resreal[k], resimag[k]);
	}

	return 0;
}
