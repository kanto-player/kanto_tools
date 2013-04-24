#include <stdio.h>
#include <stdlib.h>

/* Converts text-format numbers on standard input
 * writes out 16-bit big-endian PCM data on standard output */

int main(void)
{
	short sample;
	unsigned char buffer[512];
	int i = 0;

	while (fscanf(stdin, "%hd\n", &sample) == 1) {
		buffer[i] = (sample >> 8) & 0xff;
		buffer[i + 1] = sample & 0xff;
		i += 2;

		if (i == 512) {
			fwrite(buffer, 2, 256, stdout);
			i = 0;
		}
	}

	return 0;
}
