#!/bin/bash

# Simulates the hardware FFT compilation using dftsim and recombsim
# Takes 256 numbers line by line on standard input and produces 
# 256 complex number pairs line by line on standard output

if [ -z "$1" ]; then
	cat > fftinputs.txt
	inputs=( $(<fftinputs.txt) )
else
	inputs=( $(<"$1") )
fi

reorder=(0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15)

for i in {0..15}
do
	for j in {0..15}
	do
		base=$(expr $j \* 16 )
		addr=$(expr $base + ${reorder[$i]})
		echo ${inputs[$addr]}
	done | ./dftsim > dft${i}.txt
done

for i in {0..7}
do
	even=$(expr 2 \* $i)
	odd=$(expr $even + 1)
	paste -d " " dft${even}.txt dft${odd}.txt | ./recombsim 32 > recomb1-${i}.txt
done

for i in {0..3}
do
	even=$(expr 2 \* $i)
	odd=$(expr $even + 1)
	paste -d " " recomb1-${even}.txt recomb1-${odd}.txt | ./recombsim 64 > recomb2-${i}.txt
done

for i in {0..1}
do
	even=$(expr 2 \* $i)
	odd=$(expr $even + 1)
	paste -d " " recomb2-${even}.txt recomb2-${odd}.txt | ./recombsim 128 > recomb3-${i}.txt
done

paste -d " " recomb3-0.txt recomb3-1.txt | ./recombsim 256

rm dft{0..15}.txt
rm recomb1-{0..7}.txt
rm recomb2-{0..3}.txt
rm recomb3-{0..1}.txt
