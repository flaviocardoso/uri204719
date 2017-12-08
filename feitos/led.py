#led

#num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

#saida = list()

N = int(input())

for x in range(N):
	SV = input()
	d = 0
	V = len(SV)

	for i in range(V):
		if(SV[i] == '0' or SV[i] == '6' or SV[i] == '9'):
			d = d + 6
		elif(SV[i] == '2' or SV[i] == '3' or SV[i] == '5'):
			d = d + 5
		elif(SV[i] == '1'):
			d = d + 2
		elif(SV[i] == '4'):
			d = d + 4
		elif(SV[i] == '7'):
			d = d + 3
		elif(SV[i] == '8'):
			d = d + 7
	print("{0} leds".format(d))

"""
for x in saida:
	print("{0} leds".format(x))
print()
"""
