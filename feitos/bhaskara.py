from math import sqrt

ent = input()
v = ent.split(" ")
a = float(v[0])
b = float(v[1])
c = float(v[2])

if(a != 0):
	delta = pow(b, 2) - (4 * a * c)
	if(delta >= 0):
		x1 = ((-1 * b) + sqrt(delta)) / (2 * a)
		x2 = ((-1 * b) - sqrt(delta)) / (2 * a)
		print("R1 = %.5f" % x1)
		print("R2 = %.5f" % x2)
	else:
		print("Impossivel calcular")
else:
	print("Impossivel calcular")