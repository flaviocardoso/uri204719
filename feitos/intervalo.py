#intervalo
ent = float(input())

if(ent < 0 or ent > 100):
	print("Fora de intervalo")
elif(ent <= 25.00):
	print("Intervalo [0,25]")
elif(ent <= 50.00):
	print("Intervalo (25,50]")
elif(ent <= 75.00):
	print("Intervalo (50,75]")
elif(ent <= 100.00):
	print("Intervalo (75,100]")

'''
ent = 0

	if(ent > 100):
		print("Fora de intervalo")
	elif(ent > 75):
		print("Intervalo (75,100]")
	elif(ent > 50):
		print("Intervalo (50,75]")
	elif(ent > 25):
		print("Intervalo (25,75]")
	elif(ent >= 0):
		print("Intervalo [0,25]")
	else:
		print("Fora de intervalo")
	print(ent)
	ent = ent + 0.00001

if(ent < 0):
	print("Fora de intervalo")
elif(ent >= 0 and ent <= 25.0000):
	print("Intervalo [0,25]")
elif(ent >= 25.00001 and ent <= 50.0000000):
	print("Intervalo (25,50]")	
elif(ent >= 50.00000001 and ent <= 75.0000000000):
	print("Intervalo (50,75]")		
elif(ent >= 75.00000000001 and ent <= 100.0000000000000):
	print("Intervalo (75,100]")
else:
	print("Fora de intervalo")
'''