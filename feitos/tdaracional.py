#/usr/bin/python3
#tdaracional.py 1022

def mdc(n, m):
	if n > m:
		mdc = n
	else:
		mdc = m
	while n%mdc!= 0 or m%mdc!= 0:
		mdc -= 1
	return mdc

def mostrar(c1, c2, c3, c4):
	print("{0}/{1} = {2}/{3}".format(c1, c2, int(c3), int(c4)))

def tdaracional(e):
	sn1, op1, sd1, operacao, sn2, op2, sd2 = e
	n1, n2, d1, d2 = int(sn1), int(sn2), int(sd1), int(sd2)

	if(operacao == "+"):
		n, d = n1*d2 + n2*d1, d1*d2
		m = mdc(n, d)
		mostrar(n, d, n/m, d/m)
	elif(operacao == "-"):
		n, d = n1*d2 - n2*d1, d1*d2
		m = mdc(n, d)
		mostrar(n, d, n/m, abs(d/m))
	elif(operacao == "*"):
		n, d = n1*n2, d1*d2
		m = mdc(n, d)
		mostrar(n, d, n/m, d/m)
	elif(operacao == "/"):
		n, d = n1*d2, n2*d1
		m = mdc(n, d)
		mostrar(n, d, n/m, d/m)

n = int(input())

for i in range(n):
	e = input().split(" ")
	tdaracional(e)