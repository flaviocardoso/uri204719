a, b, c = map(float, input().split())

if(((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
	if((pow(a, 2) == ((pow(b, 2)+(pow(c,2))))) and (pow(c, 2) == ((pow(a, 2)+(pow(b,2))))) and (pow(b, 2) == ((pow(a, 2)+(pow(c,2)))))):
		print()
	if(a == b  and b == c and a == c):
		print("TRIANGULO EQUILATERO")
	elif(a == b or b == c or a == c):
		print("TRIANGULO ISOSCELES")
else:
	print("NAO FORMA TRIANGULO")