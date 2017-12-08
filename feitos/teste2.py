#/usr/bin/python3
#teste.py

n = int(input())

while n != 0:
	e = 1
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if i == j:
				e = i%n or j%n

			print(e, end=" ")
		print()
	print()
	n = int(input())