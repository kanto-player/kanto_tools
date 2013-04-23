#include <stdio.h>
#include <stdlib.h>

#define TEST_SIZE 512
#define TEST_NB (2 * TEST_SIZE)

int main(int argc, char *argv[])
{
	unsigned char data[2 * TEST_NB];
	unsigned short i;
	FILE * f;

	if (argc < 2) {
		fprintf(stderr, "Usage: %s\n", argv[0]);
		return EXIT_SUCCESS;
	}

	for (i = 0; i < TEST_SIZE; i++) {
		data[2 * i] = (i >> 8) & 0xff;
		data[2 * i + 1] = i & 0xff;
	}

	f = fopen(argv[1], "w");
	if (f == NULL) {
		perror("open()");
		return EXIT_FAILURE;
	}
	if (fwrite(data, 1, TEST_NB, f) != TEST_NB) {
		fprintf(stderr, "Write unsuccessful\n");
		return EXIT_FAILURE;
	}

	fclose(f);

	return 0;
}
