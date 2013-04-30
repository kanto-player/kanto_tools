#include <stdio.h>
#include <stdlib.h>

/* Convert 16-bit big endian PCM data to textual integers */

int main(void)
{
	int lowbyte = 0;
	short sample;
	char byte;
	int err;

	while ((err = fread(&byte, 1, 1, stdin)) > 0) {
		if (lowbyte) {
			sample |= byte;
			printf("%hd\n", sample);
		} else 
			sample = byte << 8;
		lowbyte = !lowbyte;
	}

	if (err < 0) {
		perror("fread");
		return -1;
	}

	return 0;
}
