#!/usr/bin/python3
#matrizquadrada1.py 1435

def menor(i, j):
	if i <= j:
		return i
	else:
		return j

def printmenorm(i, j):
	print(menor(i, j), end=" ")

def printmenorj(i, j):
	if j == 1:
		print(menor(i, j))
	else:
		printmenorm(i, j)

def matrizquadrada(n):
	if n%2 == 0:
		d = int(n/2)
		h = d
	else:
		d = int(n/2) + 1
		h = d - 1

	for i in range(1, d + 1):
		for j in range(1, d + 1):
			printmenorm(i, j)
		for j in range(h, 0, -1):
			printmenorj(i, j)
	for i in range(h, 0, -1):
		for j in range(1, d + 1):
			printmenorm(i, j)
		for j in range(h, 0, -1):
			printmenorj(i, j) 
	print()

n = int(input())

while n != 0:
	matrizquadrada(n)
	'''
	if n%2 == 0:
		d = int(n/2)
		#h = d - 1
		h = d
	else:
		d = int(n/2) + 1
		#h = d - 2
		h = d - 1
	
	for i in range(1, n + 1):
		for j in range(1, n + 1):			
			print("{0}{1}".format(i, j), end=" ")		
		print()
	print()
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			print("{0}".format(i + j), end=" ")
		print()
	print()
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			print("{0}".format(i * j), end=" ")
		print()
	print()

	for i in range(1, n + 1):
		for j in range(1, n + 1):
			print("{0}".format(i % j), end=" ")
		print()
	print()

	for i in range(1, n + 1):
		for j in range(1, n + 1):
			print("{0}".format(d % j), end=" ")
		print()
	print()
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			print("{0}".format(d % i), end=" ")
		print()
	print()
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if i < j:
				print("{0}".format(i), end=" ")
			else:
				print("{0}".format(j), end=" ")
		print()
	print()
	'''
	'''
	v = list()
	for i in range(1, d + 1):
		v.append(i)
	print(v)
	print()
	'''
	#teste1
	'''
	for i in range(d):
		for j in range(d):
			print(menor(v[i],v[j]), end=" ")
		for j in range(h, -1, -1):
			print(menor(v[i],v[j]), end=" ")
		print()
	for i in range(h, -1, -1):
		for j in range(d):
			print(menor(v[i],v[j]), end=" ")
		for j in range(h, -1, -1):
			print(menor(v[i],v[j]), end=" ")
		print() 
	print()
	
	for i in range(1, d + 1):
		for j in range(1, d + 1):
			print(menor(i, j), end=" ")
		for j in range(h, 0, -1):
			print(menor(i, j), end=" ")
		print()
	for i in range(h, 0, -1):
		for j in range(1, d + 1):
			print(menor(i, j), end=" ")
		for j in range(h, 0, -1):
			print(menor(i, j), end=" ")
		print() 
	print()



	
	if d%2==0 and d > 2:
		r = int(d/2)
	else:
		r = int(d/2) + 1
	print(d)
	print(r)
	d = d + 1
	for i in range(1, d):
		for j in range(1, d):
			print("{0}{1}".format(i,j), end=" ")

			if i == j:
				e = 1
			else:
				if i > j:
					e = 1
				else:
					e = 0
			print("{0}".format(e), end=" ")
		print()
	for i in range(1, r):
		for j in range(1, r):
			print("{0}{1}".format(i,j), end=" ")
		print()

	'''
	n = int(input())



'''
d = int(input())
p, q, e = 0, 0, 1
while d != 0:
	if(d%2 == 0):
		h = d - 1
		r = int(round(h/2))
		#print(r)
	else:
		h = d - 1
		r = int(round(h/2))
		#i == 0 and j == 0print(r)
	for i in range(d):
		
		for j in range(d):
			if(i == h or j == h) or (i == 0 or j == 0):
				e = 1
			else:
				if(i == r and j == r):
					e = r + 1
				else:
					e = r
			print(e, end=" ")
			e = 1

		print()
'''	
	

#não resolvido - completo V