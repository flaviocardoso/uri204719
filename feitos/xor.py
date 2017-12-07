'''
a = int(input())
b = int(input())

abit = "{0:b}".format(a)
bbit = "{0:b}".format(b)

print("%d" % (int(abit, 2) ^ int(bbit, 2)))


while True:
	try:
		a = int(input())
		print("%s" % "{0:b}".format(a))
	except EOFError as e:
		raise e

'''

import sys

v = []

c = sys.stdin.readline()

while c != '':#para terminar precisa de ctr-z
	vet = c.split(" ")

	a = int(vet[0])
	b = int(vet[1])

	abit = "{0:b}".format(a)
	bbit = "{0:b}".format(b)

	xorint = "%d" % (int(abit, 2) ^ int(bbit, 2))

	v.append(int(xorint))

	c = sys.stdin.readline()

for x in v:
	print(x)

'''

c = input()

while c != '':
	print(c)
	c = input()

'''