#!/usr/bin/python3
#quadradospares 1073

N = int(input())

for i in range(2, N + 1):
	if(i % 2 == 0):
		print("{0}^{1} = {2}".format(i, 2, pow(i, 2)))