CC=gcc
CFLAGS=-Wall -O2
EXEC=crc7_calc testdata text2pcm pcm2text

all: $(EXEC)

%: %c
	$(CC) $(CFLAGS) $(LDFLAGS) $< -o $@

clean:
	rm -f $(EXEC)

.PHONY: all clean
