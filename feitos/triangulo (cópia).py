#triangulo e trapézio
a, b, c = map(float, input().split())

if(((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
	print("Perimetro = {0:.1f}".format(a + b + c))
else:
	print("Area = {0:.1f}".format(((a + b) * c) / 2))