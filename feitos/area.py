pi = 3.14159

mens = input()

vet = mens.split(" ")

a = float(vet[0])
b = float(vet[1])
c = float(vet[2])

areaT = (a * c) / 2
areaC = pi * c * c
areaTR = (a + b) * c / 2
areaQ = b * b
areaR = a * b

print("TRIANGULO: %.3f" % areaT)
print("CIRCULO: %.3f" % areaC)
print("TRAPEZIO: %.3f" % areaTR)
print("QUADRADO: %.3f" % areaQ)
print("RETANGULO: %.3f" % areaR)