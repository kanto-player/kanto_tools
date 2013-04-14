#include <stdlib.h>
#include <stdio.h>
#include <complex.h>
#include <math.h>
#include <limits.h>
#include <stdint.h>

#define N 16

int main(void)
{
	int16_t coreal, coimag;
	int n, k;
	float complex coeff;

	for (k = 0; k < N; k++) {
		for (n = 0; n < N; n++) {
			coeff = SHRT_MAX * cexp(2 * M_PI * I * k * n / N);
			coreal = (int16_t) creal(coeff);
			coimag = (int16_t) cimag(coeff);

			printf("%d %d\n", coreal, coimag);
		}
	}

	return 0;
}
