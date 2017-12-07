#!/usr/bin/python3
#sequenciacrescente.py 1146

N = int(input())

while N != 0:
	for i in range(1, N + 1):
		print(i, end=" ")
	print()
	N = int(input())