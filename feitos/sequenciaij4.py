#!/usr/bin/python3
#sequenciaij4 1098

i = 0

while i < 2: #sem o print finam i <= 2
	for j in range(1, 4):
		''' print(type(i) == int)
			print(isinstance(i, int))
		    print(i%1==0)
		'''
		if((i%1)==0):
			i = round(i)
		else:
			i = round(i, 1)

		print("I={0} J={1}".format(i, i+j))
	i += 0.2

for j in range(3):
	print("I=2 J=?")