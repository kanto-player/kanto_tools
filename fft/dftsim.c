#include <stdlib.h>
#include <stdio.h>
#include <complex.h>
#include <math.h>
#include <limits.h>
#include <stdint.h>

#define N 16

/* Simulates the DFT stage of the FFT computation
 * Takes 16 numbers line by line on standard input
 * Produces 16 complex number pairs on standard output */

int main(void)
{
	int16_t tdom[N];
	int16_t fdom[N][2];
	float complex coeff;
	int32_t sumreal, sumimag, multreal, multimag;
	int16_t coreal, coimag;
	int n, k;

	for (n = 0; n < N; n++)
		fscanf(stdin, "%hd\n", &tdom[n]);
	
	for (k = 0; k < N; k++) {
		sumreal = 0;
		sumimag = 0;

		for (n = 0; n < N; n++) {
			coeff = SHRT_MAX * cexp(2 * M_PI * I * k * n / N);
			coreal = (int16_t) creal(coeff);
			coimag = (int16_t) cimag(coeff);
			multreal = coreal * tdom[n];
			multimag = coimag * tdom[n];
			sumreal += (multreal >> 4);
			sumimag += (multimag >> 4);
		}

		fdom[k][0] = sumreal >> 16;
		fdom[k][1] = sumimag >> 16;

		printf("%d %d\n", fdom[k][0], fdom[k][1]);
	}

	return 0;
}
