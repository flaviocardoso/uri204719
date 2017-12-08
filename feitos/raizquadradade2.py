#!/usr/bin/python3
#raizquadradade2.py

n = int(input())

def est2(e):
	return 1/ (2 + e)

def raizq2(e):
	d = 1
	h = 0
	for i in range(1, n + 1):
		h = est2(h)
	return d + h   

print("{0:.10f}".format(raizq2(n)))