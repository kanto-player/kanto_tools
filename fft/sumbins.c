#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	int i, n, res;
	unsigned int sum = 0;
	short real;

	if (argc < 2) {
		fprintf(stderr, "Usage: sumbins n\n");
		exit(EXIT_FAILURE);
	}

	n = atoi(argv[1]);

	for (i = 0; ; i++) {
		res = fscanf(stdin, "%hd\n", &real);
		
		if (res == 0 || res == EOF)
			break;
		else if (res < 0) {
			perror("fscanf");
			exit(EXIT_FAILURE);
		}

		if (i % n == 0 && i != 0) {
			printf("%d\n", sum);
			sum = 0;
		}

		if (real < 0)
			sum -= real;
		else
			sum += real;
	}

	printf("%d\n", sum);

	return 0;
}
