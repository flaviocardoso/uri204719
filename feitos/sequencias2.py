#!/usr/bin/python3
#sequencias2.py 1156
S = 0
i, j = 0, 1
while j <= 39:
	S += (j/pow(2, i))
	j += 2
	i += 1
print("{0:.2f}".format(S))