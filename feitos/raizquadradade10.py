#!/usr/bin/python3
#raizquadradade10.py 2161

n = int(input())

def est10(e):
	return 1/ (6 + e)

def raizq10(e):
	d = 3
	h = 0
	for i in range(1, n + 1):
		h = est10(h)
	return d + h   

print("{0:.10f}".format(raizq10(n)))