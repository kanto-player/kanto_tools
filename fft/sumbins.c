#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	int i;
	unsigned int sum = 0;
	short real, imag;

	for (i = 0; i < 256; i++) {
		fscanf(stdin, "%hd %hd\n", &real, &imag);
		if (i % 16 == 0) {
			printf("%d\n", sum);
			sum = 0;
		}

		if (real < 0)
			sum -= real;
		else
			sum += real;
	}

	return 0;
}
