# Tools for working with VHDL

## romgen.py

Helpful tool for generating VHDL array initializers from a JSON file.

### Example JSON ROM

	{
		"dtype": "int",
		"dsize": 32,
		"values": [12, 42, 53, 51]
	}

The "dtype" variable can be "int" or "float". The "dsize" can be 8, 16, 32, or 64
for ints and 32 or 64 for floats.
